


# 1 前言

(1) 适合有一定 C 语言和单片机基础的同学进一步学习 STM32 的开发
使用的是 F103C8T6
(2) 参考: 第二节-C 语言&单片机入门
https://robotega.feishu.cn/wiki/EcQAwzpb1iF4xJkWSKwc4NjTn0f

------

# 2 开发环境配置

以大疆官方 C 板 (RoboMaster 开发板 C 型) 为例
完成 CLion + STM32CubeMX 工具链的配置

参考博客: RoboMaster 配置 C 型开发板的 CLion 与 STM32CubeMX 开发环境
https://blog.csdn.net/weixin_68190597/article/details/143009084

另有更新版教程: Windows 11 使用 Scoop 配置 STM32 C/C++ 开发环境
https://robotega.feishu.cn/wiki/FOPFwh7lOimiCTk8u4XcSb7MnCb
除 CLion 外的部分都可以参考这个新教程


## 2.1 环境说明

请尽量严格按照以下版本安装
否则可能导致冲突或不适配

(1) 操作系统: Windows 11
(2) 开发板: RoboMaster 大疆 C 型开发板, STM32F407IGHx
(3) 下载器: ST-Link 下载器
(4) STM32CubeMX v 6.12.1
(5) CLion v 2024.2.2
(6) OpenOCD v 20240916
(7) MinGW64 v 14.2.0
(8) arm-none-eabi-gcc v 13.3.rel1
(9) ST-Link 驱动程序


## 2.2 软件安装

注意理清每个软件的安装地址
后续配置路径会用到
且尽量避免使用中文路径
否则容易报错
建议全部放在一个文件夹中
例如 `D:/STM32`


### 2.2.1 CLion

CLion 是 JetBrains 旗下的一款开发软件
帮助开发者编写, 运行和测试 C/C++ 程序

(1) 官网下载链接
https://www.jetbrains.com/clion/download/#section=windows
(2) 建议直接下载 JetBrains Toolbox APP
这样可以在 APP 内下载 CLion 和其他开发软件
(3) 下载安装后提示选择 30 天免费试用
或者登录 JetBrains 账号获取许可
注意学生可以免费使用
申请地址: https://www.jetbrains.com/shop/eform/students


### 2.2.2 STM32CubeMX

STM32CubeMX 是 ST 公司提供的一款图形化工具
主要用于简化 STM32 微控制器的配置和代码生成过程

(1) 官网下载地址
https://www.st.com/en/development-tools/stm32cubemx.html#get-software


### 2.2.3 OpenOCD

OpenOCD (Open On-Chip Debugger) 是一款开源工具
主要用于调试嵌入式设备中的微控制器
它支持多种调试和编程接口
特别适用于通过 JTAG 与 SWD 等调试协议
与 ARM Cortex 系列微控制器 (如 STM32 等) 进行通信

(1) 下载链接
https://gnutoolchains.com/arm-eabi/openocd/
(2) 注意官网下载的 OpenOCD 可能会出现 CLion 无法读取的情况
所以建议在上面这一链接中下载
(3) 下载后解压
可以得到 `bin` `drivers` `shares` 三个文件夹
请记住它们的地址
后面会用到
(4) 添加环境变量: 编辑 `Path`
新建其 `bin` 文件夹地址并保存
(5) 启动 cmd
输入 `openocd -v`
能输出版本信息即表示安装成功


### 2.2.4 MinGW

MinGW 是一种编译工具
提供 GNU 编译器集合 (GCC) 及相关工具
使你可以在 Windows 系统上编译 C 与 C++ 等语言的代码

(1) 官方下载地址
https://github.com/niXman/mingw-builds-binaries/releases
(2) 下载解压后 在环境变量中编辑 `Path`
新建其 `bin` 文件夹地址
请注意连续点击多个 "确定" 才能保存
(3) 添加到环境变量后 启动 cmd
输入 `gcc -v`
能输出版本信息即表示安装完成


### 2.2.5 arm-none-eabi-gcc

arm-none-eabi-gcc 用于编译运行在 ARM 架构微控制器上的裸机应用程序

(1) 官方下载地址
https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads
(2) 同样地 下载解压后
将其 `bin` 文件夹路径添加至 `Path` 环境变量中
(3) 然后在 cmd 中输入 `arm-none-eabi-gcc -v`
能输出版本信息即表示安装成功


### 2.2.6 ST-Link 驱动程序

使用 ST-Link 下载器才需要安装这一驱动程序
如果使用的是 Dap-Link 需要安装其他驱动

电脑 USB 插上 ST-Link 后 (另一端连接 C 板 SWD 接口)
在设备管理器的 "其他设备" 中
会出现一个带黄色感叹号的 ST-Link 设备
这表示没有安装相关驱动
点击更新驱动
选中本地 OpenOCD 安装地址中 `drivers` 文件夹里的 ST-Link
即可安装驱动程序
若不再出现黄色感叹号
即表示安装成功


## 2.3 软件配置

启动 CLion
打开设置 (Settings)
依次完成以下几项配置

(1) 配置 OpenOCD 和 STM32CubeMX 的启动地址
指向前面解压得到的 `bin` 目录
(2) 配置工具链 (Toolchains)
指向 MinGW 与 arm-none-eabi-gcc 的安装路径
(3) 确认 CMake 配置
即 CMake 的默认生成器等选项

[点拨] 这三处都在 `Settings → Build, Execution, Deployment` 下
分别对应 `Toolchains` `CMake` `Embedded Development`
OpenOCD 与 STM32CubeMX 的路径就在 Embedded Development 页
若 CLion 里找不到 `Embedded Development` 页
说明该版本的 CLion 未启用 STM32 支持
需要安装或启用对应插件
配错路径的典型症状是后面编译时提示找不到 `cmake`
`arm-none-eabi-gcc` 或 `openocd`


## 2.4 创建工程

以上完成了所有环境的搭建
接下来以点亮 C 型开发板的 LED 灯为例搭建工程

按大多数博主的教程
是先在 CLion 中创建 MX 工程
但这样非常不方便
如此做就必须保证 MX 的文件名和地址与 CLion 中的一致
这样才能更新 CLion 中的代码
对于初学者无疑加大了开发难度
因此这里直接在 CubeMX 中创建工程
然后用 CLion 打开工程

启动 STM32CubeMX
等待软件完成相关下载与配置
然后点击 `File → New Project`
等待其完成更新
如果报错无法下载 mcudoc 可直接忽略
随后进入板卡选择界面
对于大疆 C 型开发板
选择 `STM32F407IGHx`
双击
接下来开始依次配置板卡

(1) 配置时钟
在 `Pinout & Configuration` 一栏
左侧 `System Core` 中选择 `RCC`
将 `High Speed Clock` 设置为 `Crystal/Ceramic Resonator`
即外部晶振
(2) 配置调试方式
点击 `SYS`
`Debug` 选择 `Serial Wire`
即 SWD 调试
(3) 配置主频
点击顶部 `Clock Configuration`
在时钟树中完成主频相关配置
(4) 配置 GPIO 输出
查询原理图可以知道
C 板的 LED 灯引脚为 `PH10` `PH11` `PH12`
因此在 MX 中直接点击板上的这三个引脚
将其设置为 `GPIO_Output`
然后将电平拉高
如果需要还可配置引脚名称
(5) 工程文件名和路径配置
点击顶部 `Project Manager`
设置名字为 `LED`
IDE 选择为 `SW4STM32`
或者 `STM32CubeIDE`
(6) 代码生成选项
点击左侧 `Code Generator`
勾选 `Generate peripheral initialization as a pair of '.c/.h' files per peripheral`

如此便完成了工程文件的搭建
点击右上角 `GENERATE CODE`
即可得到 CLion 可以识别的代码

[点拨] `Project Manager → Project → Toolchain/IDE` 必须选
`SW4STM32` 或 `STM32CubeIDE`
选成 `MDK-ARM` 或 `IAR` 生成的是 Keil 与 IAR 工程
CLion 打不开
`Code Generator` 里每个外设生成一对 .c/.h 的勾选项
决定了外设初始化代码是全部塞进 `main.c`
还是按外设分文件
后续改代码时按文件找更方便
建议一直勾上
另外生成路径同样要避免中文


## 2.5 编译

启动 CLion
点击左上角 "打开项目"
将刚才 MX 生成的工程目录 `LED` 作为项目文件夹
此时可能会提示选择板卡
但是标准库中没有 407IG
所以跳过

接下来需要完成一项配置文件
在工程目录中新建文件夹 `config`
然后新建文件 `stlink.cfg`
将下面这段代码粘入其中
保存

```ini
# choose st-link/j-link/dap-link etc.
#adapter driver cmsis-dap
#transport select swd
source [find interface/stlink.cfg]
transport select hla_swd
source [find target/stm32f4x.cfg]
# download speed = 10MHz
adapter speed 10000
```

这段代码主要指定了下载器是 stlink
如果用的是 stlink 的话
板卡是 stm32f4x
有了这个配置文件 OpenOCD 才能识别板卡
并完成烧录

随后点击右上角编译
如果没有出现这几个图标
可以重启 CLion
出现编译成功的结果即可

[点拨] `config/stlink.cfg` 里有两条 source 语句
`source [find interface/stlink.cfg]`
`source [find target/stm32f4x.cfg]`
两条都相对 OpenOCD 自带脚本目录查找
即 `share/openocd/scripts`
不要改成绝对路径
若用的是 DAP-Link
则要反过来注释掉 stlink 那两行
启用 `adapter driver cmsis-dap`
以及 `transport select swd`
速度 `10000` 即 10 MHz
在排线较长或不稳时可先降到 `1000` 排查


## 2.6 烧录

接下来进行烧录

(1) 点击右上角 "编辑配置" (Edit Configurations)
新建一个 `OpenOCD Download & Run` 配置
即 OpenOCD 下载运行
点击确定
(2) 然后选择该运行文件
点击运行

如果输出提示 OpenOCD 没有识别到板卡
可能是因为 ST-Link 驱动没有安装成功
或者 ST-Link 与 C 板的接口 SWD 连接不稳
请检查连接

如果成功烧录
输出仍有红色 info
但是无 error
并且将看到 C 板 LED 灯亮起
亮灯种类与 MX 中拉高的引脚的电平有关
可以尝试分别亮几个颜色的灯
以确保成功烧录

------

# 3 Git

参考 Git, GitHub 通用教程
https://robotega.feishu.cn/wiki/CyKwwCkE4iWGcrkpOqBcZtKin5f

[点拨] 培训中 Git 主要用于工程版本管理与队友协作
每完成一个可用版本就提交一次
改动前先建分支
避免多人同时改同一份工程文件时互相覆盖

------

# 4 GPIO


## 4.1 简介

GPIO 即通用输入/输出口
是 STM32 最基本也最常用的外设之一
(1) 可将芯片引脚配置为输入, 输出, 复用或模拟模式
用于连接按钮, LED, 传感器等外部器件
(2) 用户可通过配置 GPIO 的输入/输出模式
上下拉, 电平状态等参数
实现数字信号的读取与控制
是嵌入式系统中进行硬件交互的基础接口


## 4.2 基本原理

待补充


## 4.3 常用函数

```c
//读取函数
HAL_GPIO_ReadPin(GPIOB,GPIO_PIN_13);
//写入函数
HAL_GPIO_WritePin(GPIOB,GPIO_PIN_13,GPIO_PIN_SET);
//翻转函数
HAL_GPIO_TogglePin(GPIOB,GPIO_PIN_13);
```


## 4.4 实践例程


### 4.4.1 闪烁小灯

```c
while(1){
    HAL_GPIO_TogglePin(GPIOC,GPIO_PIN_13);
    HAL_Delay(1000);
}
```

注: `HAL_Delay` 函数需要依赖 System tick timer 中断
中断相关知识将在后续呈现


### 4.4.2 按键翻转小灯亮灭

```c
while(1){
    if(HAL_GPIO_ReadPin(GPIOA,GPIO_PIN_1) == GPIO_PIN_SET){
        HAL_Delay(10);
        if(HAL_GPIO_ReadPin(GPIOA,GPIO_PIN_1) == GPIO_PIN_SET){
           HAL_GPIO_TogglePin(GPIOC,GPIO_PIN_13);
        }
    }
}
```

[点拨] 按键引脚在 CubeMX 的 Pinout 视图里要把 GPIO mode 设为 `Input`
并在 GPIO 配置页把 Pull-up/Pull-down 选成与硬件一致的一项
按键另一端接地就选 `Pull-up`
按下读到低电平
接 VCC 就选 `Pull-down`
代码里 `HAL_Delay(10)` 即为简单的软件消抖
实际工程建议 10~20 ms 后再判一次
或改用定时器/中断消抖

------

# 5 中断


## 5.1 简介


### 5.1.1 什么是中断

中断是处理器对外部事件的即时响应机制
外部事件如按键按下, 定时器溢出, 数据接收完成
当事件发生时 CPU 暂停当前任务
转去执行中断服务程序 (ISR)
完成后返回原任务继续执行


### 5.1.2 中断的作用

(1) 实时响应事件, 提高系统效率, 无需轮询
(2) 实现多任务并行处理, 如数据采集与通信同步
(3) 低功耗设计, 用中断唤醒休眠的 CPU
(4) 注意要让中断尽快执行完成
以将中断对正常流程的影响降到最低


### 5.1.3 中断类型

(1) 外部中断: 由 GPIO 引脚触发, 如按键
(2) 内部中断: 由外设事件触发, 如串口接收完成, 定时器溢出
(3) 异常中断: 由 CPU 异常触发, 如非法指令, 除零错误


## 5.2 基本原理

中断机制的核心组成
(1) 中断信号
外设事件 -> 触发中断控制器 -> CPU 被打断 -> 执行 IRQ_Handler()
(2) 事件信号 (Event)
外设事件 -> 硬件触发器 -> 另一外设直接响应 -> 无需 CPU 参与
例如 ADC 由定时器触发采样


### 5.2.1 中断线

(1) 外部中断线 (EXTI0-EXTI19) 与 GPIO 口的映射关系
(2) 每个外部中断线对应的输入源

[点拨] EXTI 线是按引脚号复用的
PA1, PB1, PC1 争用同一条 EXTI1
所以 CubeMX 里若已把 PA1 设为 GPIO_EXTI1
再把 PB1 也设成 EXTI 就会报引脚冲突
需要回到 Pinout 视图把其中一个改成普通 GPIO


### 5.2.2 中断源与触发条件

(1) 外部中断: GPIO 引脚电平变化, 通过 EXTI 控制器触发
1. 支持上升沿, 下降沿, 双边沿触发
2. 例如按键按下 (低电平) 或传感器信号跳变
(2) 内部中断
1. 定时器溢出 (TIMx_UP_IRQn), ADC 转换完成, UART 接收数据等
2. 例如定时器每隔 1 秒触发一次中断


### 5.2.3 NVIC (嵌套向量中断控制器)

(1) 功能: 管理中断优先级和使能/禁用中断通道
(2) 优先级规则
1. STM32 优先级分为抢占优先级和响应优先级
2. 抢占优先级高的中断可以打断低抢占优先级的中断, 即嵌套
3. 若抢占优先级相同, 响应优先级决定执行顺序, 但不可嵌套
4. 优先级分组通过 HAL_NVIC_SetPriorityGrouping() 配置
例如分组 2: 2 位抢占, 2 位子优先级
也可以在 CubeMX 中直接配置

[点拨] Cortex-M 的优先级数值越小越高, 0 最高
优先级分组决定 4 位优先级里几位给抢占, 几位给子优先级
例如 NVIC_PRIORITYGROUP_2 为 2 位抢占 (0 到 3)
再加 2 位子优先级 (0 到 3)
分组一旦在 HAL_Init() 里定下
整个工程内所有中断的 HAL_NVIC_SetPriority() 都要按同一分组理解
否则设了优先级却不抢占往往就是分组与数值不匹配


### 5.2.4 中断处理流程

(1) 中断触发: 外设检测到事件, 如 GPIO 电平变化
(2) 中断请求: 外设向 NVIC 发送中断请求信号
(3) 优先级仲裁: NVIC 比较当前中断与正在执行中断的优先级
1. 若新中断优先级更高, 暂停当前 ISR, 执行新中断, 即抢占
(4) 上下文保存: CPU 自动将程序计数器 (PC), 状态寄存器 (xPSR) 等压入堆栈
(5) 跳转至 ISR: 根据中断向量表找到对应中断服务函数入口地址
(6) 执行 ISR: 运行用户编写的处理代码, 如翻转 LED
(7) 中断返回
1. 通过 __ISB() 或 __DSB() 指令确保操作完成
2. 恢复上下文, 返回原程序继续执行


### 5.2.5 中断向量表与映射

(1) 定义: 位于 Flash 起始地址的数组, 存储所有中断服务函数的入口地址
(2) 通过 void (*const g_pfnVectors[])(void) 重定义
需修改启动文件
(3) 示例

```plaintext
// 在启动文件startup_stm32fxxx.s中
__Vectors DCD __initial_sp          ; 栈顶地址
           DCD Reset_Handler        ; 复位中断
           DCD NMI_Handler         ; NMI中断
           ...
           DCD EXTI0_IRQHandler     ; EXTI Line0中断
```


## 5.3 常用函数


### 5.3.1 中断服务函数

```c
void EXTI0_IRQHandler(void){
    HAL_GPIO_EXTI_IRQHandler(GPIO_PIN_0); //处理EXTI0中断
}
```


### 5.3.2 中断处理公用函数

```c
void HAL_GPIO_EXTI_IRQHandler(uint16_t GPIO_Pin){
    if (__HAL_GPIO_EXTI_GET_IT(GPIO_Pin)!=RESET) //是否真的触发中断
    {
    __HAL_GPIO_EXTI_CLEAR_IT(GPIO_Pin);           // 清除中断挂起标志
    HAL_GPIO_EXTI_Callback(GPIO_Pin);             // 调用用户回调函数
    }
}
```

[点拨] 调用链是 EXTIx_IRQHandler()
它在启动文件里是弱定义
再调用 HAL_GPIO_EXTI_IRQHandler()
这是 HAL 公用函数, 负责查标志与清标志
最后调用 HAL_GPIO_EXTI_Callback()
这是用户回调, __weak 空实现
所以用户只该重写 Callback, 不要重写 IRQHandler
若自己写 IRQHandler 却忘了清标志
会一出中断就原地反复重入
表现为程序卡死在中断里


### 5.3.3 中断回调函数

```c
/* USER CODE BEGIN 4 */
void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin){
    switch(GPIO_Pin){
        case GPIO_PIN_0:                  // 引脚PC0对应的中断处理任务
        /* GPIO_PIN_0 EXTI handling */
        break;
        case GPIO_PIN_13:
        /*GPIO_PIN_13 EXTI handling */    // 引脚PC13对应的中断处理任务
        break;
        case GPIO_PIN_x:                  // 引脚PCx对应的中断任务
        /* GPIO_PIN_x EXTI handling */
        break;
        ......
        default:  break;
    }
}
/* USER CODE END 4 */
```


## 5.4 实践例程


### 5.4.1 设计思路

(1) 在 CubeMX 中设置中断触发条件, 中断优先级, 使能外设中断
(2) 清除中断标志, 改写中断服务函数


### 5.4.2 设计流程


#### 5.4.2.1 CubeMX 配置

(1) RCC - High Speed Clock - 选择 Crystal/Ceramic Resonator
(2) SYS - Debug - 选择 Serial Wire
(3) 设置 PC13 为 GPIO_Output, 设置为推挽输出, 以实现点灯功能
请回忆第一节内容
(4) 可以设置 PC13 的用户标签为 LED, 方便记忆
(5) 以 PA1 引脚为例, 设置 PA1 为 GPIO_EXTI1
1. 根据你搭的外部电路, 选择上升沿/下降沿, 外部中断触发
2. 上下拉选项根据你的外部电路自行选择
3. 可以设置 PA1 的标签为 KEY, 方便记忆
(6) 在 NVIC 选项栏中勾选 EXTI line1 interrupt

