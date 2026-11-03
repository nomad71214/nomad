@echo off
chcp 65001 >nul
cd /d "%~dp0"
where python >nul 2>nul
if errorlevel 1 (
  echo 没有找到 python, 先装 Python 再试
  pause
  exit /b 1
)
python scripts\inbox.py
echo.
pause