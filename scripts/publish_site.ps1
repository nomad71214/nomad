param(
  [string]$Message = '',
  [switch]$NoCommit,
  [switch]$NoWait
)

$ErrorActionPreference = 'Stop'
$repo = Split-Path -Parent $PSScriptRoot
Set-Location $repo

function Get-ProxyUrl {
  $client = New-Object System.Net.Sockets.TcpClient
  try {
    $task = $client.ConnectAsync('127.0.0.1', 7897)
    if ($task.Wait(400) -and $client.Connected) { return 'http://127.0.0.1:7897' }
  } catch { }
  finally { $client.Dispose() }
  return ''
}

function Get-Token {
  $src = @'
using System;
using System.Runtime.InteropServices;
[StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
public struct NOMAD_CRED {
  public int Flags; public int Type; public string TargetName; public string Comment;
  public System.Runtime.InteropServices.ComTypes.FILETIME LastWritten;
  public int CredentialBlobSize; public IntPtr CredentialBlob;
  public int Persist; public int AttributeCount; public IntPtr Attributes;
  public string TargetAlias; public string UserName;
}
public class NOMAD_CRED_API {
  [DllImport("advapi32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
  public static extern bool CredRead(string target, int type, int flags, out IntPtr cred);
  [DllImport("advapi32.dll", SetLastError = true)]
  public static extern bool CredFree(IntPtr cred);
}
'@
  if (-not ('NOMAD_CRED_API' -as [type])) { Add-Type -TypeDefinition $src }
  $target = 'GitHub - https://api.github.com/nomad71214'
  $ptr = [IntPtr]::Zero
  if (-not [NOMAD_CRED_API]::CredRead($target, 1, 0, [ref]$ptr)) { return '' }
  try {
    $c = [Runtime.InteropServices.Marshal]::PtrToStructure($ptr, [type][NOMAD_CRED])
    $bytes = New-Object byte[] $c.CredentialBlobSize
    [Runtime.InteropServices.Marshal]::Copy($c.CredentialBlob, $bytes, 0, $c.CredentialBlobSize)
    return ([Text.Encoding]::UTF8.GetString($bytes)).Trim()
  } finally {
    [NOMAD_CRED_API]::CredFree($ptr) | Out-Null
  }
}

if (-not $NoCommit) {
  if (-not $Message) { throw '缺少 -Message, 提交信息写成一句话' }
  $stamp = (Get-Date).ToString('yy/M/d H:mm')
  git add -A
  $staged = git diff --cached --name-only
  if (-not $staged) {
    '没有待提交的改动'
  } else {
    git commit -m "[$stamp] $Message" | Out-Null
    "提交 [$stamp] $Message"
  }
}

$proxy = Get-ProxyUrl
$token = Get-Token
$env:GIT_TERMINAL_PROMPT = '0'
$gitArgs = @('-c', 'http.sslBackend=openssl')
if ($proxy) { $gitArgs += @('-c', "http.proxy=$proxy") }
if ($token) {
  $env:NOMAD_GH_TOKEN = $token
  $helper = '!f() { echo "username=nomad71214"; echo "password=$NOMAD_GH_TOKEN"; }; f'
  $gitArgs += @('-c', 'credential.helper=', '-c', "credential.helper=$helper")
}
$prevEap = $ErrorActionPreference
$ErrorActionPreference = 'Continue'
$out = & git @gitArgs push origin main 2>&1
$pushCode = $LASTEXITCODE
$ErrorActionPreference = $prevEap
$out | ForEach-Object { "$_" }
if ($pushCode -ne 0) { throw '推送失败' }
$env:NOMAD_GH_TOKEN = ''

$head = (git rev-parse HEAD).Trim()
"HEAD $($head.Substring(0, 7))"

if ($NoWait) { return }
if (-not $token) { '没有取到令牌, 跳过部署状态查询'; return }

$headers = @{ Authorization = "Bearer $token"; 'User-Agent' = 'nomad-publish' }
$req = @{
  Uri        = 'https://api.github.com/repos/nomad71214/nomad/actions/runs?per_page=10'
  Headers    = $headers
  TimeoutSec = 30
}
if ($proxy) { $req['Proxy'] = $proxy }

$run = $null
for ($i = 0; $i -lt 10; $i++) {
  Start-Sleep -Seconds 6
  $r = Invoke-RestMethod @req
  $run = $r.workflow_runs | Where-Object { $_.head_sha -eq $head } | Select-Object -First 1
  if ($run -and $run.status -eq 'completed') { break }
}
if (-not $run) { '等到超时, 还没有出现构建记录, 稍后到 Actions 页面看'; return }

"构建 $($run.status) / $($run.conclusion)"
if ($run.conclusion -ne 'success') { throw '构建失败, 到 Actions 页面看日志' }
"站点 https://nomad71214.github.io/nomad/"