[点拨] 引脚设成 GPIO_EXTIx 只是把线接到 EXTI 上
中断还得单独在 NVIC 页勾选对应 EXTI line 才会真正使能
只配引脚不勾 NVIC, 现象是电平变了但回调从不进
另外 NVIC 页里该行的 Preemption Priority 就是抢占优先级
改完记得确认与 HAL_Init() 里的分组设置一致

(7) 时钟配置到 72MHz
(8) 按下回车, 使其自动寻找时钟树配置
(9) 配置好项目名称和储存位置
(10) Toolchain 改为 STM32CubeIDE
(11) 然后点击生成代码
(12) 在 main.c 中, 编写 HAL_GPIO_EXTI_Callback 函数, 覆盖原有定义
1. 检测按下的 GPIO 是否为 KEY_Pin
如果是, 反转 LED 引脚的电平
2. 思考这种做法有什么漏洞


#### 5.4.2.2 硬件连接

(1) STM32 PC13 --> 220Ω 电阻 --- LED 阳极, LED 阴极 --- GND
(2) STM32 PA1 --> 按键引脚 1, 按键引脚 2 --- STM32 GND


### 5.4.3 程序代码

https://github.com/juiceooorange/Interrupt_eg.git


### 5.4.4 结果展示


## 5.5 拓展训练


### 5.5.1 多优先级中断控制 LED

(1) 通过配置两个外部中断按键实现以下功能, 两个按键优先级不同
1. 低优先级按键 (PA1)
按下后切换 LED 工作模式: 常亮 -> 慢闪 -> 快闪 -> 关闭
2. 高优先级按键 (PA0)
按下后立即强制关闭 LED, 即紧急停止
之后再按低优先级按键依然有相应响应
(2) CubeMX 配置
1. GPIO 配置
PC13: 推挽输出, 标签 LED
PA0: 外部中断 (EXTI0), 下拉, 默认高电平, 按下接地, 标签 EMG_KEY
PA1: 外部中断 (EXTI1), 下拉, 标签 MODE_KEY
2. NVIC 配置
EXTI0 中断 (PA0): 优先级 0, 最高
EXTI1 中断 (PA1): 优先级 1
3. 时钟配置: 72MHz 系统时钟
(3) 设计思路
1. 普通模式切换
通过低优先级按键循环切换 LED 状态, 含常亮, 慢闪, 快闪, 关闭
2. 紧急停止功能
通过高优先级按键立即关闭 LED

------

# 6 串口 UART


## 6.1 简介

UART 是一种通信协议和硬件接口
用于在计算机系统和外部设备之间进行异步数据传输
它是一种简单且常见的串行通信方式
广泛应用于嵌入式系统, 单片机和通信设备中

(1) 串口也称串行通信接口
按电气标准及协议来分
包括 RS-232-C, RS-422, RS485, USB, TTL 等
RS-232-C, RS-422 与 RS-485 标准只对接口的电气特性做出规定
不涉及接插件, 电缆或协议

(2) 串口指物理接口形式(硬件)
而 TTL, RS-232, RS-485 指的是电平标准(电信号)
RS232 信号的逻辑 1(高电平)电压为 -15V
逻辑 0(低电平)电压为 +15V
而 TTL 的电压则是 0V~5V

(3) 嵌入式系统里面单片机的串口一般都是 TTL 电平


## 6.2 基本原理

UART 的英文全称是 Universal Asynchronous Receiver/Transmitter
意为通用异步收发传输器
UART 有两根数据线 TX 和 RX
可以以全双工的形式进行发送和接收数据
同一时刻
两条链路的发送器和接收器可以同时传输数据


### 6.2.1 异步传输

(1) 以 1 个字符为传输单位
传输 2 个字符之间的时间间隔是未知的
但是同一字符内相邻位间的时间间隔是确定的
这涉及到 UART 传输速率的概念
即波特率
波特率的单位是 bps
全称 bit per second
意为每秒钟传输的 bit 数量

(2) 举例: 收发时 UART1 以 9600 波特率发送 0x33
先在数据线上放 1 个 104us 脉宽的低电平(起始位)
然后是连续 2 个 104us 脉宽的高电平(2 bit 逻辑 1)
依次类推
接收端以 9600 波特率接收 0x33
通过数这些数据的脉宽来确认数据


### 6.2.2 通信方式

(1) 串行通信
数据是一位一位地通过 TX/RX 引脚传输的
但 MCU 内部处理数据通常是以字节(8 位)为单位的
也就是并行处理

(2) STM32 的 USART 接口(TTL 电平)与 PC 的 USB 接口通信
需要 CH340
1. 电平转换: 3.3V/5V TTL 电平 ↔ USB 差分
2. 电平协议转换: 串口 UART 协议 ↔ USB 协议

(3) UART 帧数据格式: 1 个起始位 + 8 个数据位 + 1 个停止位
无校验位
对应下面初始化函数中的 WordLength, StopBits, Parity 配置


### 6.2.3 轮询的底层机制

(1) 发送: CPU -> 发送数据寄存器 -> 发送移位寄存器 -> TX 输出
(2) 接收: RX -> 接收移位寄存器 -> 接收数据寄存器 -> CPU


### 6.2.4 中断的底层机制

(1) 发送: 发送数据寄存器非空中断
(2) 接收: 接收寄存器非空中断


## 6.3 硬件电路引脚


## 6.4 UART 类别

(1) 阻塞式通信
1. 发送: MCU 以同步逐字节传输方式将数据送入外设发送缓冲区
在此期间, MCU 持续等待外设完成当前字节的发送操作
无法执行其他任务
直至全部数据发送完成
2. 接收: MCU 主动轮询接收端口状态
持续检测数据到达信号
当检测到有效数据时
逐字节读取并存储
此过程中 CPU 始终处于忙等待状态

(2) 中断式通信
1. 发送: MCU 向外设发送单字节数据后
立即释放 CPU 控制权执行其他任务
外设完成该字节发送后
通过硬件中断信号通知 MCU
MCU 响应中断后继续发送下一字节
2. 接收: 外设接收到数据时触发接收中断事件
MCU 暂停当前任务
在中断服务程序(ISR)中逐字节读取数据
完成后返回主程序

(3) DMA 中断通信
直接内存访问 Direct Memory Access
将在后续详细介绍 DMA
1. 发送: MCU 向 DMA 控制器配置源数据地址, 目标外设地址及数据长度
DMA 接管数据传输任务
将数据从内存批量搬运至外设发送缓冲区
传输完成后
DMA 通过中断通知 MCU
2. 接收: MCU 初始化 DMA 的目标存储地址与传输长度
并设定触发条件(如外设数据就绪)
DMA 自动将外设数据搬运至指定内存区域
完成后触发中断通知 MCU 处理

(4) 空闲中断
中断触发条件与接收的字节数无关
实现 UART 收发不定长数据


## 6.5 常用函数


### 6.5.1 串口初始化函数

CubeMX 自动生成
函数中的串口配置与 CubeMX 中的图形化配置一一对应

```c
void MX_USART1_UART_Init(void)
{
  huart1.Instance = USART1;
  huart1.Init.BaudRate = 9600;//波特率
  huart1.Init.WordLength = UART_WORDLENGTH_8B;//字节长度
  huart1.Init.StopBits = UART_STOPBITS_1;//停止位
  huart1.Init.Parity = UART_PARITY_NONE;//校验
  huart1.Init.Mode = UART_MODE_TX_RX;//接收发送模式
  huart1.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart1.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart1) != HAL_OK)
  {
    Error_Handler();
  }
}
```


### 6.5.2 串口接收与发送函数(阻塞式)

串口接收函数: HAL_UART_Receive

```c
/**
  * @brief  以阻塞模式接收指定数量的数据
  * @param  huart：指向UART_HandleTypeDef结构的指针，该结构包含指定UART模块的配置信息
  * @param  pData：数据缓冲区指针，即你读到的数据存哪
  * @param  Size：接收数据元素的数量
  * @param  Timeout：超时时间，即等待多久。若希望一直等待直到收到数据，传入HAL_MAX_DELAY
  * @retval HAL status：是否执行成功
  */
HAL_StatusTypeDef HAL_UART_Receive(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size, uint32_t Timeout)；
```

串口发送函数: HAL_UART_Transmit

```c
/**
  * @brief  以阻塞模式发送指定数量的数据
  * @param  huart：指向UART_HandleTypeDef结构的指针，该结构包含指定UART模块的配置信息
  * @param  pData：数据缓冲区指针，即你发送的数据在哪
  * @param  Size：发送数据元素的数量
  * @param  Timeout：超时时间，即等待多久。若希望一直等待直到发送完成，传入HAL_MAX_DELAY
  * @retval HAL status：是否执行成功
  */
HAL_StatusTypeDef HAL_UART_Transmit(UART_HandleTypeDef *huart, const uint8_t *pData, uint16_t Size, uint32_t Timeout)；
```

示例: 复读机

```c
int main(void)
{
  HAL_Init();
  SystemClock_Config();
  MX_GPIO_Init();
  MX_USART1_UART_Init();
  uint8_t RecieveBuf[2];
  while (1)
  {
        HAL_UART_Receive(&huart1,RecieveBuf,2, HAL_MAX_DELAY);//等待接收两个字符
        HAL_UART_Transmit(&huart1,RecieveBuf,2, 100);//发送接收到的两个字符
  }
}
```


### 6.5.3 串口中断接收与发送函数(中断式)

(1) 这两个函数前三个传入参数与普通发送和接收函数一样
区别在于不存在 Timeout 参数

(2) 同时
HAL_UART_Receive_IT 不会阻塞
当中断接收开启
程序会继续执行
所以不能在其运行后立即分析数据
也不要在 while 循环中调用该接收函数
需要在中断回调函数中执行

```c
HAL_StatusTypeDef HAL_UART_Receive_IT(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)；

HAL_StatusTypeDef HAL_UART_Transmit_IT(UART_HandleTypeDef *huart, const uint8_t *pData, uint16_t Size)；
```


### 6.5.4 串口中断回调函数

(1) 下面两个中断回调函数
顾名思义
就是在串口发送或者接收完成之后调用的函数
使用它来进行数据处理可以避免中断还未执行完
就又被开启等现象
实际使用中还有诸如 HalfCpltCallback 等回调函数
可以自行查阅补充

```c
__weak void HAL_UART_TxCpltCallback(UART_HandleTypeDef *huart)

__weak void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
```

(2) 实际使用中可以通过 stm32fxxx_it.c 中的
HAL_UART_IRQHandler(&huart1) 函数去索引到这两个函数的位置
可以看到在该文件中
这两个函数是弱定义(__weak)的
这表明我们可以在工程其他地方重新定义这两个函数
来实现自己所需要的回调功能


### 6.5.5 空闲中断

阻塞式

```c
HAL_UARTEx_ReceiveToIdle(&huart1, buffer, sizeof(buffer), &rx_len, HAL_MAX_DELAY);
```

中断式

```c
//启动接收
HAL_UARTEx_ReceiveToIdle_IT(&huart1, buffer, sizeof(buffer));

// 回调函数实现
void HAL_UARTEx_RxEventCallback(UART_HandleTypeDef *huart, uint16_t Size) {
    if (huart->Instance == USART1) {
        process_data(buffer, Size);  // 处理数据
        HAL_UARTEx_ReceiveToIdle_IT(huart, buffer, sizeof(buffer));  // 重启接收
    }
}
```

[点拨] HAL_UARTEx_ReceiveToIdle_IT 只是配好缓冲区 + 开 IDLE 中断
真正的 IDLE 标志位在 USARTx_IRQHandler 里由 HAL 清除
回调里必须像上面那样重新调用一次 ReceiveToIdle_IT
否则只能收到第一帧
用 CubeMX 时要确认 USART1 global interrupt 已勾选
若改用 DMA 版本(HAL_UARTEx_ReceiveToIdle_DMA)
还需在 DMA 配置里把对应 Stream 设为 Circular
或每次回调后重启
才能持续收不定长数据


### 6.5.6 串口重定向(串口打印)

(1) 为方便查看和调试
可以使用与 printf 相近的格式去打印数据

```c
#define TX_BUF_SIZE 512
uint8_t send_buf[TX_BUF_SIZE];

void usart_printf(const char* format, ...)
{
    va_list args;
    uint32_t length;
    va_start(args, format);
    length = vsnprintf((char*)send_buf, TX_BUF_SIZE, (const char*)format, args);
    va_end(args);

    HAL_UART_Transmit(&huart8, (uint8_t *)send_buf, length, 0xFFFF);
    //最后一行决定使用阻塞式/中断式/DMA中断式通信
}
```

(2) 注意: 如果使用非阻塞式 UART
两次调用可能会造成打印时数据覆盖
所以需要等待第一次 DMA 发送完成再调用第二次
这会使代码复杂

(3) Keil 串口重定向
1. 开启 Use MicroLIB 选项
2. 重写 fputc 与 fgetc 函数
可以写在 main.c 里面
记得引用 stdio.h 头文件

```c
/**
  * 函数功能: 重定向c库函数printf到DEBUG_USARTx
  * 输入参数: 无
  * 返 回 值: 无
  * 说    明：无
  */
int fputc(int ch, FILE *f)
{
  HAL_UART_Transmit(&huart1, (uint8_t *)&ch, 1, 0xffff);
  return ch;
}

/**
  * 函数功能: 重定向c库函数getchar,scanf到DEBUG_USARTx
  * 输入参数: 无
  * 返 回 值: 无
  * 说    明：无
  */
int fgetc(FILE *f)
{
  uint8_t ch = 0;
  HAL_UART_Receive(&huart1, &ch, 1, 0xffff);
  return ch;
}
```

然后就可以在代码中使用 printf 了
此函数就会通过串口 1 打印所需的内容
当然
上述代码中的 HAL_UART_Transmit 也可以改为 HAL_UART_Transmit_IT
或者 HAL_UART_Transmit_DMA
下节课会讲
可以接收不定长数据

(4) 示例

```c
int main(void)
{//生成的一系列初始化、省略
    while (1)
      {
            printf("hello usart \n");
      }
}
```

[点拨] Keil 通过勾选 Use MicroLIB 让 fputc 生效
CLion + GCC(MinGW/arm-none-eabi) 使用的是 newlib
编译器不会调用 fputc
需要改写 __io_putchar 或 _write
并用 setvbuf(stdout, NULL, _IONBF, 0) 关掉 stdout 缓冲
否则 printf 的内容会留在缓冲区里不输出


## 6.6 实践例程


### 6.6.1 设计思路

非常简单, 我们写一个复读机


### 6.6.2 设计流程


#### 6.6.2.1 CubeMX 配置

左侧边栏 Connectivity 中
选择 USART1
设置 MODE 为 Asynchronous(异步通信)
基础参数设置:
1. Baud Rate(波特率) 单位为 bit/s
即单位时间内传输码元的个数
接收端与发送端必须一致
此处选择 115200 bit/s
2. 其余参数一般保持默认
即传输数据长度为 8 Bit
奇偶检验无, 停止位 1
接收和发送都使能
中断设置: 在 NVIC Settings 中打开中断

[点拨] NVIC Settings 页里要勾的是
USART1 global interrupt 的 Enabled 复选框
只把 MODE 改成 Asynchronous 并不会自动开中断
勾选后生成的代码里 HAL_NVIC_EnableIRQ(USART1_IRQn) 才会出现
中断式收发才能正常工作


#### 6.6.2.2 硬件连接

在引脚图中找到开启串口的对应 TX, RX 引脚
C8T6 三个串口对应引脚如下
本实验选用串口 1

表6-1 USART 引脚分配

| 串口 | TX | RX |
|---|---|---|
| USART1 | PA9 | PA10 |
| USART2 | PA2 | PA3 |
| USART3 | PB10 | PB11 |

在与其他设备连接时
注意接线应该为: TX 接 RX, RX 接 TX
本实验连接 USB 转 TTL 模块


#### 6.6.2.3 代码实现

轮询(阻塞式)

```c
int main(void)
{
  HAL_Init();
  SystemClock_Config();
  MX_GPIO_Init();
  MX_USART1_UART_Init();
  uint8_t RecieveBuf[2];
  while (1)
  {
        HAL_UART_Receive(&huart1,RecieveBuf,2, HAL_MAX_DELAY);//等待接收两个字符
        HAL_UART_Transmit(&huart1,RecieveBuf,2, 100);//发送接收到的两个字符
  }
}
```

中断

```c
uint8_t RecieveBuf[2];
void SystemClock_Config(void);
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart){
     if(huart == &huart1){
         //之后可能会进行一些很复杂的解算操作……
         HAL_UART_Transmit_IT(&huart1,RecieveBuf,2);
         //再次开启接收
         HAL_UART_Receive_IT(&huart1,RecieveBuf,2);
     }
 }

int main(void)
{//生成的一系列初始化
  HAL_Init();
  SystemClock_Config();
  MX_GPIO_Init();
  MX_USART1_UART_Init();
  //开始接收
  HAL_UART_Receive_IT(&huart1,RecieveBuf,2);
  while (1)
  {
    //假装我在主函数处理一些很复杂的东西
  }
}
```


### 6.6.3 结果展示


## 6.7 拓展训练

------

# 7 DMA


## 7.1 简介

DMA (Direct Memory Access) 即直接存储器访问
借助内部的控制器实现内存和外设之间的数据传输

(1) 转移数据 (尤其是转移大量数据) 时可以不需要 CPU 参与
(2) 例如希望把外设 A 的数据拷贝到外设 B
只要给两种外设提供一条数据通路
直接让数据由 A 拷贝到 B, 不经过 CPU 的处理
DMA 就是基于以上设想设计的


## 7.2 基本原理


### 7.2.1 DMA 请求

(1) 外设要想通过 DMA 传输数据
必须先给 DMA 控制器发送 DMA 请求
(2) DMA 收到请求信号之后
控制器会给外设一个应答信号
当外设应答, 且 DMA 控制器收到应答信号之后
就启动 DMA 传输, 直到传输完毕
(3) DMA 有 DMA1 和 DMA2 两个控制器
DMA1 有 7 个通道, DMA2 有 5 个通道
不同的 DMA 控制器的通道对应着不同的外设请求
这决定了软件编程上该怎么设置
具体见 DMA 请求映像表 (部分芯片存在差异)


### 7.2.2 DMA 通道与仲裁

当发生多个 DMA 通道请求时
就存在响应处理的先后顺序问题
这由仲裁器管理
仲裁器管理 DMA 通道请求分为两个阶段

(1) 软件阶段: 可以在 `DMA_CCRx` 寄存器中设置
共 4 个等级: 非常高, 高, 中和低
(2) 硬件阶段: 如果两个或以上 DMA 通道请求设置的优先级一样
则优先级取决于通道编号
编号越低优先权越高
比如通道 0 高于通道 1
此外 DMA1 控制器拥有高于 DMA2 控制器的优先级


### 7.2.3 DMA 模式

(1) 普通模式 (Normal)
传输结束后 (即要传输数据的数量达到零)
将不再产生 DMA 操作
若开始新的 DMA 传输
需在关闭 DMA 通道的情况下
手动重新启动 DMA 传输
(2) 循环模式 (Circular)
可用于处理环形缓冲区和连续数据流
激活循环模式后
每轮传输结束时
要传输的数据数量将自动用设置的初始值重新加载
并继续响应 DMA 请求

[点拨] 在 STM32CubeMX 的 DMA Settings 页签里
每个请求都有 Direction (外设到内存 / 内存到外设)
Mode (Normal / Circular)
Data Width (Peripheral / Memory 各自的 Byte, Half Word, Word)
与 Increment Address 四项
串口收发一般用 Byte 宽度
Memory 侧开地址自增
Direction 分别为 Peripheral To Memory / Memory To Peripheral
做连续采集 (如 ADC, 串口不定长接收) 才选 Circular
否则选 Normal 并在每次传输前重新调用一次启动函数


## 7.3 常用函数 (以串口 DMA 为例)


### 7.3.1 串口 DMA 发送与接收

```c
/**
  * @brief  以DMA模式发送一定数量的数据。
  * @param  huart 指向UART_HandleTypeDef结构体的指针
  * @param  pData 指向数据缓冲区的指针。
  * @param  Size  要发送的数据元素数量。
  * @retval HAL状态
  */
HAL_StatusTypeDef HAL_UART_Transmit_DMA(UART_HandleTypeDef *huart, const uint8_t *pData, uint16_t Size)
```

```c
/**
  * @brief  以DMA模式接收一定数量的数据。
  * @param  huart 指向UART_HandleTypeDef结构体的指针
  * @param  pData 指向数据缓冲区的指针。
  * @param  Size  要接收的数据元素数量。
  * @retval HAL状态
  */
HAL_StatusTypeDef HAL_UART_Receive_DMA(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
```


### 7.3.2 空闲中断 + DMA

```c
//启动DMA接收
HAL_UARTEx_ReceiveToIdle_DMA(&huart1, buffer, sizeof(buffer));

// 回调函数中处理数据
void HAL_UARTEx_RxEventCallback(UART_HandleTypeDef *huart, uint16_t Size) {
    if (huart->RxState == HAL_UART_STATE_READY) {  // 确保是空闲中断触发
        process_data(buffer, Size);
    }
}
```

[点拨] `HAL_UARTEx_ReceiveToIdle_DMA` 已经把
DMA 接收 + 串口空闲 (IDLE) 中断封装在一起了
不需要像标准库那样手动开 `__HAL_UART_ENABLE_IT(&huart1, UART_IT_IDLE)`
它回调的是 `HAL_UARTEx_RxEventCallback`
注意带 `Ex`, 与普通 `HAL_UART_RxCpltCallback` 不是同一个
参数 `Size` 就是本帧实际收到的字节数
若要在每帧后继续接收
需在回调里再次调用一次 `HAL_UARTEx_ReceiveToIdle_DMA`


### 7.3.3 串口重定向

(1) 目的: 方便查看和调试
可以使用与 printf 相近的格式去打印数据
(2) 实现函数

```cpp
#define TX_BUF_SIZE 512
uint8_t send_buf[TX_BUF_SIZE];

void usart_printf(const char* format, ...)
{
    va_list args;
    uint32_t length;
    va_start(args, format);
    length = vsnprintf((char*)send_buf, TX_BUF_SIZE, (const char*)format, args);
    va_end(args);

    //HAL_UART_Transmit(&huart8, (uint8_t *)send_buf, length, 0xFFFF);
    HAL_UART_Transmit_DMA(&huart1, (uint8_t*)send_buf, length);
}
```

最后一行其实就决定了用哪个串口
以什么样的形式 (中断, 轮询, DMA) 去传输这个数据


## 7.4 实践例程


### 7.4.1 设计思路

通过重定向的 DMA 发送函数
在 vofa 中打印 sin 与 cos 曲线

(1) 实现 DMA 的初始化
(2) 实现重定向
(3) 写出 sin 与 cos 曲线


### 7.4.2 设计流程

在上个实验串口配置的基础上
选中 DMA Settings
为接收和发送均开启 DMA 通道
可以修改 Channel 与 Priority
来改变它们的优先级


#### 7.4.2.1 主要代码实现

```c
int times = 0;
int main(void)
{
  HAL_Init();
  SystemClock_Config();
  MX_GPIO_Init();
  MX_USART1_UART_Init();
  uint8_t RecieveBuf[2];
    while (1)
    {
    if(times>200)times=0;
    else times++;
    usart_printf("%.2f,%.2f\r\n",coss[times],sins[times]);//用的串口2
    HAL_Delay(50);
    }
}
```

[点拨] DMA 传输的源缓冲区 (这里是 `send_buf`) 在传输完成前不能被改写
否则发出去的是被覆盖后的数据
连续调用 `usart_printf` 时两次之间应确认上一次 DMA 已结束
查询 `huart1.gState` 或等 `HAL_UART_TxCpltCallback` 回调
必要时把发送长度和缓冲区做成双缓冲
另外在 Cortex-M4/M7 (如 F4/F7/H7) 上
若开启了 D-Cache
DMA 读写的内存区要做对齐
并手动调用 `SCB_CleanDCache_by_Addr` 与
`SCB_InvalidateDCache_by_Addr`
否则 CPU 看到的是 Cache 里的旧数据


### 7.4.3 结果展示

在 vofa 中可观察到 sin 与 cos 两条曲线


### 7.4.4 程序代码


## 7.5 拓展训练

使用定时器 + 串口, 在 vofa+ 中绘制指定频率的正弦波

------

# 8 ADC(招新培训忽略)


## 8.1 简介

(1) 模数转换器 ADC 是把模拟信号转换为数字信号的电子器件
ADC 即 Analog-to-Digital Converter
(2) 现实世界中的许多物理量都是连续变化的模拟信号
温度, 电压, 声音等都属于此类
数字信号便于处理, 存储和传输
ADC 是两者之间的桥梁
ADC 也是现代电子系统的核心模块之一
(3) 在嵌入式系统中
ADC 常被集成在 MCU 内部
用于采集外部传感器信号
实现对环境的感知和响应
(4) 不同类型的 ADC 精度, 速度和功耗特性不同
需要根据实际应用进行选型


## 8.2 基本原理

ADC 将模拟正弦波转换为二进制数字
以完成数据采集


### 8.2.1 ADC 的工作过程

(1) 采样(Sampling)
以固定的时间间隔对模拟信号进行截取
得到一个快照
采样频率需要至少是信号最高频率的两倍
即奈奎斯特定理
通常最好为 4-10 倍
否则可能发生混叠
(2) 保持(Hold)
在 ADC 进行转换时
为防止输入信号变化
采样后的值会被保持一段时间
以确保转换精度
(3) 量化(Quantization)
将模拟电压映射到有限个离散电平
比如 12 位 ADC 将电压划分为 2¹² = 4096 个等级
(4) 编码(Encoding)
将量化后的电平值转换为对应的二进制数字
以供数字电路使用


### 8.2.2 ADC 常见架构及结构差异


#### 8.2.2.1 逐次逼近型(SAR ADC)

SAR 即 Successive Approximation Register
SAR ADC 速度适中, 结构较简单
广泛用于通用 MCU 中

(1) 工作原理
通过一个逐步逼近的比较过程
从高位到低位依次判断输入电压与内部 DAC 输出的比较结果
从而逐步锁定每一位的数值
(2) 典型结构
包括采样保持电路, 比较器, 内部 DAC 以及 SAR 控制逻辑
(3) 优点
功耗低, 转换速度较快
可达几百 kHz 甚至 MHz
适用于大多数中等速率, 高精度需求的场合


#### 8.2.2.2 Σ-Δ 型(Sigma-Delta ADC)

Sigma-Delta ADC 通过过采样和噪声整形技术实现高分辨率
常见于音频处理, 精密测量等应用

(1) 工作原理
通过高频率对信号进行采样
将模拟误差积分反馈
并使用低通滤波器对输出进行数字滤波
从而提高分辨率
(2) 典型结构
包括积分器, 比较器, 1 位 DAC 反馈环路和数字低通滤波器
(3) 优点
分辨率高, 常见为 16 位及以上
线性度好
适合低速, 高精度的应用场景


### 8.2.3 ADC 的关键性能指标

(1) 分辨率
指 ADC 输出的位数
决定其能区分的电平数量
例如 12 位 ADC 有 4096 个离散电平
其计算公式为

$LSB = \frac{FSR}{2^N}$

(2) 采样率
单位时间内进行采样并完成转换的次数
单位为 SPS, Samples Per Second
(3) 精度
表示 ADC 转换值与真实输入值之间的误差
受参考电压, 噪声, 非线性等因素影响
(4) 有效位数
综合考虑噪声与误差后 ADC 真实可用的分辨率
通常 12 位 ADC 的有效位数可能仅有 10 位


## 8.3 硬件设计


### 8.3.1 常见外围电路设计


#### 8.3.1.1 滤波电路

目的: 滤除输入时的高频噪声
降低采样抖动
提高转换精度
抗混叠

参考设计:

(1) 无源缓冲滤波电路
设计建议:
1. 截止频率 $f_c = \frac{1}{2 \pi R_f C_f}$
一般设置为高于信号带宽
低于噪声带宽
2. 一般不选取太大的 $R_f$
否则会影响 ADC 采样精度
与阻抗匹配相关
(2) 有源抗混叠滤波电路
设计建议:
1. 运放选型要关注带宽, 压摆率, 低噪和轨到轨输出特性
2. 输入处可使用高精度低温漂的电阻进行分压
或使用更精细的分压测量电路进行预处理
增大测量范围

[点拨] 采样保持电容需要由外部信号在采样窗口内充到稳定电平
源阻抗越大所需采样时间越长
若把上面的 $R_f$ 取到几十 kΩ 以上
务必在 CubeMX 的 ADC 通道参数里把 Sampling Time 调大
如 239.5 Cycles
否则读数会明显偏低
且随通道切换漂移


#### 8.3.1.2 保护电路

目的: 限制输入端的浪涌电流和输入电压
保证输入 ADC 引脚的信号不会损害到芯片

参考设计:

设计建议:
(1) 限流电阻 $R_{lim}$ 一般不选取太大
百欧级即可
(2) 可用普通小信号二极管, 如 1N4148
或集成钳位, 如 TVS


### 8.3.2 STM32CubeMX 配置

[点拨] CubeMX 中 ADC 有三个参数相互约束
即 Continuous Conversion Mode
Scan Conversion Mode 与 Number of Conversions
只有开启 Scan Conversion Mode
才能配置多通道与 Number of Conversions
此时 Number of Conversions 必须等于已启用通道数
单通道时将其设为 1
Continuous Conversion Mode 为 Enable 时
一轮转换结束后自动重新启动
不必在代码里重复调用启动函数
若同时开了 Scan
则按规则组顺序循环扫描


## 8.4 软件设计


### 8.4.1 轮询模式转换

轮询方式是 STM32 外设最基础的驱动方式
通过简单的轮询模式转换
可以更轻松地理解 STM32 驱动 ADC 的逻辑和方法
下列是一些轮询模式转换相关的函数

```c
/**
  * @brief  启动 ADC 转换（非中断、非 DMA 模式）
  * @param  hadc：指向 ADC_HandleTypeDef 的指针
  * @retval HAL status：是否成功启动
  */
HAL_StatusTypeDef HAL_ADC_Start(ADC_HandleTypeDef *hadc);

/**
  * @brief  阻塞等待 ADC 转换完成
  * @param  hadc：指向 ADC_HandleTypeDef 的指针
  * @param  Timeout：超时时间（单位为毫秒）。可传入 HAL_MAX_DELAY 以无限等待
  * @retval HAL status：是否成功完成转换
  */
HAL_StatusTypeDef HAL_ADC_PollForConversion(ADC_HandleTypeDef *hadc, uint32_t Timeout);

/**
  * @brief  读取 ADC 转换结果
  * @param  hadc：指向 ADC_HandleTypeDef 的指针
  * @retval ADC 数值（无符号整型），其有效位数由 ADC 初始化时的分辨率决定
  */
uint32_t HAL_ADC_GetValue(ADC_HandleTypeDef *hadc);

/**
  * @brief  停止 ADC 转换（非中断、非 DMA 模式）
  * @param  hadc：指向 ADC_HandleTypeDef 的指针
  * @retval HAL status：是否成功停止
  */
HAL_StatusTypeDef HAL_ADC_Stop(ADC_HandleTypeDef *hadc);
```

(1) 单次转换的流程为
启动 ADC -> 等待转换完成 -> 获取 ADC 转换结果
一般而言不需要停止 ADC 转换
故 `HAL_ADC_Stop` 可以不使用
(2) 若在 CubeMX 中将 ADC 配置中的
Continuous Conversion Mode 设为 Disable
则可在 main 函数中的 while 循环下加入这一流程
在获取到转换结果后使用计算公式得到实际物理数值
并配合串口向电脑或其他上位机发送结果
这样便能实现 ADC 连续转换功能
(3) 除了每次都对 ADC 进行启动, 阻塞以外
还可以将 Continuous Conversion Mode 设置为 Enable
则相当于让程序在每次获取完数值后定时再次自动启动
无需使用函数手动启动
与上面的情况相比
只需在代码中将启动 ADC 与等待转换结束的函数放在循环外部
同样可以实现 ADC 连续转换功能

[点拨] `HAL_ADC_GetValue` 返回的是原始码值 0~4095, 12 位
换算电压用 `V = raw * VREF+ / 4096`
其中 4096 即 $2^{12}$, 不是 4095
注意 CubeMX 里 VREF+ 默认接到 VDDA
若板子用了外部基准
换算时要用外部基准电压
否则整段读数会按比例偏大或偏小


### 8.4.2 中断模式转换

与轮询方式相比
中断方式具有更高的效率
主循环可以处理更多其他任务
而无需等待 ADC 转换完成
是一种更常用于实际工程应用中的采样驱动方式
下列是一些中断模式转换相关的函数

```c
/**
  * @brief  启动 ADC 并启用中断模式进行转换
  * @param  hadc：指向 ADC_HandleTypeDef 的指针
  * @retval HAL status：是否成功启动
  * @note   转换完成后将自动触发中断，调用用户重写的回调函数 HAL_ADC_ConvCpltCallback()
  */
HAL_StatusTypeDef HAL_ADC_Start_IT(ADC_HandleTypeDef *hadc);

/**
  * @brief  用户自定义的 ADC 转换完成中断回调函数
  * @param  hadc：指向 ADC_HandleTypeDef 的指针
  * @retval 无
  * @note   该函数为弱定义（`__weak`），用户应在 `user_code` 区域内重写它以处理采样数据
  */
void HAL_ADC_ConvCpltCallback(ADC_HandleTypeDef* hadc);

/**
  * @brief  停止 ADC 中断模式转换
  * @param  hadc：指向 ADC_HandleTypeDef 的指针
  * @retval HAL status：是否成功停止
  */
HAL_StatusTypeDef HAL_ADC_Stop_IT(ADC_HandleTypeDef *hadc);
```

(1) 中断驱动 ADC 的方式不再需要在主函数中频繁地轮询等待转换完成
而是通过配置 ADC 中断模式
使得每当一次转换完成后
自动触发中断并调用用户定义的回调函数
从而异步地获取转换结果
(2) 通常流程为
启动 ADC -> 等待中断触发 -> 在回调函数中读取转换结果
(3) 由于 ADC 会在完成一次转换后自动进入等待状态
因此如果需要连续转换
可将 Continuous Conversion Mode 设置为 Enable
这样在中断触发后 ADC 会自动启动下一轮转换
无需手动重新调用启动函数


### 8.4.3 DMA 模式转换(电赛培训忽略)


## 8.5 实验例程


### 8.5.1 轮询模式转换


#### 8.5.1.1 设计思路(CubeMX 配置)

在串口实验配置的基础上
点击 Analog - ADC1
开启任意通道
这里以选择 IN5 为例
将 Continuous Conversion Mode 设置为 Enable
即完成轮询模式下的配置


#### 8.5.1.2 程序代码

在 main.c 文件中
进行全部代码的修改
如图中注释


#### 8.5.1.3 结果展示


### 8.5.2 中断模式转换


#### 8.5.2.1 设计思路(CubeMX 配置)

在 ADC 轮询实验配置的基础上
点击 System Core - NVIC
将 ADC1 and ADC2 global interrupts 勾选
即可完成配置


#### 8.5.2.2 程序代码

(1) 和轮询不一样的是
ADC 中断的操作指令将全部在 ADC 中断的回调函数中执行
而并非 main 函数中
故修改在 adc.c 文件中
保证驱动函数存在相应文件下
增强项目可读性
(2) 如下 adc.c 文件中全部代码的修改
如图中注释
(3) 由于这里使用了封装在 usart.c 文件中的串口打印函数
这里还需要在顶部加入

```c
#include "usart.h"
```

(4) 另外这里的 HAL_ADC_ConvCpltCallback 函数同文档介绍
是一个被事先弱定义了的函数
这里直接进行重新定义即可
无需在 adc.h 文件中再次声明
(5) 如下 main.c 文件中全部代码的修改
如图中注释


#### 8.5.2.3 结果展示


## 8.6 拓展训练

------

# 9 定时器


## 9.1 简介


### 9.1.1 时钟树

时钟信号
时钟信号指边沿触发器的控制端
该控制端接入方波信号
当控制端出现一个由低电平变为高电平的上升沿时
输出端变成输入端的电平

时钟树
详细讲解见
[STM32 超清晰 STM32 时钟树动画讲解_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1ph4y1e7Ey?spm_id_from=333.788.videopod.sections&vd_source=42a2d38b0cfe87572ea3d876193fbaff)


### 9.1.2 定时器

定时器(TIM)是单片机内部的一种硬件模块
核心功能是精准计时和计数
核心组成部分包括计数器(CNT)
比较寄存器(CMP)
自动重装载寄存器(ARR)
此外还有预分频器(PSC)等其他部分
通过设置不同的时钟脉冲来源
不同的触发和计数方式
不同的输出方式
能够实现准确计时, 定时触发, 脉冲宽度捕获
PWM 宽度检测, PWM 输出, 检测外部脉冲等功能
在嵌入式设计中有广泛的应用

根据其能实现的功能的不同
STM32 片上的定时器主要分为
(1) 基本定时器
(2) 通用定时器
(3) 高级定时器

基本定时器为 TIM6, TIM7
通用定时器为 TIM2, TIM3, TIM4, TIM5
高级定时器为 TIM1, TIM8


## 9.2 基本原理


### 9.2.1 基本定时部分

计数器(CNT)
定时器最基本的部分为计数器(CNT)
即一个 16 bits 的边沿检测寄存器
每当有一个上升沿经过
寄存器的值便加 1

预分频器(PSC / Prescaler)
为了提升定时器的计时能力
在定时器前会有一个预分频器(PSC)
为输入的脉冲信号进行分频

自动重装载计数器(ARR / Counter Period (AutoReload Value))
为了使计数器重置的值更加灵活
引入了自动重装载计数器(ARR)
设定了计数器自动重装载的值
当计数器与 ARR 值相同时
便重置为 0
并触发更新中断

为增进理解
推荐观看
[STM32 第 16 集 动画告诉你, STM32 的定时器到底怎么回事_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV11u4y1A7gS?spm_id_from=333.788.videopod.sections&vd_source=42a2d38b0cfe87572ea3d876193fbaff)

[点拨] 定时时间如下式
两个 `+1` 最容易漏

$T=\dfrac{(PSC+1)\times(ARR+1)}{f_{TIMx}}$

CubeMX 里 PSC 填 71 表示 72 分频
ARR 填 999 表示计 1000 个数
另外, TIM1/TIM8 挂 APB2
TIM2~TIM5 挂 APB1
TIM6/TIM7 挂 APB1
CubeMX 的 Clock Configuration 页里
APB1/APB2 预分频不为 1 时
定时器时钟会自动 ×2
所以主频 72 MHz 下
APB1 定时器时钟仍是 72 MHz
而不是 36 MHz


### 9.2.2 定时器通道

一个定时器通常有多个通道
这些通道既可作为外部时钟信号的输入
也可作为定时器内部信号的输出

以 STM32F103 举例
其 TIM1 定时器为高级定时器
共有四个通道
这些通道可作为输入通道
也可作为输出通道


### 9.2.3 外部时钟

外部时钟模式
顾名思义
即将外部信号作为定时器的时钟信号或者控制信号

外部触发源共有

(1) 外部专用引脚(ETR)
一个独立于四个时钟通道的引脚
通常直接连接定时器的外部触发输入
(2) 内部定时器同步信号(ITRx)
来自其他定时器的 TRGO(触发输出)信号
用于级联定时器
(3) 输入捕获通道(TI1/TI2 等)
由 TI1FP1 等的信号边沿触发
常用于 PWM 输入或编码器输入模式
(4) 外部中断引脚
通过复用功能选择
将 GPIO 映射为触发源

从模式(Slave Mode)
让此定时器受另一个定时器或外部时钟源控制

(1) 外部时钟模式 1
将外部信号作为定时器时钟源
进行边沿计数
(2) 重置模式
外部信号边沿令计数器重置
(3) 门模式
外部信号高电平时计时器才进行计数
(4) 触发模式
外部信号边沿令计数器开始计数
常与单脉冲模式共用

触发源(Trigger Source)
在上述从模式下触发器选择的信号源
可见信号源有内部定时器信号, 外部专用引脚和 TI1 通道信号
其中 ED 为双边沿信号

时钟源(Clock Source)
即计数器边沿计数的信号

(1) 内部时钟信号(Internal Clock)
与外部时钟信号区分开
这里表示的是 MCU 的主频信号
(2) 外部时钟模式 2
将外部信号(这里只有 ETR)作为定时器时钟源
进行边沿计数


### 9.2.4 输入捕获模式

为了避免例如中断函数调用等导致的延时
在通用定时器的时钟通道中
设置了捕获寄存器
实现在边沿出现时立刻记录计数器的值

间接模式指的是信号通道与寄存器的通道不符

设置 Channel1 为上升沿检测
Channel2 为下降沿检测
即可实现记录高电平宽度的持续时间


### 9.2.5 编码器模式

编码器
是一种在旋转时产生方波输出的元件
根据方波的相位差和频率即可知道编码器旋转的方向和速度

编码器可作为交互元件
更可以用于电机中
向 MCU 传输电机旋转方向和速度等信息

在 STM32 中
芯片已经预备好了通过定时器接收编码器的通道
选择 Encoder Mode 后
定时器的 CHANNEL1, CHANNEL2 即可实现对编码器信号的计数

[点拨] Encoder Mode 会同时占用该定时器的 CH1/CH2 两个引脚
如 TIM1_CH1/CH2 对应 PA8/PA9
此时这两个引脚不能再作 PWM 输出或普通 GPIO 用
TIM1 的 CH1 还与 TIM1_CH1N, TIM1_ETR 等复用重叠
改配置前先在 CubeMX 的 Pinout 视图里确认引脚
是否与其它外设(如 USART1, SPI1)冲突


### 9.2.6 PWM 输出

PWM 是一种占空比可调的方波
通过设置定时器的 CMP 和 ARR
可很方便地实现 PWM 波的输出
基本上每一个时钟通道都可以输出 PWM 波

在 CubeMX 中选择 PWM Generation 后
可以看到如下的设置界面

(1) Mode(PWM 输出模式)
mode1 时当 CNT 的值小于 CMP 时
引脚输出高电平
而当 CNT 的值大于 CMP 时
引脚输出低电平
mode2 则相反
(2) Pulse
即比较寄存器的值
定时器 PSC, CMP, ARR 的值确定了 PWM 波的频率和占空比
(3) Fast Mode
PWM 频率较高时可使用
(4) CH Polarity(通道极性)
调整后极性翻转相当于一个与门

一般来说
除了设置寄存器的值
其他设置保持不变即可

PWM 的频率和占空比有如下公式

$f_{PWM}=\dfrac{f_{clock}}{预分频器 PSC\times 自动重装载寄存器 ARR}$

$Duty=\dfrac{比较寄存器 CMP}{自动重装载寄存器 ARR}$

在实际工程中
通过调节 PWM 的占空比
能实现对 LED 亮度, 电机转速, 数模转换等功能

[点拨] 在 CubeMX 的 TIMx 配置里
先把某个 Channel 的 Mode 选成 `PWM Generation CHx`
右下角才会出现 Pulse, Fast Mode, CH Polarity 这几项
同一通道若选成 `Input Capture` 或 `Encoder`
界面换成对应的捕获/编码器参数页
公式里的 PSC 与 ARR 是寄存器值
实际分频/计数值还要 +1
注意与 HAL 里写入的值对齐


## 9.3 常用函数


### 9.3.1 定时器初始化

CubeMX 工具能帮我们自动生成以下代码

```c
MX_TIM1_Init();
MX_TIM2_Init();
MX_TIM3_Init();
MX_TIM4_Init();
```

但这些只是定时器功能的初始化
具体功能开始工作还需要我们手写函数开启


### 9.3.2 定时器功能开启

主要的开启函数有

```c
//仅实现开启
HAL_StatusTypeDef HAL_TIM_Base_Start(TIM_HandleTypeDef *htim);
//开启定时器和中断
HAL_StatusTypeDef HAL_TIM_Base_Start_IT(TIM_HandleTypeDef *htim);
//开启定时器和DMA
HAL_StatusTypeDef HAL_TIM_Base_Start_DMA(TIM_HandleTypeDef *htim, const uint32_t *pData, uint16_t Length);
//当然还会有对应的stop函数,此处略去

//PWM开启
HAL_StatusTypeDef HAL_TIM_PWM_Start(TIM_HandleTypeDef *htim, uint32_t Channel);
HAL_StatusTypeDef HAL_TIM_PWM_Start_IT(TIM_HandleTypeDef *htim, uint32_t Channel);

//输入捕获 Input Capture
HAL_StatusTypeDef HAL_TIM_IC_Start(TIM_HandleTypeDef *htim, uint32_t Channel);
HAL_StatusTypeDef HAL_TIM_IC_Start_IT(TIM_HandleTypeDef *htim, uint32_t Channel);

//编码器Encoder
HAL_StatusTypeDef HAL_TIM_Encoder_Start(TIM_HandleTypeDef *htim, uint32_t Channel);
HAL_StatusTypeDef HAL_TIM_Encoder_Start_IT(TIM_HandleTypeDef *htim, uint32_t Channel);
```

只有用 `HAL_TIM_Base_Start_IT` 等函数启动定时器时
才能让定时器每次在自动重装载值时触发更新中断


### 9.3.3 定时器中断函数

如果想实现每隔某段时间进行某项任务
则可利用中断函数实现
即需要重写中断回调函数

```c
//计数周期完成中断
__weak void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim);
//计数周期过半中断
__weak void HAL_TIM_PeriodElapsedHalfCpltCallback(TIM_HandleTypeDef *htim);
//输入捕获中断
__weak void HAL_TIM_IC_CaptureCallback(TIM_HandleTypeDef *htim);
/*
这些函数前的 __weak 表示在此的定义是弱定义, 我们可以在自己的文件中重新定义这些函数
*/

__HAL_TIM_GET_FLAG(__HANDLE__, __FLAG__);
__HAL_TIM_CLEAR_FLAG(__HANDLE__, __FLAG__);
/*
这些预定义函数能够查看中断标志位
*/
```

`__weak` 表示在此的定义是弱定义
可以在自己的文件中重新定义这些函数

ps: 找这些中断回调函数的路径为
`stm32f1xx_it.c` 中的 `TIM4_IRQHandler` 函数
再进入 `HAL_TIM_IRQHandler` 函数


### 9.3.4 查看并修改寄存器的值

```c
//设置预分频器的值
__HAL_TIM_SET_PRESCALER(__HANDLE__, __PRESC__);
//获取,设置计数器的值
__HAL_TIM_GET_COUNTER(__HANDLE__);
__HAL_TIM_SET_COUNTER(__HANDLE__, __COUNTER__);
//获取,设置自动重装载寄存器的值
__HAL_TIM_GET_AUTORELOAD(__HANDLE__);
__HAL_TIM_SET_AUTORELOAD(__HANDLE__, __AUTORELOAD__);
//获取.设置比较寄存器的值
__HAL_TIM_GET_COMPARE(__HANDLE__, __CHANNEL__)
__HAL_TIM_SET_COMPARE(__HANDLE__, __CHANNEL__, __COMPARE__)
```

通过这些函数
我们就能在代码运行过程中实现对触发频率, PWM 频率
以及 PWM 占空比的动态调整


## 9.4 实践例程

通过简单的设置和代码编写
实现通过转动编码器, 控制电机转速

这个实验需要用到

(1) TIM1: Encoder 模式
(2) TIM2: PWM 输出

实验步骤如下

(1) 选择高速外部时钟源
(2) 设置主频为 72 MHz
(3) 设置 TIM1
1. 选择 TIM1 为编码器模式
2. 在 TIM1 的具体设置中
将预分频器设置为 2 分频
将输入滤波(Input Filter)的值设为最大 15
(4) 设置 TIM2
因为电机需要两路 PWM 线输入
故打开两个 PWM 通道
记得选择时钟源为内部时钟
在 TIM2 的具体参数设置中
设置预分频器为 72-1
即 72 分频
自动重装载寄存器设置为 1000
即得到的 PWM 波频率为

$f=\dfrac{72MHz}{72\times 1000}=1kHz$

(5) 保存并生成代码
转到 CLion 中编写代码
1. 初始化代码中
此处通过两个 start 函数开启 TIM1 的编码器工作
和 TIM2 的 PWM 工作
然后设置 TIM1 的计数器初始值为 0
2. 循环代码中
首先通过 get 函数得到 htim1 的计数器值
即可得到编码器的旋转情况
然后过滤掉上下的无效值
最后把得到的数据放入 TIM2 通道一的比较寄存器中
修改占空比
(6) 这个实验比较简单
还有很多可以拓展的地方
比方说
反转编码器时
实现电机反转并也能调速
用定时器和中断函数实现每隔一段时间更新速度数据
使用自带编码器的电机
并将信号引入 MCU
实现测速, PID 滤波等功能

------

# 10 CAN 通信


## 10.1 简介

CAN (Controller Area Network) 是一种多主机串行通信协议
常用于汽车产业
在 RoboMaster 的机器人中
CAN 通信在主控与主控之间
以及主控与电机之间的数据交互中发挥重要作用


## 10.2 基本原理

整体可分为物理层和数据层


### 10.2.1 物理层

物理层规定了硬件电路的连接方式与设计规则
硬件电路通常包括 CAN 控制器 + CAN 收发器 + 差分总线
设计时需注意波特率与数据同步/异步传输等问题

(1) CAN 收发器

CAN 控制器 (即 STM32) 的 TX 与 RX 信号是单端逻辑电平
单端电平为 3.3V 与 0V
CAN 总线上的信号是差分电平
需要收发器进行电平转换, 信号驱动与隔离收发
常见的 CAN 收发器芯片有 TJA1044 (C 板) 与 TJA1050 (淘宝小模块)

(2) 差分总线

每个设备各两根线
CAN_H 接到一起, CAN_L 接到一起
终端接入 120Ω 的电阻
防止信号不稳定与响应速度变慢等问题

差分总线的电平分为显性 (Dominant) 和隐性 (Recessive)
分别对应逻辑 "0" 和 "1"
电压对应关系如下表

表10-1 CAN 差分电平

| 逻辑电平 | CAN_H | CAN_L | 电位差 diff |
|---|---|---|---|
| 显性 (逻辑 0) | 3.5V | 1.5V | 2V |
| 隐性 (逻辑 1) | 2.5V | 2.5V | 0V |

使用差分总线传输主要是为了提高信号传输的鲁棒性
并在一定程度上削减噪声与干扰的影响

1. 差分

差分信号使用两根等长, 等宽的导线 (称为差分对)
同时传输振幅相等, 相位完全相反的信号
接收设备并不关注单根线的绝对电压
而是比较两根线的瞬时电压差来识别信号逻辑状态

2. 波特率

指每秒钟在总线上传输的比特数, 单位是 bps
一对 CAN 总线上的设备需要统一波特率才能正常工作
否则无法正常通信
大疆官方的电机或电调设备 (GM6020, C610, C620) 均为 1 Mbps
则 STM32 主控也需要设置为 1 Mbps
在 STM32 中, 通过下列公式设置 CAN 波特率

$CAN 波特率 = \frac{CAN 时钟频率}{分频系数 \times \ Quantum 数} = \frac{f_{PCLK}}{Prescaler \times (1+BS1+BS2)}$

设置波特率时还有些行业规范 (内容较多, 此处不展开)
可参考在线工具辅助计算各参数
http://www.bittiming.can-wiki.info/


### 10.2.2 数据层

(1) 数据帧

CAN 通信协议的数据帧分为七个段
具体字段如下表

表10-2 CAN 数据帧字段

| 字段名称 | 位数 | 说明 |
|---|---|---|
| 起始位 (Start of Frame) | 1 位 | 总线空闲后开始传输的起始标志 |
| 仲裁字段 (Arbitration Field) | 12 位 | 包括 11 位 ID + 1 位 RTR 标志位 |
| 控制字段 (Control Field) | 6 位 | 包括 IDE (标识是否扩展帧), r0 (保留), DLC (数据长度) |
| 数据字段 (Data Field) | 0 ~ 64 位 | 实际要传输的数据 (0~8 字节) |
| CRC 校验字段 (CRC Field) | 15 + 1 位 | CRC 校验序列 + CRC 界定符 |
| ACK 字段 (ACK Field) | 2 位 | 接收节点发送确认 (ACK 槽 + ACK 界定符) |
| 结束位 (End of Frame) | 7 位 | 标志一帧数据结束 |

(2) 通信协议

大疆官方电机/电调的用户手册说明了使用 CAN 通信时需要注意配置的字段
以 GM6020 电机为例
CAN 通信是一种广播式的通信方式
其一帧信息可以被总线上多个设备接收
结合 STM32 驱动 CAN 的方法, 需配置的字段如下表

表10-3 GM6020 帧配置字段

| 字段名称 | 说明 |
|---|---|
| ID (标识符) | 设置为 0x1FF (接收) / 0x204+电机ID (反馈) |
| IDE (帧类型) | 设置为 CAN_ID_STD |
| RTR (帧格式) | 设置为 CAN_RTR_DATA |
| DLC (数据长度) | 设置为 0x08 (表示 8 个字节) |
| Data (数据) | uint8_t Data[8] |

发送和接收时, 每个数据 (如机械角度, 转速) 都占 2 个字节长度
所以发送时需将 uint16_t 的数据按位拆分为两个 uint8_t 的数据
而接收时需要将两个 uint8_t 的数据按位合并为一个 uint16_t 的数据


## 10.3 常用函数

```c
// 启动 CAN 外设（必须调用）
HAL_StatusTypeDef HAL_CAN_Start(CAN_HandleTypeDef *hcan);
/*
使能 CAN 控制器进入正常工作状态，开始收发数据。
*/

// 停止 CAN 外设
HAL_StatusTypeDef HAL_CAN_Stop(CAN_HandleTypeDef *hcan);
/*
禁用 CAN 控制器，停止收发。
*/

// 发送一帧 CAN 消息
HAL_StatusTypeDef HAL_CAN_AddTxMessage(CAN_HandleTypeDef *hcan,
                                       CAN_TxHeaderTypeDef *pHeader,
                                       uint8_t aData[],
                                       uint32_t *pTxMailbox);
/*
向指定邮箱写入消息。需设置好 ID、DLC、帧类型。aData 是最多 8 字节的有效数据。
*/

// 接收一帧 CAN 消息
HAL_StatusTypeDef HAL_CAN_GetRxMessage(CAN_HandleTypeDef *hcan,
                                       uint32_t RxFifo,
                                       CAN_RxHeaderTypeDef *pHeader,
                                       uint8_t aData[]);
/*
从 FIFO 中读取接收到的帧。FIFO 可选为 CAN_RX_FIFO0 或 FIFO1。数据将写入 aData 缓冲区。
*/

// 配置 CAN 接收过滤器
HAL_StatusTypeDef HAL_CAN_ConfigFilter(CAN_HandleTypeDef *hcan,
                                       CAN_FilterTypeDef *sFilterConfig);
/*
设置 ID 过滤规则。需在 HAL_CAN_Start() 前调用。可根据需要只接收某些 ID，提高效率。
*/

// 启用中断通知
HAL_StatusTypeDef HAL_CAN_ActivateNotification(CAN_HandleTypeDef *hcan,
                                               uint32_t ActiveITs);
/*
启用接收、错误等中断。ActiveITs 支持位或组合：CAN_IT_RX_FIFO0_MSG_PENDING、CAN_IT_ERROR 等。
*/

// 弱定义的 FIFO0 接收中断回调函数
__weak void HAL_CAN_RxFifo0MsgPendingCallback(CAN_HandleTypeDef *hcan)
/*
当 FIFO0 有新数据时由 HAL 自动调用。需在此函数中调用 HAL_CAN_GetRxMessage() 读取数据并处理。
*/
```


## 10.4 实验例程

通过 CAN 通信, 实现对 GM6020 电机的开环控制 (电压控制)
使用杜邦线连接 TJA1050 模块
CAN_TX 接 PA12, CAN_RX 接 PA11
+5V 接 VCC, GND 接 GND
STM32F103C8T6 中仅有一个 CAN 控制器
故在左侧栏中找到 Connectivity 下的 CAN
直接点击 Activated 使能即可


### 10.4.1 CubeMX 配置

(1) 波特率设置

在时钟树中设置 $f_{HCLK}$ 为 72 MHz
则 $f_{PCLK}$ 默认为 36 MHz
想要设置波特率为 1 Mbps
那么就需要 $Time \ Quantum 数 = 36$
也就是 $(1+BS1+BS2) \times Prescaler = 36$
使用工具辅助计算后可得
设置 $Prescaler = 2$, $BS1 = 15$, $BS2 = 2$
看到 Baud Rate 为 1 000 000 bit/s 后即表示设置完成

[点拨] STM32CubeMX 里这三项不在时钟树
而在 Connectivity → CAN → Parameter Settings
的 Bit Timings Parameters 分组内
分组包含 Prescaler, Time Quanta in Bit Segment 1
与 Time Quanta in Bit Segment 2
注意 BS1, BS2 填的是 "Time Quantum 个数"
公式里还要各加 1 才是真实段长
采样点由 $(1+BS1)/(1+BS1+BS2)$ 决定
1 Mbps 下一般落在 75%~87.5% 之间
若通信偶发错误帧可优先微调 BS2

(2) 接收中断使能

进入 NVIC Settings, 打开 RX0 接收中断使能
至此 STM32 配置完成


### 10.4.2 关键代码

(1) CAN 初始化配置

```c
void CAN_Init()
{
    // 设置滤波器参数
    CAN_FilterTypeDef can_filter_t;
    can_filter_t.FilterBank = 0;
    can_filter_t.FilterMode = CAN_FILTERMODE_IDMASK;
    can_filter_t.FilterScale = CAN_FILTERSCALE_32BIT;
    can_filter_t.FilterIdHigh = 0x0000;
    can_filter_t.FilterIdLow = 0x0000;
    can_filter_t.FilterMaskIdHigh = 0x0000;
    can_filter_t.FilterMaskIdLow = 0x0000;
    can_filter_t.FilterActivation = ENABLE;
    can_filter_t.FilterFIFOAssignment = CAN_RX_FIFO0;
    can_filter_t.SlaveStartFilterBank = 14;

    // 调用滤波器配置
    HAL_CAN_ConfigFilter(&hcan, &can_filter_t);
    // 启动 CAN 外设
    HAL_CAN_Start(&hcan);
    // 启用 FIFO0 的接收中断
    HAL_CAN_ActivateNotification(&hcan, CAN_IT_RX_FIFO0_MSG_PENDING);
}
```

HAL 库的 HAL_CAN_INIT() 只初始化了引脚, 时钟分频等基础配置
还需要另外初始化 CAN 滤波器, 激活中断
全部打包在新的 CAN_INIT() 函数内

[点拨] 在 CAN_FILTERMODE_IDMASK 下
FilterId 是 "期望值"
FilterMask 是 "哪些位参与比较"
1 = 必须匹配, 0 = 不关心
此处 Mask 全 0 等于放行所有 ID
若只想收 0x201
可把 FilterIdHigh 设为 0x201 << 5
标准帧 ID 在 32 位寄存器中左对齐到 bit31~21
Mask 设为 0x7FF << 5
改用 CAN_FILTERMODE_IDLIST 时
一次最多登记 2 个 (16 位尺度) 或 4 个 (32 位尺度) 精确 ID
且同样要在 HAL_CAN_Start() 之前配置

(2) 构建电机结构体

```c
typedef struct {
    float _angle;         // 当前角度（单位：度），由编码器解析得到
    float _velocity;      // 当前速度（单位：度/秒）
    float _current;       // 电机电流反馈（单位：mA 或 A，根据解码方式）
    float _temp;          // 电机温度（单位：°C）

    float _angle_last;    // 上一次的角度值，用于角度跳变判断
    float _spin_times;    // 累积转动圈数，用于角度全范围追踪
} MotorC;
```

(3) CAN 发送至电机

```c
// 向电机发送电压控制指令
void MOTOR_Set_Voltage(int16_t voltage)
{
    CAN_TxHeaderTypeDef tx_header;
    uint32_t tx_mailbox;
    uint8_t tx_data[8];

    // 配置发送帧头
    tx_header.StdId = 0x1FF;         // 标识符，对应电机的接收 ID
    tx_header.IDE = CAN_ID_STD;      // 标准帧
    tx_header.RTR = CAN_RTR_DATA;    // 数据帧
    tx_header.DLC = 0x08;            // 数据长度：8 字节

    // 构造数据帧内容
    tx_data[0] = voltage >> 8;       // 高 8 位
    tx_data[1] = voltage;            // 低 8 位

    if (HAL_CAN_AddTxMessage(&hcan, &tx_header, tx_data, &tx_mailbox) != HAL_OK) {
        Error_Handler();
    }
}
```

该函数将一个 16 位整型电压值 (int16_t voltage) 打包成 CAN 标准数据帧格式
并通过 HAL_CAN_AddTxMessage() 发送出去
将传入的参数修改为数组, 并对应构造新的数据帧
即可拓展为多电机控制

(4) 部分代码解析

```c
// 构造数据帧内容
    tx_data[0] = voltage >> 8;       // 高 8 位
    tx_data[1] = voltage;            // 低 8 位
```

这里 voltage 是一个 16 位整数 (范围 -30000~30000)
代表要发送给电机的控制电压值
这两行代码的作用是将这个 16 位的电压值拆分成两个 8 位的部分
分别存储到数据数组 tx_data 的第 0 个和第 1 个位置

1. voltage >> 8
将 16 位的 voltage 右移 8 位
这样原来高 8 位的值就移到了低 8 位
而高 8 位变为 0
然后赋值给 tx_data[0], 即存储高 8 位部分

2. voltage
直接取 voltage 的低 8 位
因为赋值给一个 8 位变量时高位会被丢弃
赋值给 tx_data[1], 即存储低 8 位部分

(5) CAN 从电机接收回调

```c
// 中断回调函数中 FIFO 接收与解析数据
void HAL_CAN_RxFifo0MsgPendingCallback(CAN_HandleTypeDef *hcan)
{
    CAN_RxHeaderTypeDef rx_message;
    uint8_t rx_data[8];

    HAL_CAN_GetRxMessage(hcan, CAN_RX_FIFO0, &rx_message, rx_data);    // 接收报文

    int16_t pos, vel, cur, tmp;

    // 判断是否为目标电机的反馈帧
    if (rx_message.StdId == 0x201) {
        pos = (rx_data[0] << 8 | rx_data[1]);    // 机械角度
        vel = (rx_data[2] << 8 | rx_data[3]);    // 转速
        cur = (rx_data[4] << 8 | rx_data[5]);    // 转矩电流
        tmp = (rx_data[6]);                      // 温度
        MOTOR_Update_Infos(&motor, pos, vel, cur, tmp);
    }
}

// 电机结构体属性更新函数
void MOTOR_Update_Infos(MotorC *motor, int16_t pos, int16_t vel, int16_t cur, int16_t temp)
{
    motor->_angle       = (float)pos * ENCODER_TO_ANGLE;
    motor->_velocity    = (float)vel;
    motor->_current     = cur;
    motor->_temp        = temp;

    // 根据当前与上一次角度的变化判断是否跨圈
    if (motor->_angle - motor->_angle_last < - 300)
        ++motor->_spin_times;
    else if(motor->_angle - motor->_angle_last > 300)
        --motor->_spin_times;

    motor->_angle_last = motor->_angle;
}
```

这里在回调内读取报文内容, 并解析数据
而后将参数传入更新函数, 用于更新电机状态结构体

[点拨] 回调里必须保证在中断中执行得足够快
HAL_CAN_GetRxMessage() 每次只取走 FIFO 中最前面的一帧
若一个控制周期内电机连发多帧
可在回调里用下面的循环取空
while (HAL_CAN_GetRxFifoFillLevel(&hcan, CAN_RX_FIFO0) > 0)
否则会触发 FIFO 溢出 (可查 CAN_IT_RX_FIFO0_OVERRUN)
另外反馈 ID 是 0x204 + 电机 ID 还是 0x200 + 电机 ID
取决于具体型号
务必对照该型号手册, 不能照抄 0x201

(6) 部分代码解析

```c
pos = (rx_data[0] << 8 | rx_data[1]);    // 机械角度
vel = (rx_data[2] << 8 | rx_data[3]);    // 转速
cur = (rx_data[4] << 8 | rx_data[5]);    // 转矩电流
tmp = (rx_data[6]);                      // 温度
```

以 pos 为例
占用 rx_data[0] 和 rx_data[1] 组合成一个 16 位数据
即 rx_data[0] 左移 8 位
然后与 rx_data[1] 进行按位或
实际上是相加, 因为移位后低位为 0
这样 rx_data[0] 作为高 8 位
rx_data[1] 作为低 8 位, 组合成一个 16 位整数

------

# 11 PID 算法


## 11.1 简介

PID (Proportional-Integral-Derivative) 控制器
是一种经典的闭环控制算法
广泛应用于工业控制, 机器人, 无人机, 温控系统等领域
其核心思想是通过比例, 积分, 微分三个环节的组合
动态调整系统输出
在 RM 中, 我们使用 PID 进行部分电机的控制
如摩擦轮, 拨弹轮等电机

PID 具有多种类型
如位置式 PID, 增量式 PID, 步进式 PID 等
这里主要介绍位置式 PID

PID 基本控制逻辑为: 目标位置 → 系统 → 输出 → 新位置


## 11.2 PID 控制的基本原理

(1) 误差信号 (Error)
定义

$err= SV(set\ value)-PV(process\ value)$

PID 控制器根据 $e(t)$ 计算控制量
目标是使得误差为 0

(2) PID 输出公式
1. 连续形式

$u(t)=K_p e(t)+K_I\int_0^t e(\tau)d\tau+K_D\frac{de(t)}{dt}$

2. 离散形式

$u(k)=K_p e(k)+K_i\sum_{i=0}^{k}e(i)+K_d\left[e(k)-e(k-1)\right]$

与 11.4.2 中的 `PID_GetPositionPID` 实现一致

(3) 三个核心组成部分
1. 比例 (P)
输出 $K_p\times err$
作用: 起主要控制作用, 使反馈量向目标值靠拢
2. 积分 (I)
输出 $K_I\int _t err\ dt$
作用: 消除系统存在的稳态误差
会使得震荡相对于更大收敛更慢, 但可能引起积分饱和
3. 微分 (D)
输出 $K_D\times \frac{d\ err}{d\ t}$
作用: 能反应偏差信号的变化趋势
可以理解为在系统中引入一个"早期修正信号"
从而加快系统的动作速度, 减小调节时间
对噪声有一种放大
示例 $\frac{d(0.01\sin{1000t})}{dt}=10\cos{1000t}$

(4) 积分饱和现象
积分饱和指当系统存在较大误差时
积分项会不断累积
导致积分项输出过大
即使误差已经减小或改变方向
系统仍然会产生较大的超调量

(5) PID 中的几种限幅
1. 总输出限幅
作用: 限制 PID 控制器的最终输出值
确保执行器 (如电机驱动器, 加热器) 不超出物理承受范围
2. 积分限幅
作用: 限制积分项的累积值
防止积分项过大导致系统超调或振荡
3. 微分限幅
作用: 抑制微分项对高频噪声的敏感度
平滑输出突变
4. 单步输出限幅
作用: 针对增量式 PID
限制每个控制周期内控制器输出量的变化幅度 (ΔU)
而非最终输出值 (U)
抑制执行器的机械冲击和系统振荡
确保控制动作平稳
增量式 PID 将在后续介绍

[点拨] 调参顺序建议先 Kp, 后 Ki, 再 Kd
先把 P 加到系统刚开始小幅等幅振荡, 再退回一点
然后加 I 消掉静差
D 最后加且从小值起
另外积分限幅和总输出限幅不是一回事
积分限幅限制的是 `PID_Err_all` 这个累加量, 防饱和
总输出限幅限制的是算完 P, I, D 之后的 `PID_Out`, 保护执行器
两者必须分别设
且代码里是先限积分, 再算输出, 最后限输出


### 11.2.1 PID 的工作流程

(1) 传感器测量被控量, 如温度, 速度等
得到实际值 (PV)
(2) 计算误差 $e(t)=SP−PV$
(3) 分别计算 P, I, D 三个分量的输出
并求和得到总控制量 $U(t)$
(4) 执行器 (如电机, 加热器) 输出 $U(t)$ 调整系统
(5) 循环, 继续读取新的实际值


### 11.2.2 PID 的优缺点

(1) 优点
1. 结构简单, 适用性强
2. 无需精确模型, 依赖参数调整
(2) 缺点
1. 对非线性, 时变系统效果有限
2. 微分项 (D) 易受噪声干扰


## 11.3 双环 PID 控制电机


### 11.3.1 为什么采用双环 (速度环 & 位置环)

通过 CAN 总线发送电流驱动无刷电机
或是改变 PWM 的占空比驱动直流电机
是为了通过控制扭矩控制转动速度
但很多时候需要控制的变量是位置而非速度
因此引入双环

(1) 外环为位置环
得到当前需要的速度
通过速度控制位置

(2) 内环为速度环
得到需要输出的转矩
通过转矩控制速度

[点拨] 串级双环能成立的前提是内环带宽远高于外环
一般速度环响应比位置环快 3~10 倍
所以速度环的调用周期要明显短于位置环
位置环输出还要做限幅后再送给速度环当目标值
否则内环跟不上外环指令
双环会互相干扰, 抖动


### 11.3.2 外环位置环

位置环常用 P/PD 控制
首先明确调节的期待效果
稳定, 快速转动到给定位置
少超调, 少稳态误差

(1) P
对于位置环, 位移 = 速度 × 时间, 无阻力
只要位置的给定和反馈有差值
在 P 的作用下就会产生速度指令, 进而改变位置
直至位置的给定值与反馈值没有误差
所以仅用 P 不会产生稳态误差

(2) I
反而, 引入 I 有可能会导致稳态误差

(3) D
引入 D 有助于系统快速收敛
使 P 到稳态误差为 0 的位置之后迅速衰减

当然实际情况 PID 参数如何调
还得看系统的具体表现

```cpp
// 位置PID结构体
typedef struct {
    float Kp, Kd;      // PI参数
    float target;       // 目标位置（单位：编码器脉冲数）
    float error_now;    // 本次误差
    float error_last;   // 上次误差
} PosPID;

float PosPID_Compute(PosPID* pid, float current_pos) {
    pid->error_now = pid->target - current_pos;

    float output = pid->Kp * error + pid->Kd * (pid->error_now - pid->error_last);
    pid->error_last = pid->error_now;
    return output;  // 输出为速度设定值
}
```

[点拨] 上面这段位置环代码里 `pid->Kp * error` 的 `error` 并没有定义
按语义应写成 `pid->error_now`
直接编译会报未声明标识符
结构体注释写的是"PI 参数"但成员实际是 `Kp, Kd`, PD 控制
抄写时别被注释带偏


### 11.3.3 内环速度环

速度环响应位置环输出的速度指令
这种设计并非物理上的"速度 = 位移/时间"计算
而是控制策略上的一种映射关系
位置误差越大
系统就需要越高的速度来快速消除该误差

常用 PI 控制
电机的运动方程

$Jα=T-T_L$

存在阻力
即系统的负载转矩, 摩擦转矩等等

(1) P
如果仅用 P 环节
速度环产生的电流指令未必能使电机的速度改变

(2) I
所以必须引入 I 环节, 消除稳态误差

(3) D
速度本身抖动较大
微分环节作为位置信息的求导再求导
如果编码器精度不高, 采样不准确
则容易放大噪声信号, 产生更大的干扰
因此少用 D


## 11.4 实验例程


### 11.4.1 设计思路

通过双环 PID 控制输出让电机达到固定位置

拆解问题
我们需要完成以下任务

(1) 电机速度控制
即得到 PID 的输出 U 后
如何传递给电机

(2) 电机速度和角度的读取
即如何拿到实际位置

(3) 目标值如何输入

(4) 构建双环 PID 算法 (C 语言)
1. 构建 PID 结构体
2. 参数初始化
3. 输入更新 (更新速度, 角度)
4. 计算输出


### 11.4.2 设计流程

任务 1, 2 可以通过 CAN 总线通信实现
任务 3 可以通过串口发送指定值并读取
本次实验主要关注双环 PID 算法的构建

(1) 构建 PID 结构体

```c
#include <stdio.h>
#include <math.h>

// PID结构体（存储状态和参数）
typedef struct
{
  float Kp1;
  float Ki1;
  float Kd1;
  float PID_Err_now;//误差
  float PID_Err_last;
  float PID_Err_lastlast;
  float PID_Err_all;//积分
  float PID_Out;//输出
  float PID_lastout;
  float PID_Target;//目标值
  float PID_lastTarget;
  float PID_Input;//输入
  float PID_LastInput;
  float PID_ErrAllMax; // PID积分限幅
  float PID_OutMax;  // PID输出限幅
  float PID_OutStep;   // PID输出步幅限制
} PID_t;
```

(2) 初始化 PID 参数

```c
void PID_ParamInit(PID_t* WhichPID)
{
    WhichPID->Kp1 = 10;
    WhichPID->Ki1 = 0;
    WhichPID->Kd1 = 0;
    WhichPID->PID_Err_now = 0.0;
    WhichPID->PID_Err_last = 0.0;
    WhichPID->PID_Err_lastlast = 0.0;
    WhichPID->PID_Err_all = 0.0;
    WhichPID->PID_Out = 0.0;
    WhichPID->PID_lastout = 0.0;
    WhichPID->PID_Target = 0.0;
    WhichPID->PID_Input = 0.0;
    WhichPID->PID_ErrAllMax = PID_DEFAULT_ERRALL_MAX;//换成实际值
    WhichPID->PID_OutMax = PID_DEFAULT_OUTPUT_MAX;//换成实际值
    WhichPID->PID_OutStep = PID_DEFAULT_OUTPUT_STEP_MAX;//换成实际值
}
```

(3) 更新参数

```c
void PID_Update(PID_t* WhichPID, float NowInput)
{

//更新误差和输入
    WhichPID->PID_Input = NowInput;

    WhichPID->PID_Err_lastlast = WhichPID->PID_Err_last;
    WhichPID->PID_Err_last = WhichPID->PID_Err_now;
    WhichPID->PID_Err_now = WhichPID->PID_Target - NowInput;

    WhichPID->PID_Err_all += WhichPID->PID_Err_now;

//积分限幅
    if (WhichPID->PID_Err_all > WhichPID->PID_ErrAllMax)
    {
       WhichPID->PID_Err_all = WhichPID->PID_ErrAllMax;
    }
    else if (WhichPID->PID_Err_all < -WhichPID->PID_ErrAllMax)
    {
       WhichPID->PID_Err_all = -WhichPID->PID_ErrAllMax;
    }
}
```

(4) 计算输出

```c
/*
    * @name   PID_GetPositionPID
    * @brief  位置式PID
    * @param  WhichPID PID结构体指针
    * @retval 输出
*/
float PID_GetPositionPID(PID_t* WhichPID)
{
    WhichPID->PID_Out =
          WhichPID->Kp1 * WhichPID->PID_Err_now + WhichPID->Kd1 * (WhichPID->PID_Err_now - WhichPID->PID_Err_last);
    WhichPID->PID_Out += (WhichPID->PID_Err_all * WhichPID->Ki1);

//输出限幅
    if (WhichPID->PID_Out >= WhichPID->PID_OutMax)
       WhichPID->PID_Out = WhichPID->PID_OutMax;
    if (WhichPID->PID_Out <= -WhichPID->PID_OutMax)
       WhichPID->PID_Out = -WhichPID->PID_OutMax;

//单步限幅
    if (WhichPID->PID_Out - WhichPID->PID_lastout > WhichPID->PID_OutStep)
    {
       WhichPID->PID_Out = WhichPID->PID_lastout + WhichPID->PID_OutStep;
    }
    if (WhichPID->PID_Out - WhichPID->PID_lastout < -WhichPID->PID_OutStep)
    {
       WhichPID->PID_Out = WhichPID->PID_lastout + -WhichPID->PID_OutStep;
    }

    WhichPID->PID_lastout = WhichPID->PID_Out;

    return WhichPID->PID_Out;
}
```

(5) 双环 PID 处理
位置环的输出作为速度环的输入, 速度设定值
速度环的输出再送给电机


## 11.5 PID 拓展


### 11.5.1 增量式 PID (Incremental PID)

(1) 增量式 PID 计算的是控制量的增量 (Δu)
即本次控制量相对于上一次的变化量
而非绝对控制量 (u)
避免误差累积导致的输出超限

(2) 公式表达
其中
$e(k)$ 为当前误差
$e(k−1)$, $e(k−2)$ 为历史误差
$u(k)$ 为输出值

推导原理: 计算控制量的增量 (Δu)
而非绝对值
避免积分饱和

易得

$u(k-1) = \sum_{i=1}^{k-1}\Delta u(i) = K_p *e_{k-1}+ K_i \sum_{i=1}^{k-1}e_i+K_d*(e_{k-1}-e_{k-2})$

$\Delta u(k)= u(k)-u(k-1)=K_p* (e_k-e_{k-1})+ K_i* e_k+K_d(e_{k}-2e_{k-1}+e_{k-2})$

$那么输出 u(k)=u(k-1)+\Delta u(k)$

观察 $\Delta u(k)$ 的特点

(1) 只需要用到上一次的输出 & 三次的误差
由于不会有误差的一直积累, 不用考虑积分限幅

(2) 控制增量 $Δu(k)$ 的确定仅与最近 3 次的采样值有关
遇到"尖刺"噪声
增量式不会严重持续影响系统的工作

(3) 积分截断效应大, 可能会有稳态误差


### 11.5.2 步进式 PID 与斜坡函数 (Ramp)

(1) 针对 PID 系统设定值发生较大突变时容易产生超调的问题
提出解决方案
并不改变 PID 算法结构本身
而是对设定值进行步进处理

(2) 微分冲击
设定值阶跃突变时
微分项对该突变求导而产生的输出冲击

(3) 解决方法: 让输入平滑
1. 采用步进式给定设定值
所谓步进式其实质是将设定值的突变修改为平缓的变化
即把一个阶跃修改为一个斜坡函数
2. 可以确定步长
知道步长后
就可以根据步长来不断修改设定值
直到目标值
3. 步进式 PID 虽然可以减少阶跃信号带来的干扰
但是也会让系统的响应速度变慢
可以调节步长来平衡两者之间的关系
步长越小运行越稳定, 系统响应速度越慢, 反之亦然


## 11.6 其他控制算法拓展


### 11.6.1 滑模控制 (SMC)

参考滑模控制器
https://robotega.feishu.cn/wiki/QtQtwTz26iZeK0kYL26cAoVznhb

------

# 12 FreeRTOS

本节只讲 FreeRTOS 的基本用法
更深入的了解可参考官方文档
RTOS 基础知识 - FreeRTOS™
https://www.freertos.org/zh-cn-cmn-s/Documentation/01-FreeRTOS-quick-start/01-Beginners-guide/01-RTOS-fundamentals


## 12.1 简介

FreeRTOS(Free Real-Time Operating System)
是一个开源的实时操作系统内核
专为嵌入式设备设计
它的作用是实现多任务调度和实时响应
使多个任务能够并行运行且互不干扰
从而提升系统的稳定性, 实时性和可维护性

它提供了任务管理, 调度器, 信号量, 队列
定时器, 事件组等功能
帮助开发者实现任务分工
任务间通信与资源同步


## 12.2 为什么需要 FreeRTOS

轮询

主动去循环检查状态

```c
while(1){
    看饭有没有做好();
    打游戏();
    if(饭做好了){
        去吃饭;
        break;
    }
}
```

(1) 重复执行浪费 CPU 资源
(2) 如果事件发生在检查周期间隙内
则响应会被延迟

中断

被动等待
CPU 自己执行一个任务
当某个事件发生时
停止当前任务
然后去执行中断服务程序 ISR
执行完后回来

```c
void 饭做好了EXTI_IRQHandler(void){
    去吃饭();
}

int main(void){
    while(1){
        打游戏();
    }
}
```

(1) 如果执行中断函数时间太长
会阻碍主程序运行
只能等待中断结束才能叫回来
(2) 当有很多个中断时
处理中断嵌套, 中断优先级变得复杂

典型场景
一开始在打游戏
然后死了等复活
趁此机会去扒两口饭
扒着扒着这边复活了
又回来继续打
两个任务看起来是并发的
不会相互影响, 不阻塞
并且可能有一个明显的优先级
用上述两种方式实现都比较复杂
而 FreeRTOS 可以很简单地解决这个问题


## 12.3 FreeRTOS 基本原理


### 12.3.1 任务(Task)和状态

任务就是一个正在运行的
可以被调度的独立执行单元
它通常是由用户编写的一个函数
FreeRTOS 会为每个任务分配
独立的堆栈空间和控制块
(TCB, Task Control Block)
并负责调度这些任务的执行

例如放电影可以拆分成两个任务
放声音和放画面

如果是对于裸机

```cpp
while(1){
    放画面();    //这里被阻塞
    放声音();
}
```

如果是使用 FreeRTOS

```cpp
// 每个运行1ms然后切换，对于感知上来说是并行的

void 放声音(){
    while(1){

    }
}

void 放画面(){
    while(1){

    }
}
```

(1) FreeRTOS 的任务在完成创建后
将由操作系统的调度器管理
切换也由调度器完成
用户只需要创建任务分配参数即可
(2) 任务是非阻塞的
支持多任务并发
操作系统会根据任务优先级
和时间片调度机制在不同任务之间切换
(3) 每个任务有独立的堆栈空间和上下文信息
操作系统切换任务时会保存和恢复这些信息

FreeRTOS 有四种正式状态

(1) `Running`(运行态)
1. 当前被 CPU 执行的任务
2. 系统中任意时刻只有一个 Running 任务
3. 一旦出现更高优先级任务 Ready
就会切换
(2) `Ready`(就绪态)
1. 准备运行, 但暂时没有获得 CPU
2. 多个同优先级任务会轮流进入 Running
即时间片轮转
(3) `Blocked`(阻塞态)
1. 正在等待某个事件
如延时, 信号量, 队列, 事件组
2. 阻塞时间可为有限
如 `vTaskDelay(100)`
也可为无限
如 `portMAX_DELAY`
3. 一旦等待事件完成
就会从 Blocked 转到 Ready
(4) `Suspended`(挂起态)
1. 人工调用 `vTaskSuspend()` 进入该状态
2. 不会自动恢复
必须手动 `vTaskResume()` 或 `xTaskResumeFromISR()`
3. 与 Blocked 不同
即使事件满足也不会恢复运行


### 12.3.2 Tick

Tick(节拍)是 FreeRTOS 中的时间心跳
由一个定时中断周期性地触发
用于维持任务调度和时间管理的基础单位
通常用内核自带的 SysTick 定时器
来触发 Tick 中断

每次 Tick 中断到来
系统就会

(1) 更新任务延时计数器
`vTaskDelay()` 和 `osDelay()` 基于 Tick 实现
(2) 判断哪些任务被唤醒
如延时结束
(3) 执行时间片轮转
相同优先级任务按 Tick 切换
(4) 启动上下文切换
如果有更高优先级任务 Ready

每次 Tick 代表的具体时间
由 `configTICK_RATE_HZ` 这个宏设置
在 MX 里面也可以直接设置

```cpp
#define configTICK_RATE_HZ 1000  // 表示 1ms 一次 Tick(Configuration 配置） 连起来就是"配置节拍频率"
```

因此不同设备中一个 Tick 代表的实际时间
可能不一样
为了便于移植和增加可读性
封装了 `pdMS_TO_TICKS` 函数
所以一般在写代码时不直接用 Tick
都直接写时间
然后用 `pdMS_TO_TICKS(500)` 转换一下

```cpp
/// 将毫秒数转换为 Tick 单位数（根据 configTICK_RATE_HZ 自动换算）
///
/// \param[in]     xTimeInMs     输入的时间（单位：毫秒）
///
/// \return 返回对应的 Tick 数（TickType_t 类型）
///
/// \note  FreeRTOS 中几乎所有延时或超时相关函数都使用 Tick 作为单位。
///        该宏用于将常用的“毫秒”单位转换为 RTOS 所需的 Tick 单位，
///        以便在不同 Tick 配置下仍保持时间行为一致。
///
/// \example
///     vTaskDelay(pdMS_TO_TICKS(100));  // 延时 100ms
///
/// \see    vTaskDelay()、xQueueReceive() 等支持 Tick 超时的函数
///
#define pdMS_TO_TICKS(xTimeInMs)   (((TickType_t)((xTimeInMs) * configTICK_RATE_HZ) / 1000U))
//pd portable/project defined(可移植的/项目定义的）  MS(毫秒) TO（转换到）ticks（节拍）
```


### 12.3.3 优先级与调度机制

FreeRTOS 是一个抢占式实时操作系统(RTOS)
调度器会优先运行
优先级最高, 就绪状态的任务

(1) 每个任务都有一个整数优先级
(2) 数字越大, 优先级越高
(3) 可以在创建任务的时设置优先级

因此主要存在以下两种调度机制

(1) 抢占式调度
高优先级任务一旦就绪
会立即抢占当前低优先级任务
(2) 时间片轮转, 默认启用
同一优先级的多个任务会平均分配时间片
轮流执行

时间片轮转的调度方法
是让相同优先级的几个任务轮流运行
每个任务运行一个时间片
任务在时间片运行完之后
操作系统自动切换到下一个任务运行
在任务运行的时间片中
也可以提前让出 CPU 运行权
调用 `vTaskDelay`
把它交给下一个任务运行
FreeRTOS 的时间片固定为一个时钟节拍
即一个 tick

(1) 相同优先级的任务按 FIFO(First In First Out) 顺序排列
谁先进入 Ready 状态排前面
(2) 每次系统 Tick 到来, 调度器检查
1. 是否有更高优先级任务 Ready
如果有则抢占
2. 如果没有, 则同优先级任务轮换

```cpp
void Task1(void *pvParameters) {
    for (;;) {
        printf("T1\n");
    }
}

void Task2(void *pvParameters) {
    for (;;) {
        printf("T2\n");
    }
}

int main(void) {
    xTaskCreate(Task1, "T1", 128, NULL, 2, NULL);
    xTaskCreate(Task2, "T2", 128, NULL, 2, NULL);  // 与 T1 同优先级

    vTaskStartScheduler();
}
```

```cpp
T1
T2
T1
T2
...
```

如何解决高优先级任务持续占用
导致低优先级任务无法执行的问题
两个任务之间如果有条件执行关系

可以通过任务通知, 队列, 信号量唤醒任务
还可以使用互斥锁等
这涉及到更多的 FreeRTOS 知识


### 12.3.4 区分 CMSIS, HAL, FreeRTOS API

首先需要知道这些都是谁开发的
就能理解它们互相之间的关系了

(1) CMSIS
Cortex Microcontroller Software Interface Standard
CMSIS 是 ARM 公司推出的一套
标准化的软件接口和驱动层架构
提供统一的软件接口标准
使不同厂商的 MCU 开发更加一致
它不只是一个文件
而是一个完整的软件包
包含多个组件
(2) HAL
HAL 是由 STMicroelectronics(意法半导体)官方开发和维护的嵌入式驱动库
专门用于其 STM32 系列微控制器
提供更易用的 API 接口
基于 CMSIS 构建
也就是说会调用 CMSIS 提供的接口
(3) FreeRTOS
FreeRTOS 是一个由 Amazon 提供的第三方操作系统组件
运行在 Cortex-M 内核之上
相对于 CMSIS 和 HAL 来说
它是独立于芯片厂商与 ARM 的 RTOS 内核
为嵌入式系统增加了多任务调度
延时, 同步等操作系统功能
CMSIS-RTOS 中的 API 底层可由 FreeRTOS 实现

因此可以理解成这样
ARM 造好内核, 提供 CMSIS 接口
它有组件支持 FreeRTOS
调用 FreeRTOS API
ST 基于内核封装好芯片
并提供了 HAL, LL 等库便于用户开发
调用 CMSIS 接口


## 12.4 常用函数

```cpp
/// 创建一个任务并将其加入活动任务列表（自动开始调度执行）
///
/// \param[in]     func          任务函数的入口地址，必须为 void 类型并接收一个 void* 参数：
///                              函数原型应为：void TaskFunction(void *argument);
///                              当任务启动时，从该函数入口开始运行。
///
/// \param[in]     argument      启动时传递给任务函数的参数指针，
///                              可传入结构体、数组、整型地址等任意类型（通过 void* 兼容）。
///
/// \param[in]     attr          任务属性结构体指针（osThreadAttr_t 类型），用于配置：
///                              - 任务名称（.name）
///                              - 堆栈大小（.stack_size）
///                              - 优先级（.priority）
///                              - 是否使用静态分配（.stack_mem / .cb_mem）
///                              若传入 NULL，则使用 CMSIS 默认属性（自动分配内存，普通优先级）。
///
/// \return 返回该任务的标识符（osThreadId_t 类型），可用于后续操作该任务；
///         如果任务创建失败（如内存不足、任务数达到上限、属性配置非法），则返回 NULL。
///
/// \note
///     - 该函数是 CMSIS-RTOS2 标准接口，在底层运行于 FreeRTOS 内核时，
///       实际调用的是 FreeRTOS 的任务创建函数：
///
///         - 若使用动态内存分配 → 调用 `xTaskCreate()`
///         - 若使用静态内存分配 → 调用 `xTaskCreateStatic()`
///
///     - 返回值本质是 FreeRTOS 的任务句柄（TaskHandle_t），经过类型转换为 osThreadId_t。
///     - 任务一经创建即自动转入就绪态，等待调度器分配 CPU 执行。
///
/// \example
///     const osThreadAttr_t myTaskAttr = {
///         .name = "MyTask",
///         .priority = osPriorityNormal,
///         .stack_size = 512
///     };
///     osThreadId_t tid = osThreadNew(MyTask, NULL, &myTaskAttr);
///
/// \see    xTaskCreate()           FreeRTOS 原生动态任务创建函数
/// \see    xTaskCreateStatic()     FreeRTOS 原生静态任务创建函数
/// \see    osThreadTerminate()     终止任务
/// \see    osThreadSetPriority()   设置任务优先级
/// \see    osThreadYield()         当前任务主动让出 CPU
///
osThreadId_t osThreadNew(osThreadFunc_t func, void *argument, const osThreadAttr_t *attr);
```

```cpp
/// 获取当前系统 Tick 计数值（即自系统启动以来经过的 Tick 数）
///
/// \return 返回一个 `uint32_t` 类型的值，表示从操作系统启动以来累计的 Tick 数。
///         每次 SysTick 中断触发时，该值会自动增加，常用于超时控制、时间戳记录、周期判断等。
///
///         Tick 的单位由 `osKernelGetTickFreq()` 决定，通常在 `configTICK_RATE_HZ` 中设置，
///         例如设为 1000 则代表每 Tick 间隔 1ms。
///
///         返回值在 32 位平台上大约可运行 49.7 天后回绕归零；
///         若使用 16 位 Tick（通过配置 FreeRTOS 选项），则约 65 秒回绕一次。
///
/// \note   该函数必须在调度器启动（`osKernelStart()`）之后调用，否则返回值恒为 0。
///         该函数是线程安全的，也可在中断服务程序（ISR）中使用。
///
/// \see    osKernelGetTickFreq()        获取 Tick 频率（单位 Hz）
/// \see    osDelay()                    延时函数（基于 Tick）
/// \see    pdMS_TO_TICKS()              毫秒转 Tick 宏（需结合 FreeRTOS 使用）
/// \see    xTaskGetTickCount()          FreeRTOS 原生版本
///
uint32_t osKernelGetTickCount(void);
```

```cpp
/// 当前任务延时指定的 Tick 数（即“从现在开始延时 N Tick”）
///
/// \param[in]     ticks     延时的 Tick 数（单位为 Tick）
///
/// \return 返回 osOK 表示成功；若在中断中调用，则返回 osErrorISR。
///
/// \note  调用该函数后，当前任务将进入 Blocked 状态，
///        在指定 Tick 数时间后重新进入 Ready 状态等待调度。
///        此延时不会阻塞其它任务运行，适用于任务节拍控制、让出 CPU 等。
///
/// \warning 参数单位是 **Tick** 而非毫秒！
///          若想以毫秒延时，应配合 `pdMS_TO_TICKS(ms)` 使用，例如：
///          `osDelay(pdMS_TO_TICKS(500));` 表示延时 500ms。
///
///          若系统配置为 `configTICK_RATE_HZ = 1000`，则 1 Tick ≈ 1ms；
///          若为 250Hz，则 1 Tick ≈ 4ms，因此避免误解单位！
///
/// \example
///     osDelay(pdMS_TO_TICKS(100));  // 延时 100ms
///
/// \see    pdMS_TO_TICKS()       将毫秒转换为 Tick
/// \see    vTaskDelay()          FreeRTOS 原生延时函数
/// \see    osDelayUntil()        精确周期控制函数（CMSIS）
///
/// \note   若 ticks = 0U，则不会发生延时（不会进入 Blocked）；
///         若在中断中调用，会直接返回错误 osErrorISR。
///
osStatus_t osDelay(uint32_t ticks);
//相对时间
```

```cpp
/// 延时直到指定的绝对 Tick 时间（用于精确周期任务控制）
///
/// \param[in]     ticks     下次唤醒的绝对 Tick 时间（单位为 Tick）
///
/// \return 返回 osOK 表示成功；若在中断中调用，则返回 osErrorISR；
///         若系统尚未启动调度器，也可能返回 osError.
///
/// \note  与 `osDelay()` 不同，`osDelayUntil()` 是基于**绝对时间点**的延时，
///        适用于周期任务执行控制。调用后，当前任务将被阻塞，
///        直到系统 Tick 计数达到或超过指定的 `ticks` 值。
///
///        若当前时间已超过 `ticks`，任务将立即恢复（不会额外延时）。
///        该机制适合周期性任务：
///
///        ```c
///        tick += pdMS_TO_TICKS(100);   // 每次增加固定周期
///        osDelayUntil(tick);           // 精确控制周期节拍
///        ```
///
/// \warning 参数 `ticks` 必须为绝对时间，通常配合 `osKernelGetTickCount()` 使用。
///          不应直接传入 `pdMS_TO_TICKS(ms)` 等相对延时值。
///
/// \example
///     uint32_t lastWakeTime = osKernelGetTickCount();
///     for (;;) {
///         // 执行周期性任务
///         toggleLED();
///
///         // 等待到下一个 100ms 的时刻
///         lastWakeTime += pdMS_TO_TICKS(100);
///         osDelayUntil(lastWakeTime);
///     }
///
/// \note   该函数的底层在 FreeRTOS 中调用的是：
///         `vTaskDelayUntil()`，CMSIS 封装成 `osDelayUntil()` 接口；
///         参数类型与 FreeRTOS 不同，为值传递而不是引用传递。
///
/// \see    osKernelGetTickCount()    获取当前 Tick
/// \see    vTaskDelayUntil()         FreeRTOS 原生绝对延时函数
/// \see    osDelay()                 基于相对时间的延时（单位 Tick）
///
/// \attention 注意：
///     - 在 FreeRTOS 中，`vTaskDelayUntil()` 是引用参数；
///     - 在 CMSIS 中，`osDelayUntil()` 是值参数，需要自己维护时间变量。
///
osStatus_t osDelayUntil(uint32_t ticks);
//绝对时间
```

[点拨] CMSIS 版 `osDelay` 系列不能在中断里调用
会直接返回 `osErrorISR`
在 ISR 里要用带 `FromISR` 后缀的原生 API
例如 `xQueueSendFromISR()`
`xSemaphoreGiveFromISR()`
`xTaskResumeFromISR()`
并检查其返回的 `pxHigherPriorityTaskWoken`
为 `pdTRUE` 时
在 ISR 退出前调用 `portYIELD_FROM_ISR()`


## 12.5 实验例程


### 12.5.1 MX 配置

选择芯片 STM32F103C8t6
进入该界面
SYS 按这样配置
默认的 `SysTick` 会被 FreeRTOS 用作系统 Tick 源
所以要把 HAL 库的时间基准(Timebase Source)改为 `TIMx`
避免冲突和延时异常

[点拨] 这个选项在 CubeMX 的 System Core 里改
在 SYS 的 Timebase Source 一项
若保持 `SysTick`
`HAL_Delay()` 与 FreeRTOS 会争用同一个定时器
表现为 `HAL_Delay` 延时不准甚至死等
工程生成后再改这一项
会导致 HAL 时基初始化代码不完整
最好在建工程时就定好

RCC 配置外部晶振
然后配置主频

先打开 Usart 的相关功能
配置为异步, 打开全局中断

配置 DMA
方便实现串口重定向
设置 RX 的 Mode 为 Circular
不断等待接收

检查 NVIC

打开 FreeRTOS
选择使用 CMSIS-V2

创建任务
设置堆栈为 256
不然会容易溢出

[点拨] CubeMX 里任务 Stack Size 的单位是 word(4 字节)
填 256 即 1024 字节
而 `configTOTAL_HEAP_SIZE` 在 FreeRTOS 的 Config parameters 里
是所有任务栈, 队列, 信号量共用的堆
任务多或栈偏大时
会出现 `pvPortMalloc` 返回 NULL, 任务创建失败
可把该值从默认 3072 调大
并打开 `configCHECK_FOR_STACK_OVERFLOW`
配合 `vApplicationStackOverflowHook` 排查

勾选为每个外设生成一对 `.c/.h` 文件

选择使用 1.8.5 固件包
否则报错找不到库
然后生成代码即可


### 12.5.2 测试程序

在 `usart.c` 中配置串口重定向
加入下面这段代码
注意写在

```plaintext
/* USER CODE BEGIN 1 */
/* USER CODE END 1 */
```

这中间
这样每次更新 MX 不会丢失代码
养成代码习惯

```cpp
#define TX_BUF_SIZE 512
uint8_t send_buff[TX_BUF_SIZE];
void usart_printf(const char *format, ...)
{
  va_list args;
  uint32_t length;

  va_start(args, format);
  length = vsnprintf((char *)send_buff, TX_BUF_SIZE, (const char *)format, args);
  va_end(args);
  HAL_UART_Transmit_DMA(&huart1, (uint8_t *)send_buff, length);
}
```

然后在 `usart.h` 中声明
随后引入该库就可以调用这个打印函数了
串口接收软件推荐使用 VOFA
下载地址: https://www.vofa.plus/

下面进行两种调度方式的测试

抢占调度
高优先级任务就绪即抢占低优先级任务

时间片轮转

(1) 不让出 CPU
同优先级任务在 Tick 到来时被动轮换
(2) 主动让出 CPU
任务中调用 `vTaskDelay` 提前交出 CPU

[点拨] `vTaskDelay()` 与 `HAL_Delay()` 不要混用
`HAL_Delay()` 是忙等
基于 HAL 时基
改到 TIMx 后仍需 HAL 中断在跑
期间任务不进入 Blocked
同优先级任务拿不到 CPU
低优先级任务被饿死
在 `vTaskSuspendAll()` 或临界区内调用 `HAL_Delay()`
还可能因时基中断被挂起而永久卡死
RTOS 任务里一律用 `osDelay()` 或 `vTaskDelay()`

测试中出现 `211121112`
多打了一个 1 不是因为没执行
而是两个任务同时打印
串口一次只能输出后面一个
属于 Buffer 填充问题

------

# 13 CMake


## 13.1 简单的 CMake 开发及编译原理简介

使用 CLion 开发 STM32 时
CubeMX 会生成一个 `CMakeLists.txt` 文件
这就是常说的 CMake 文件
为了理解它在嵌入式与 C/C++ 工程中的作用
先回顾 C/C++ 的编译原理


### 13.1.1 编译原理简介

需要一系列任务和操作
来使人类的语言能被机器理解
这些任务和操作, 对于 C/C++ 而言
即为编译和汇编

(1) 翻译程序
将一种计算机编程语言所编写的程序(源程序)
翻译成与之等价的另外一种计算机语言的程序(目标程序)
完成这个翻译工作的程序称为翻译程序
编译程序, 解释程序, 汇编程序均被认为是翻译程序
(2) 编译程序
源程序语言是高级语言
目标程序语言是汇编语言或机器语言之类的低级语言
这样的翻译程序称为编译程序
(3) 汇编程序
源程序语言是汇编语言
输出目标程序语言是机器语言
这样的翻译程序称为汇编程序
(4) 解释程序
在词法, 语法, 语义分析方面与编译程序的工作原理基本相同
但在执行过程中不产生目标程序
而是直接解释执行源程序或源程序的内部形式(中间代码)
即边解释边执行
Python 解释器就是一种解释程序

通常目标程序文件仍不能被 CPU 直接执行
需要通过链接程序进行连接后才可生成可执行程序 `.exe`
现代编译器通常包含以下的主要工作流程

[点拨] 对应到 GCC 的实际命令
这条流水线是四个可单独执行的阶段
(1) 预处理, `-E`, 展开宏与头文件, 产物 `.i`
(2) 编译, `-S`, 生成汇编 `.s`
(3) 汇编, `-c`, 生成目标文件 `.o`
(4) 链接, 无开关, 由 `.o` 与库合成 `.elf`
静态库 `.a` 只是 `.o` 的打包(`arm-none-eabi-ar`)
链接时被整体拷入可执行文件
动态库 `.so/.dll` 则在运行时才加载
这也是 CMake 里 `add_library(... STATIC/SHARED ...)` 的实际差别


### 13.1.2 为什么需要 CMake 来管理项目


#### 13.1.2.1 项目(A Project)是什么

项目通过文件, 目录和工具链规范代码和资源
确保可维护性和协作效率

大型项目可能涉及成千上万个文件
那么如何告诉编译器

我的项目包含了什么
用了什么外部库
要把哪些文件编译成库文件
哪些文件作为可执行文件去执行

这是一个非常重要的问题
而 CMake 提供了一个便捷的方法


#### 13.1.2.2 CMake 的好处

管理这样一个 C 项目的方法多如牛毛
你可能听过好几种 Make 工具
例如以下几种
(1) GNU Make
(2) Qt 的 qmake
(3) 微软的 MS nmake
(4) BSD Make, 即 pmake
(5) Makepp
以及其他 Make 工具

这些 Make 工具遵循着不同的规范和标准
所执行的 Makefile 格式也千差万别
由此带来一个严峻的问题
如果软件想跨平台
必须保证能够在不同平台编译
而如果使用上面的 Make 工具
就得为每一种标准写一次 Makefile
这会带来很大的重复工作量

CMake 就是针对上述问题而设计的工具
(1) 首先允许开发者编写一种平台无关的 `CMakeLists.txt` 文件
来定制整个编译流程
(2) 然后根据目标用户的平台
进一步生成所需的本地化 Makefile 和工程文件
如 Unix 的 Makefile 或 Windows 的 Visual Studio 工程
(3) 从而做到 "Write once, run everywhere"

显然, CMake 是一个比上述几种 make 更高级的编译配置工具
一些使用 CMake 作为项目架构系统的知名开源项目有
(1) VTK
(2) ITK
(3) KDE: https://zhida.zhihu.com/search?content_id=206897677&content_type=Article&match_order=1&q=KDE&zhida_source=entity
(4) OpenCV
(5) OSG: https://zhida.zhihu.com/search?content_id=206897677&content_type=Article&match_order=1&q=OSG&zhida_source=entity

由此可以理解
CMake 是一个跨平台的构建系统生成器
用于自动化管理代码的编译过程
它通过读取配置文件(`CMakeLists.txt`)生成标准的构建文件
如 Makefile, Visual Studio 项目文件等
从而简化跨平台项目的构建流程
CMake 凭借其跨平台能力, 灵活的配置语法和强大的工具链集成
成为 C/C++ 项目的首选构建工具
尽管其语法有一定学习成本
但其在简化构建流程, 提升可维护性方面的优势
使其在开源和商业领域均被广泛采用


### 13.1.3 简单的 CMake 开发: 以 Cube 生成的 STM32 工程为例


#### 13.1.3.1 CMake 安装

(1) 在已安装使用的 CLion + CubeMX 工具链中
已经捆绑安装 CMake
使用捆绑安装的 CMake 即可
(2) 但要在环境变量中把 CMake 的路径加进去
并重启电脑
(3) 在终端中输入 `cmake`
若有输出, 则证明安装成功
(4) 同时可以把 ninja 也一起放入环境变量中

在 CLion + CubeMX 工具链中
各开发工具的作用及关系如下

(1) MinGW
环境工具集, 提供基础的开发环境
包括编译工具链(如 GCC, GDB)和运行库
(2) CMake
解析项目中的 `CMakeLists.txt`
生成构建规则文件(如 `build.ninja`)
(3) Ninja
构建工具, 执行 CMake 生成的构建文件(如 `build.ninja`)
调用编译器完成实际编译和链接
(4) arm-none-eabi-gcc/g++
编译器, 将源代码编译为目标文件(`.o`)
并链接生成最终的可执行文件或库
被 `build.ninja` 调用


#### 13.1.3.2 工程管理规范

在 CLion 中, 默认状态下不能直接编译
需要修改 `CMakeLists.txt` 告诉 CMake 该项目的结构


#### 13.1.3.3 最低版本要求

这是每个 `CMakeLists.txt` 都必须包含的第一行

```plaintext
cmake_minimum_required(VERSION 3.1）
```

(1) 这句话说明该工程使用的最低 cmake 版本
(2) 如果需要使用别人的工程
但你们的 cmake 版本不一致(你的版本比他低)
那么更改这个版本号即可编译


#### 13.1.3.4 添加头文件路径

```plaintext
include_directories(User/Framework/ User/MCUDriver/)
```

(1) 必须要添加路径
否则部分文件将不会编译, 或无法索引引用

[点拨] `include_directories()` 是"目录级"的全局设置
会影响它之后定义的所有目标
现代 CMake 更推荐用
`target_include_directories(目标名 PUBLIC/PRIVATE 路径)`
把包含路径绑定到具体目标上
避免不同库的头文件互相污染
这也是 13.2 节要展开的核心差异


#### 13.1.3.5 源文件收集

```plaintext
file(GLOB_RECURSE SOURCES "Library/*.*" "Core/*.*" ...)
```

(1) 作用: 递归收集所有源文件(C/C++/汇编)
需要把所有工程相关文件夹写在这里

以上为简单开发一个 CMake 项目所需要修改的地方
对于 STM32 项目来说
仅修改以上几处就能满足开发要求
下面介绍该 CMake 项目中其他字段

```cmake
#THIS FILE IS AUTO GENERATED FROM THE TEMPLATE! DO NOT CHANGE!
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_VERSION 1)
cmake_minimum_required(VERSION 3.23)

# specify cross-compilers and tools
set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER arm-none-eabi-g++)
set(CMAKE_ASM_COMPILER  arm-none-eabi-gcc)
set(CMAKE_AR arm-none-eabi-ar)
set(CMAKE_OBJCOPY arm-none-eabi-objcopy)
set(CMAKE_OBJDUMP arm-none-eabi-objdump)
set(SIZE arm-none-eabi-size)
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)

# project settings
project(STM32F407IGH6TR_board C CXX ASM)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_C_STANDARD 11)

#Uncomment for hardware floating point
add_compile_definitions(ARM_MATH_CM4;ARM_MATH_MATRIX_CHECK;ARM_MATH_ROUNDING)
add_compile_options(-mfloat-abi=hard -mfpu=fpv4-sp-d16)
add_link_options(-mfloat-abi=hard -mfpu=fpv4-sp-d16)

#Uncomment for software floating point
#add_compile_options(-mfloat-abi=soft)

add_compile_options(-mcpu=cortex-m4 -mthumb -mthumb-interwork)
add_compile_options(-ffunction-sections -fdata-sections -fno-common -fmessage-length=0)

# uncomment to mitigate c++17 absolute addresses warnings
#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-register")

# Enable assembler files preprocessing
add_compile_options($<$<COMPILE_LANGUAGE:ASM>:-x$<SEMICOLON>assembler-with-cpp>)

if ("${CMAKE_BUILD_TYPE}" STREQUAL "Release")
    message(STATUS "Maximum optimization for speed")
    add_compile_options(-Ofast)
elseif ("${CMAKE_BUILD_TYPE}" STREQUAL "RelWithDebInfo")
    message(STATUS "Maximum optimization for speed, debug info included")
    add_compile_options(-Ofast -g)
elseif ("${CMAKE_BUILD_TYPE}" STREQUAL "MinSizeRel")
    message(STATUS "Maximum optimization for size")
    add_compile_options(-Os)
else ()
    message(STATUS "Minimal optimization, debug info included")
    add_compile_options(-Og -g)
endif ()

include_directories(Core/Inc Drivers/STM32F4xx_HAL_Driver/Inc Drivers/STM32F4xx_HAL_Driver/Inc/Legacy Drivers/CMSIS/Device/ST/STM32F4xx/Include Drivers/CMSIS/Include Middlewares/Third_Party/FreeRTOS/Source/include Middlewares/Third_Party/FreeRTOS/Source/CMSIS_RTOS Middlewares/Third_Party/FreeRTOS/Source/portable/GCC/ARM_CM4F Middlewares/ST/ARM/DSP/Inc USB_DEVICE/App USB_DEVICE/Target Middlewares/ST/STM32_USB_Device_Library/Core/Inc Middlewares/ST/STM32_USB_Device_Library/Class/CDC/Inc)

# global macro definition
add_definitions(
        -DDEBUG
        -DUSE_HAL_DRIVER
        -DSTM32F407xx
        -DARM_MATH_CM4
        -D__FPU_USED=1U
        -D__FPU_PRESENT=1U
        -DARM_MATH_MATRIX_CHECK
        -DARM_MATH_ROUNDING
)
file(GLOB_RECURSE SOURCES "Library/*.*" "Core/*.*" "Middlewares/*.*" "Drivers/*.*" "User/*.*")

set(LINKER_SCRIPT ${CMAKE_SOURCE_DIR}/STM32F407IGHX_FLASH.ld)

add_link_options(-Wl,-gc-sections,--print-memory-usage,-Map=${PROJECT_BINARY_DIR}/${PROJECT_NAME}.map)
add_link_options(-mcpu=cortex-m4 -mthumb -mthumb-interwork)
add_link_options(-T ${LINKER_SCRIPT})

link_directories(${PROJECT_SOURCE_DIR}/Middlewares/ST/ARM/DSP/Lib)
link_libraries("arm_cortexM4lf_math.a")

add_executable(${PROJECT_NAME}.elf ${SOURCES} ${LINKER_SCRIPT})

# target link ahrs.lib
target_link_libraries(${PROJECT_NAME}.elf ${PROJECT_SOURCE_DIR}/User/Framework/IMU/algorithm/AHRS.lib)

set(HEX_FILE ${PROJECT_BINARY_DIR}/${PROJECT_NAME}.hex)
set(BIN_FILE ${PROJECT_BINARY_DIR}/${PROJECT_NAME}.bin)

add_custom_command(TARGET ${PROJECT_NAME}.elf POST_BUILD
        COMMAND ${CMAKE_OBJCOPY} -Oihex $<TARGET_FILE:${PROJECT_NAME}.elf> ${HEX_FILE}
        COMMAND ${CMAKE_OBJCOPY} -Obinary $<TARGET_FILE:${PROJECT_NAME}.elf> ${BIN_FILE}
        COMMENT "Building ${HEX_FILE}
Building ${BIN_FILE}")
```


#### 13.1.3.6 交叉编译工具链配置

```cmake
set(CMAKE_SYSTEM_NAME Generic)  # 声明为裸机（无操作系统）系统
set(CMAKE_SYSTEM_VERSION 1)
set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER arm-none-eabi-g++)
set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)
set(CMAKE_AR arm-none-eabi-ar)
set(CMAKE_OBJCOPY arm-none-eabi-objcopy)
set(CMAKE_OBJDUMP arm-none-eabi-objdump)
set(SIZE arm-none-eabi-size)
```

(1) 作用: 配置 ARM 交叉编译工具链
针对 STM32F4 芯片生成裸机(无操作系统)程序


#### 13.1.3.7 项目基础设置

```plaintext
project(STM32F407IGH6TR_board C CXX ASM)  # 项目名和支持的语言
set(CMAKE_CXX_STANDARD 17)  # C++17 标准
set(CMAKE_C_STANDARD 11)    # C11 标准
```

(1) 作用: 定义项目名称
并指定代码使用的 C/C++ 语言标准


#### 13.1.3.8 硬件浮点配置

```plaintext
add_compile_definitions(ARM_MATH_CM4;ARM_MATH_MATRIX_CHECK;ARM_MATH_ROUNDING)
add_compile_options(-mfloat-abi=hard -mfpu=fpv4-sp-d16)  # 启用硬件浮点
add_link_options(-mfloat-abi=hard -mfpu=fpv4-sp-d16)
```

(1) 作用: 启用 Cortex-M4 的硬件浮点单元(FPU)
提升浮点运算性能

[点拨] `-mfpu` 与 `-mfloat-abi` 必须与实际芯片的 FPU 一致
F407 是单精度 FPU(`fpv4-sp-d16`)
若照抄成 `fpv5-d16` 或双精度型号
启动后浮点指令会进入 HardFault
这类工具链 `set(...)` 通常写在独立的 `cmake/gcc-arm-none-eabi.cmake`
即工具链文件, 由 `CMAKE_TOOLCHAIN_FILE` 指定
CubeMX 生成工程时可在 `CMakeLists.txt` 同级的 `cmake/` 目录下找到
CLion 的设置页里对应 Settings 页
路径为 Build, Execution, Deployment
再到 CMake 的 Toolchain file 一项


#### 13.1.3.9 通用编译选项

```plaintext
add_compile_options(
    -mcpu=cortex-m4    # 指定 CPU 架构
    -mthumb            # 使用 Thumb 指令集（节省代码空间）
    -mthumb-interwork  # 允许 Thumb 和 ARM 指令混合调用
    -ffunction-sections -fdata-sections  # 函数和数据分节（便于链接优化）
    -fno-common        # 禁止未初始化变量共用段
    -fmessage-length=0 # 错误信息完整输出
)
```

(1) 嵌入式优化
`-ffunction-sections` 和 `-fdata-sections` 允许链接器移除未使用的代码
通过 `-Wl,--gc-sections`, 减少固件体积


#### 13.1.3.10 构建类型配置

```plaintext
if ("${CMAKE_BUILD_TYPE}" STREQUAL "Release")
    add_compile_options(-Ofast)  # 最大速度优化
elseif ("${CMAKE_BUILD_TYPE}" STREQUAL "RelWithDebInfo")
    add_compile_options(-Ofast -g)  # 优化 + 调试信息
elseif ("${CMAKE_BUILD_TYPE}" STREQUAL "MinSizeRel")
    add_compile_options(-Os)  # 最小体积优化
else ()
    add_compile_options(-Og -g)  # 调试优化 + 调试信息
endif ()
```

(1) 作用: 根据构建类型(Debug/Release)动态调整优化选项


#### 13.1.3.11 全局宏定义

```plaintext
add_definitions(
    -DDEBUG             # 启用调试模式
    -DUSE_HAL_DRIVER    # 使用 STM32 HAL 库
    -DSTM32F407xx       # 定义芯片型号
    -DARM_MATH_CM4      # 启用 CMSIS-DSP 库的 Cortex-M4 支持
    ...
)
```

(1) `USE_HAL_DRIVER`: HAL 库的启用标志
(2) `STM32F407xx`: 芯片型号
HAL 库通过此宏选择特定型号的驱动代码


#### 13.1.3.12 链接配置

```plaintext
set(LINKER_SCRIPT ${CMAKE_SOURCE_DIR}/STM32F407IGHX_FLASH.ld)  # 指定链接脚本
add_link_options(
    -Wl,-gc-sections      # 移除未使用的段
    -T ${LINKER_SCRIPT}   # 指定链接脚本
    ...
)
link_libraries("arm_cortexM4lf_math.a")  # 链接 CMSIS-DSP 数学库
```

(1) 链接脚本作用: 定义内存布局(Flash/ROM 和 RAM 的地址分配)


#### 13.1.3.13 生成可执行文件与后处理

```plaintext
add_executable(${PROJECT_NAME}.elf ${SOURCES} ${LINKER_SCRIPT})
target_link_libraries(${PROJECT_NAME}.elf ${PROJECT_SOURCE_DIR}/.../AHRS.lib)
add_custom_command(
    COMMAND ${CMAKE_OBJCOPY} -Oihex $<TARGET_FILE:...>   # 生成 HEX 文件
    COMMAND ${CMAKE_OBJCOPY} -Obinary ...                # 生成 BIN 文件
    )
```

(1) 生成 ELF 可执行文件
并链接自定义的 `AHRS.lib`(姿态解算库)
(2) 通过 `objcopy` 生成 HEX 和 BIN 文件
用于烧录到芯片


### 13.1.4 实验例程

修改 CMake 文件与 CMake 母版
管理好自己的工程
添加 User 文件夹并实现编译和烧录

```plaintext
include_directories()
```

tips: 记得修改后重新点击左上角 文件 → 重新加载 CMake


## 13.2 CMake 进阶: Modern CMake

现代 CMake 是 CMake 工具链的演进版本和最佳实践集合
强调更结构化, 模块化和目标 (Target) 导向的配置方式
二者之间的关系可以理解为
CMake 是基础工具
现代 CMake 是基于 CMake 的改进方法论
旨在解决传统 CMake 的痛点并提升项目的可维护性


### 13.2.1 现代 CMake 的核心原则


#### 13.2.1.1 以目标 (Target) 为中心

每个库或可执行文件定义为一个独立目标
显式声明其属性, 如头文件路径, 编译选项, 依赖关系

```cmake
add_library(math STATIC math.cpp)
target_include_directories(math PUBLIC include)  # 头文件路径仅影响 math 目标
target_link_libraries(math PUBLIC Eigen3::Eigen) # 依赖通过目标传递
```

以 ROS 为例, 简述现代 CMake 和 CMake 的区别


#### 13.2.1.2 避免全局命令

禁用 `include_directories()`, `link_directories()` 等全局命令
改用目标级命令, 防止污染其他模块

```cmake
# 传统方式（不推荐）
include_directories(include)  # 所有目标都会添加此路径
# 现代方式（推荐）
target_include_directories(my_target PUBLIC include)
```


#### 13.2.1.3 显式依赖传递

使用 `PUBLIC`, `PRIVATE`, `INTERFACE` 关键字控制依赖的传播范围
(1) `PUBLIC`: 依赖传递给使用者, 如头文件依赖
(2) `PRIVATE`: 仅本目标使用, 如实现细节
(3) `INTERFACE`: 仅使用者需要, 如纯头文件库

[点拨] `PRIVATE` 与 `PUBLIC` 的差别体现在谁最终拿到这条依赖上
`target_link_libraries(app PRIVATE foo)` 只有 `app` 自己链接 `foo`
写成 `PUBLIC` 时
任何 `target_link_libraries(bar ... app)` 的目标都会连带链接 `foo`
并继承 `foo` 的 `INTERFACE` 头文件路径
所以对外暴露的公共头文件里若 `#include` 了某个库的头文件
该库的链接必须是 `PUBLIC`
否则使用者编译期找不到头文件


#### 13.2.1.4 包管理的现代实践

优先使用 `find_package()` 的现代模式, 支持导入目标
而非手动指定路径

```cmake
find_package(Eigen3 REQUIRED)
# 传统方式（不推荐）
include_directories(${EIGEN3_INCLUDE_DIRS})
# 现代方式（推荐）
target_link_libraries(my_target Eigen3::Eigen)
```


### 13.2.2 以 ROS 工程为例

一个典型的 ROS 工程如下


#### 13.2.2.1 模块化与目标 (Target) 导向的依赖管理

ROS 工程通常由多个功能包 (Package) 组成
每个包负责独立的功能, 如传感器驱动, 导航算法等
现代 CMake 的目标中心化配置完美契合这种模块化需求
每个 ROS 包的 `CMakeLists.txt`
通过 `add_library` 或 `add_executable` 定义自己的目标
目标可以是库, 也可以是可执行节点
并通过 `target_link_libraries` 声明依赖

```cmake
# 示例：定义一个ROS节点目标
add_executable(talker src/talker.cpp)
target_link_libraries(talker
    ${catkin_LIBRARIES}  # ROS核心库
    other_dependency     # 其他依赖
)
```


#### 13.2.2.2 自动化处理 ROS 消息与服务生成

ROS 中自定义的消息 (`.msg`), 服务 (`.srv`)
动作 (`.action`) 需要生成对应的 C++/Python 代码
现代 CMake 通过自定义命令 (`add_custom_command`)
和生成器表达式高效实现

```cmake
# 生成消息和服务代码
generate_messages(
    DEPENDENCIES
    std_msgs  # 依赖的标准消息类型
)

# 将生成的头文件路径添加到目标
target_include_directories(my_node
    PRIVATE
    ${CATKIN_DEVEL_PREFIX}/include
)
```


#### 13.2.2.3 跨平台与工具链兼容性

ROS 需支持 Linux (主平台), Windows (通过 ROS2) 和嵌入式系统
现代 CMake 的工具链文件 (Toolchain File)
和条件编译简化跨平台配置


#### 13.2.2.4 依赖查找与包管理集成

ROS 依赖大量第三方库, 如 OpenCV, Boost, PCL
现代 CMake 的 `find_package` 和 `ament_cmake` (ROS2)
或 `catkin` (ROS1) 深度集成

```cmake
# ROS1中查找OpenCV
find_package(OpenCV REQUIRED)
target_link_libraries(my_node ${OpenCV_LIBRARIES})

# ROS2中使用ament_cmake
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
target_link_libraries(my_node rclcpp::rclcpp)
```


#### 13.2.2.5 再谈编译原理


### 13.2.3 现代 CMake 语法和规范

Modern CMake 源文档

https://modern-cmake-cn.github.io/Modern-CMake-zh_CN/

鼓励大家通过看文档学习一些先进知识或工具


### 13.2.4 实验例程


#### 13.2.4.1 将 CubeMX 自动生成的 CMake 改写为现代 CMake

```cmake
# --------------------------------
# 现代 CMake 核心配置
# --------------------------------
cmake_minimum_required(VERSION 3.23)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)  # 生成编译命令数据库（支持IDE分析）

# --------------------------------
# 1. 交叉编译工具链配置（推荐分离到独立工具链文件）
# --------------------------------
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR cortex-m4)  # 明确指定处理器架构

# 编译器配置
set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER arm-none-eabi-g++)
set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)
set(CMAKE_AR arm-none-eabi-ar)
set(CMAKE_OBJCOPY arm-none-eabi-objcopy)
set(CMAKE_OBJDUMP arm-none-eabi-objdump)
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)

# --------------------------------
# 2. 项目定义与目标分离
# --------------------------------
project(STM32F407IGH6TR_board
        VERSION 1.0.0
        LANGUAGES C CXX ASM
)

# 创建可执行目标（核心目标）
add_executable(${PROJECT_NAME}.elf)

# --------------------------------
# 3. 目标属性配置（避免全局污染）
# --------------------------------

# 标准配置
target_compile_features(${PROJECT_NAME}.elf
        PRIVATE
        c_std_11
        cxx_std_17
)

# 硬件浮点配置
target_compile_definitions(${PROJECT_NAME}.elf
        PRIVATE
        ARM_MATH_CM4
        ARM_MATH_MATRIX_CHECK
        ARM_MATH_ROUNDING
        __FPU_USED=1U
        __FPU_PRESENT=1U
        USE_HAL_DRIVER
        STM32F407xx
        DEBUG
)

target_compile_options(${PROJECT_NAME}.elf
        PRIVATE
        -mcpu=cortex-m4
        -mthumb
        -mthumb-interwork
        -mfloat-abi=hard
        -mfpu=fpv4-sp-d16
        -ffunction-sections
        -fdata-sections
        -fno-common
        -fmessage-length=0
)

# 汇编预处理配置
target_compile_options(${PROJECT_NAME}.elf
        PRIVATE
        $<$<COMPILE_LANGUAGE:ASM>:-xassembler-with-cpp>
)

# 链接选项
target_link_options(${PROJECT_NAME}.elf
        PRIVATE
        -Wl,-gc-sections
        -Wl,--print-memory-usage
        -Wl,-Map=${PROJECT_BINARY_DIR}/${PROJECT_NAME}.map
        -mcpu=cortex-m4
        -mthumb
        -mthumb-interwork
        -mfloat-abi=hard
        -mfpu=fpv4-sp-d16
        -T${CMAKE_CURRENT_SOURCE_DIR}/STM32F407IGHX_FLASH.ld
)

# --------------------------------
# 4. 模块化头文件管理
# --------------------------------
target_include_directories(${PROJECT_NAME}.elf
        PUBLIC
        Core/Inc Drivers/STM32F4xx_HAL_Driver/Inc Drivers/STM32F4xx_HAL_Driver/Inc/Legacy Drivers/CMSIS/Device/ST/STM32F4xx/Include Drivers/CMSIS/Include Middlewares/Third_Party/FreeRTOS/Source/include Middlewares/Third_Party/FreeRTOS/Source/CMSIS_RTOS Middlewares/Third_Party/FreeRTOS/Source/portable/GCC/ARM_CM4F Middlewares/ST/ARM/DSP/Inc USB_DEVICE/App USB_DEVICE/Target Middlewares/ST/STM32_USB_Device_Library/Core/Inc Middlewares/ST/STM32_USB_Device_Library/Class/CDC/Inc
        # ... (其他路径按相同模式添加)
)

# --------------------------------
# 5. 构建类型优化配置
# --------------------------------
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug)  # 设置默认构建类型
endif()

string(TOUPPER "${CMAKE_BUILD_TYPE}" BUILD_TYPE_UPPER)
set(OPTIMIZATION_FLAGS
        Debug       "-Og -g"
        Release     "-Ofast"
        RelWithDebInfo "-Ofast -g"
        MinSizeRel  "-Os"
)
target_compile_options(${PROJECT_NAME}.elf
        PRIVATE
        ${${BUILD_TYPE_UPPER}_OPTIMIZATION_FLAGS}
)

# --------------------------------
# 6. 源文件管理（推荐显式列出，此处保留 GLOB 需谨慎）
# --------------------------------
file(GLOB_RECURSE PROJECT_SOURCES
        "Core/*.*"
        "Core/*.*"
        "Core/*.*"
        "Drivers/*.*"
        "Middlewares/*.*"
        "User/*.*"
        "USB_DEVICE/*.*"
        "PID_stm32/*.*"
)

target_sources(${PROJECT_NAME}.elf
        PRIVATE
        ${PROJECT_SOURCES}
        ${CMAKE_CURRENT_SOURCE_DIR}/STM32F407IGHX_FLASH.ld
)

# --------------------------------
# 7. 依赖库管理
# --------------------------------
target_link_directories(${PROJECT_NAME}.elf
        PRIVATE
        ${PROJECT_SOURCE_DIR}/Middlewares/ST/ARM/DSP/Lib
)

target_link_libraries(${PROJECT_NAME}.elf
        PRIVATE
        arm_cortexM4lf_math
        #${PROJECT_SOURCE_DIR}/User/Framework/IMU/algorithm/AHRS.lib
)

# --------------------------------
# 8. 后处理命令（生成 HEX/BIN）
# --------------------------------
add_custom_command(TARGET ${PROJECT_NAME}.elf POST_BUILD
        COMMAND ${CMAKE_OBJCOPY} -Oihex $<TARGET_FILE:${PROJECT_NAME}.elf> ${PROJECT_BINARY_DIR}/${PROJECT_NAME}.hex
        COMMAND ${CMAKE_OBJCOPY} -Obinary $<TARGET_FILE:${PROJECT_NAME}.elf> ${PROJECT_BINARY_DIR}/${PROJECT_NAME}.bin
        COMMENT "Generating HEX and BIN files"
        VERBATIM
)
```

[点拨] 上面第 1 段应整体搬进独立的 `toolchain.cmake`
包括 `CMAKE_SYSTEM_NAME`, 各 `CMAKE_*_COMPILER`
以及 `CMAKE_TRY_COMPILE_TARGET_TYPE`
配置时用 `cmake -DCMAKE_TOOLCHAIN_FILE=toolchain.cmake` 引入
加 `-G Ninja -B build`
这样同一份 `CMakeLists.txt` 既能给 `arm-none-eabi` 用
也能在主机上做单元测试
注意 `CMAKE_TOOLCHAIN_FILE` 只在首次配置时读取
即 build 目录为空的时候
改了工具链文件必须先删 `build/` 再配
`CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY` 的作用
是让编译器探测阶段不去链接可执行文件
否则会因缺少启动文件或链接脚本而报错
报错信息如下
"compiler is not able to compile a simple test program"


#### 13.2.4.2 将自己写的算法编译成静态库

1. 为什么需要编译成库文件

Linux 下静态库为 `.a` 文件, 动态库为 `.so` 文件
Windows 下静态库为 `.lib` 文件
动态库的导入库文件为 `.lib` 文件, 动态库为 `.dll` 文件
MCU 中为 `.a` 文件

(1) 功能封装: 将常用算法, 工具函数或模块编译成库
可以在不同项目中重复使用, 避免重复编写相同代码
(2) 模块化设计: 大型项目可以拆分为多个库
每个团队独立开发和维护自己的库
通过接口 (头文件) 协作, 降低代码耦合
(3) 实际开发中的优势: 修改库代码后只需重新编译库本身
依赖库的项目无需重新编译
分发库时只需提供头文件和库文件, 保护源代码
不同团队通过接口 (头文件) 和库文件协作, 无需共享源码

2. 静态库和动态库的区别和选择

静态库和动态库是两种不同的代码共享方式
它们在链接方式, 文件管理, 内存占用等方面存在显著区别

(1) 静态库 (Static Library)
1. 编译时链接: 代码在编译时被完整复制到可执行文件中
2. 文件扩展名: Windows 下为 `.lib`, Linux/macOS 下为 `.a`
3. MCU 系统中为 `.a`, 且只能使用静态库
4. 文件体积大: 可执行文件包含所有静态库代码
5. 内存占用高: 多个程序使用同一静态库时
每个程序都会加载一份独立的副本
6. 无运行时依赖: 可执行文件独立运行
不一定需要外部库文件, 但在 gcc 编译环境中需要
7. 适用场景: 嵌入式系统, 单文件分发
8. 更新需重新编译: 修改静态库后
所有依赖它的程序必须重新编译
9. 启动速度快: 符号在编译时解析, 无运行时加载开销

(2) 动态库 (Dynamic Library)
1. 运行时链接: 代码在程序运行时动态加载到内存中
2. 文件扩展名: Windows 下为 `.dll`, Linux/macOS 下为 `.so`
macOS 下还可为 `.dylib`
3. 文件体积小: 可执行文件仅包含对动态库的引用
4. 内存占用低: 同一动态库可被多个程序共享
内存中只需加载一次
5. 需运行时依赖: 必须确保动态库文件存在且版本兼容
6. 适用场景: 操作系统核心库, 如 `OpenGL`, 插件化架构
7. 热更新支持: 替换动态库文件即可生效
无需重新编译主程序, 需接口兼容
8. 启动稍慢: 运行时需加载库并解析符号
但首次加载后后续调用无额外开销
9. 动态库的导入库 (Import Library): Windows 下为 `.lib`
与静态库同名, 但内容不同
Linux 下为 `.so`
在 Windows 中编译时需要 `.lib` 文件
用来声明动态库的导出函数和符号
链接器通过这些信息生成可执行文件
Linux 下不需要导入库, 直接通过 `.so` 文件链接

3. 实验例程: 假设算法结构如下

```plaintext
my_algorithm/
├── include/               # 头文件目录
│   └── my_algorithm.h     # 算法头文件
├── src/                   # 源文件目录
│   └── my_algorithm.cpp   # 算法实现
└── CMakeLists.txt         # CMake配置文件
```

在项目根目录下创建 `CMakeLists.txt`, 内容如下, 注意使用的是 F407

```cmake
cmake_minimum_required(VERSION 3.20)

# 设置库类型（静态库或动态库）
option(BUILD_SHARED_LIBS "Build shared libraries" OFF)  # 默认为静态库

# 包含头文件目录
include_directories(include)

**#以下部分与工程源CMake文件相同，目的是为了保持编译的一致性，防止出现编译规则不一致的情况**
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR cortex-m4)  # 明确指定处理器架构

# 编译器配置
set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER arm-none-eabi-g++)
set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)
set(CMAKE_AR arm-none-eabi-ar)
set(CMAKE_OBJCOPY arm-none-eabi-objcopy)
set(CMAKE_OBJDUMP arm-none-eabi-objdump)
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)

#这里为了防止gcc识别为simple test project
project(ToGetLibrary
        VERSION 1.0.0
        LANGUAGES C CXX ASM
)

*# 定义库名称变量*
set(LIB_NAME "my_algorithm")

# 添加库目标
add_library(${LIB_NAME}
    STATIC
    src/my_algorithm.cpp   # 指定源文件
)
#下面 target部分改成 ${LIB_NAME}指定该文件编译选项
# 标准配置
target_compile_features(${LIB_NAME}
        PRIVATE
        c_std_11
        cxx_std_17)

# 硬件浮点配置
target_compile_definitions(${LIB_NAME}
        PRIVATE
        ARM_MATH_CM4
        ARM_MATH_MATRIX_CHECK
        ARM_MATH_ROUNDING
        __FPU_USED=1U
        __FPU_PRESENT=1U
        USE_HAL_DRIVER
        STM32F407xx
        DEBUG)

target_compile_options(${LIB_NAME}
        PRIVATE
        -mcpu=cortex-m4
        -mthumb
        -mthumb-interwork
        -mfloat-abi=hard
        -mfpu=fpv4-sp-d16
        -ffunction-sections
        -fdata-sections
        -fno-common
        -fmessage-length=0)

# 汇编预处理配置
target_compile_options(${LIB_NAME}
        PRIVATE
        $<$<COMPILE_LANGUAGE:ASM>:-xassembler-with-cpp>)

# 链接选项
target_link_options(${LIB_NAME}
        PRIVATE
        -Wl,-gc-sections
        -Wl,--print-memory-usage
        -Wl,-Map=${PROJECT_BINARY_DIR}/${PROJECT_NAME}.map
        -mcpu=cortex-m4
        -mthumb
        -mthumb-interwork
        -mfloat-abi=hard
        -mfpu=fpv4-sp-d16
        -T${CMAKE_CURRENT_SOURCE_DIR}/STM32F407IGHX_FLASH.ld)

# 可选：安装规则（库）
install(TARGETS ${LIB_NAME}
    ARCHIVE DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/include     # 静态库安装路径
    ~~LIBRARY DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/include     # 动态库安装路径~~
~~    RUNTIME DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/include     # Windows动态库（DLL）安装路径~~
)

# 可选：安装规则(头文件)
install(
    FILES my_algorithm.h
    DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/include
)
```

生成和编译库
在算法所在文件夹 `my_algorithm` 下用命令行编译

```bash
# 创建构建目录
mkdir build && cd build

# 生成构建系统（默认生成静态库）
# 这里前提是ninja、gcc、g++都添加到环境变量中
cmake "-DCMAKE_MAKE_PROGRAM=ninja.exe" "-DCMAKE_C_COMPILER=arm-none-eabi-gcc.exe" "-DCMAKE_CXX_COMPILER=arm-none-eabi-g++.exe" -G Ninja -S ..

# 编译并安装
cmake --build . --target install
```

最后, 输出到 `include` 文件夹的文件即为我们调用时需要的库 (`.a`) 文件和头文件
删除 `build` 和源文件即可在原来的工程中使用你的算法了

使用生成的库
在需要调用该库的项目中, 配置如下

```cmake
*# 查找并链接库*
find_package(MyAlgorithm REQUIRED)
add_executable(my_app main.cpp)
target_link_libraries(my_app PRIVATE my_algorithm)
```

手动指定库路径, 如果未安装到系统目录

```cmake
# 手动指定头文件和库路径
~~target_include_directories(my_app PRIVATE /path/to/my_algorithm/include)~~
~~target_link_directories(my_app PRIVATE /path/to/my_algorithm/lib)~~
target_link_libraries(my_app PRIVATE my_algorithm)
```

[点拨] `find_package(MyAlgorithm REQUIRED)` 只在一种情况下成功
即 CMake 能找到 `MyAlgorithmConfig.cmake`
或找到 `myalgorithm-config.cmake`
光有 `.a` 加 `.h` 是找不到的
所以实际项目里通常仍用最后那段手动指定路径
或自己写一个 `install(EXPORT ...)`
加 `MyAlgorithmConfig.cmake.in` 的包配置
另外原文代码块里残留的飞书加粗标记
即两个星号包裹的文字
以及飞书删除线标记, 即两个波浪线包裹的文字
它们是文档排版标记, 并非 CMake 语法
复制到工程中必须去掉
否则 CMake 解析报错
