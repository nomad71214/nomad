# Riemann 积分的定义

- [知识点](#知识点)
- [Riemann 积分定义的实际来源](#Riemann%20积分定义的实际来源)
  - [曲边扇形的面积](#曲边扇形的面积)
  - [建模的适用范围](#建模的适用范围)
- [Riemann 积分的定义](#Riemann%20积分的定义)
  - [部分和与可积性](#部分和与可积性)
  - [Cauchy 叙述与 Heine 叙述](#Cauchy%20叙述与%20Heine%20叙述)
  - [Cauchy 收敛原理](#Cauchy%20收敛原理)
  - [三种叙述的等价性](#三种叙述的等价性)
- [Riemann 积分的基本分析性质](#Riemann%20积分的基本分析性质)
  - [有界性](#有界性)
  - [阿基米得的困惑](#阿基米得的困惑)
  - [改变有限个点不影响积分](#改变有限个点不影响积分)
- [建立方式](#建立方式)

## 知识点

闭区间上 Riemann 积分的实际来源与数学定义
核心是分割, 选取, 求和, 求极限四要素
部分和极限有 Cauchy 叙述, Heine 叙述与 Cauchy 收敛原理
三者等价, 且与函数极限的三种刻画完全平行
基本分析性质为可积必有界, 以及局部改变不影响整体
有界性只是必要条件, 改变有限个点不改变积分值

## Riemann 积分定义的实际来源

### 曲边扇形的面积

引例为曲边扇形的面积
设曲线由极坐标 $R=R(\theta)$ 给出
它与两条射线 $\theta=\theta_a$ 与 $\theta=\theta_b$ 围成曲边扇形
求此面积的基本想法分为四步

![图13-1]()

(1) 分割

按角度对曲边扇形作划分, 即对区间 $[\theta_a,\theta_b]$ 作分割
$$P:\theta_a=\theta_0<\theta_1<\cdots<\theta_{i-1}<\theta_i<\cdots<\theta_N=\theta_b$$
记 $\Delta\theta_i:=\theta_i-\theta_{i-1}$ 为第 $i$ 段的跨度
分割的模取为各段跨度的最大值
$$|P|:=\max_{1\leqslant i\leqslant N}\Delta\theta_i$$

(2) 选取

每一小块仍为曲边扇形, 考虑用规则的几何形状近似实际的形状
取 $\xi_i\in[\theta_{i-1},\theta_i]$, 以 $R(\xi_i)$ 为半径
以 $[\theta_{i-1},\theta_i]$ 为张角作规则扇形
作为第 $i$ 块面积的近似
$$S_i=\dfrac{1}{2}R^2(\xi_i)\Delta\theta_i$$

![图13-2]()

(3) 求和

累加各块近似值, 得部分和
$$\sigma\left(\dfrac{R^2(\theta)}{2},P,\xi\right):=\sum_{i=1}^{N}S_i=\sum_{i=1}^{N}\dfrac{1}{2}R^2(\xi_i)\Delta\theta_i$$
至此以部分和近似原曲边扇形的面积

(4) 求极限

希望定义在 $[\theta_a,\theta_b]$ 上的 $\dfrac{R^2(\theta)}{2}$ 具有行为
$$\exists S\in\mathbb{R},\ \forall\varepsilon>0,\ \exists\delta_\varepsilon>0,\ \left|\sigma\left(\dfrac{R^2(\theta)}{2},P,\xi\right)-S\right|<\varepsilon$$
$$\forall|P|<\delta_\varepsilon$$
上述行为不受限于对 $P$ 的选取 $\xi$, 即对任意选取都成立
它表明分割的模足够小时, 部分和将趋近一个固定的数
此固定的数即作为曲边扇形真实面积的计算

### 建模的适用范围

分割, 选取, 求和, 求极限的建模过程适用于诸多情形
如计算曲线的弧长, 旋转体的侧面积, 变力所做的功等
这些构成了 Riemann 积分定义的实际来源
就建模的结构而言, 可分为整体细分, 局部近似, 引入极限三部分

## Riemann 积分的定义

### 部分和与可积性

对函数 $f(x):[a,b]\ni x\mapsto f(x)\in\mathbb{R}$ 与分割
$$P:a=x_0<x_1<\cdots<x_N=b$$
记 $\Delta x_i:=x_i-x_{i-1}$ 与 $|P|:=\max\limits_{1\leqslant i\leqslant N}\Delta x_i$
取 $\xi_i\in[x_{i-1},x_i]$, 称
$$\sigma(f(x),P,\xi):=\sum_{i=1}^{N}f(\xi_i)\Delta x_i$$
为 $f(x)$ 关于分割 $P$ 与选取 $\xi$ 的部分和

### Cauchy 叙述与 Heine 叙述

如具有如下行为, 则称 $f(x)$ 在 $[a,b]$ 上 Riemann 可积
$$\exists S\in\mathbb{R},\ \forall\varepsilon>0,\ \exists\delta_\varepsilon>0,\ \left|\sigma(f(x),P,\xi)-S\right|<\varepsilon$$
$$\forall|P|<\delta_\varepsilon$$
此即 Riemann 积分的集聚刻画, 称为 Cauchy 叙述
此时记 $f(x)\in R[a,b]$, 并称部分和极限
$$\int_a^b f(x)\,dx$$
为 $f(x)$ 在 $[a,b]$ 上的定积分

Riemann 积分的序列刻画称为 Heine 叙述
$$\exists S\in\mathbb{R},\ \forall\{P_n\}_{n\in\mathbb{N}},\ |P_n|\to0,\ \sigma(f(x),P_n,\xi_n)\to S$$
式中 $\{\xi_n\}_{n\in\mathbb{N}}$ 为相对于分割族 $\{P_n\}_{n\in\mathbb{N}}$ 的任意选取族

与函数极限的 Cauchy 叙述与 Heine 叙述一样, 二者等价
故部分和极限可统一记为
$$\exists\lim\limits_{|P|\to0}\sigma(f(x),P,\xi)=S=:\int_a^b f(x)\,dx\in\mathbb{R}$$
此极限可按 Cauchy 叙述理解, 也可按 Heine 叙述理解

### Cauchy 收敛原理

部分和极限还有振幅刻画, 即对 $\forall\varepsilon>0$, $\exists\delta_\varepsilon>0$, 成立
$$\left|\sigma(f(x),\hat P,\hat\xi)-\sigma(f(x),\tilde P,\tilde\xi)\right|<\varepsilon$$
$$\forall|\hat P|,\ |\tilde P|<\delta_\varepsilon$$
此即 Cauchy 收敛原理
它与 Cauchy 叙述及 Heine 叙述等价, 是部分和极限的又一叙述形式

### 三种叙述的等价性

定理13-1 部分和极限与 Cauchy 收敛原理的等价性

如有 $\exists\lim\limits_{|P|\to0}\sigma(f(x),P,\xi)=S\in\mathbb{R}$
则 Cauchy 收敛原理成立, 反之亦然

证明 (1) 设部分和极限为 $S$, 按 Cauchy 叙述
对 $\forall\varepsilon>0$, $\exists\delta_\varepsilon>0$, 成立
$$\left|\sigma(f(x),P,\xi)-S\right|<\varepsilon,\quad\forall|P|<\delta_\varepsilon$$
分别取 $P=\hat P$ 与 $P=\tilde P$, 有
$$\left|\sigma(f(x),\hat P,\hat\xi)-S\right|<\varepsilon,\quad\left|\sigma(f(x),\tilde P,\tilde\xi)-S\right|<\varepsilon$$
按三角不等式即得
$$\left|\sigma(f(x),\hat P,\hat\xi)-\sigma(f(x),\tilde P,\tilde\xi)\right|<2\varepsilon$$
$$\forall|\hat P|,\ |\tilde P|<\delta_\varepsilon$$
即为 Cauchy 收敛原理的叙述

(2) 设已有 Cauchy 收敛原理
对 $\forall\{P_n\}$ 满足 $|P_n|\to0$, 数列 $\{\sigma(f(x),P_n,\hat\xi_n)\}$ 为基本数列
同样 $\{\sigma(f(x),P_n,\tilde\xi_n)\}$ 亦为基本数列
按数列极限的 Cauchy 收敛原理有
$$\sigma(f(x),P_n,\hat\xi_n)\to\hat S,\quad\sigma(f(x),P_n,\tilde\xi_n)\to\tilde S$$
以下证明 $\hat S=\tilde S$
作混合选取
$$\xi_n:=\begin{cases}\hat\xi_{2k},&n=2k\\ \tilde\xi_{2k-1},&n=2k-1\end{cases}$$
则 $\sigma(f(x),P_n,\xi_n)\to S$, 考虑其偶子列与奇子列
$$\sigma(f(x),P_{2k},\hat\xi_{2k})\to S=\hat S,\quad\sigma(f(x),P_{2k-1},\tilde\xi_{2k-1})\to S=\tilde S$$
故 $\hat S=\tilde S=S$
上述讨论说明, 对 $\forall|\hat P_n|\to0$ 有 $\sigma(f(x),\hat P_n,\xi_n)\to\hat S$
且 $\hat S$ 不依赖于选取
对 $\{\tilde P_n\}$ 同理有 $\sigma(f(x),\tilde P_n,\xi_n)\to\tilde S$, 且 $\tilde S$ 不依赖于选取

再交错取分割列
$$P_n=\begin{cases}\hat P_{2k},&n=2k\\ \tilde P_{2k-1},&n=2k-1\end{cases}$$
易见 $|P_n|\to0$, 故 $\sigma(f(x),P_n,\xi_n)\to S$
比较偶子列与奇子列即可得 $\hat S=\tilde S=S$

综上, Cauchy 叙述, Heine 叙述与 Cauchy 收敛原理三者等价
部分和的集聚刻画, 序列刻画与振幅刻画, 与函数极限完全一致
此等价性是一种通识性结构, 反映极限行为的本质

## Riemann 积分的基本分析性质

### 有界性

有界性是 Riemann 可积的必要条件, 但非充分
即如有 $f(x)\in R[a,b]$, 则 $f(x)$ 在 $[a,b]$ 上有界
反之, $[a,b]$ 上的有界函数不一定 Riemann 可积
此结论的证明在后续章节给出

### 阿基米得的困惑

考虑计算一块土地的面积
因灌溉之需在某些位置 $c_j$ 上开有水渠, 其中 $1\leqslant j\leqslant l$
设水渠足够狭窄, 近似面积按 $f(x)-g(x)$ 计算
$$\sigma((f-g)(x),P,\xi)=\sum_{i=1}^{N}(f-g)(\xi_i)\Delta x_i$$
设 $c_j\in[x_{k-1},x_k]$, 则一个子区间至多含一个 $c_j$
对该子区间有
$$S_k=(f-g)(\xi_k)\Delta x_k=\begin{cases}(f-g)(\xi_k)\Delta x_k\ne0,&\xi_k\ne c_j\\ 0,&\xi_k=c_j\end{cases}$$
从近似角度看, 是否计及水渠的面积似乎对近似值影响很大
此困惑在极限观点下得以解决
对含有水渠的闭子区间, 计及与否都有相同的极限值

![图13-3]()

### 改变有限个点不影响积分

定理13-2 改变有限个点不影响 Riemann 积分

设 $f(x)\in R[a,b]$, 且
$$\hat f(x)=\begin{cases}f(x),&x\ne x^\ast\\ C^\ast,&x=x^\ast\end{cases}$$
则 $\hat f(x)$ 在 $[a,b]$ 上 Riemann 可积, 且
$$\lim\limits_{|P|\to0}\sigma(\hat f(x),P,\xi)=\int_a^b f(x)\,dx$$

证明 由 $f(x)\in R[a,b]$ 有 $f(x)$ 在 $[a,b]$ 上有界
由此易见 $\hat f(x)$ 在 $[a,b]$ 上有界
作估计
$$\left|\sigma(\hat f(x),P,\xi)-\int_a^b f(x)\,dx\right|\leqslant\left|\sigma(\hat f(x),P,\xi)-\sigma(f(x),P,\xi)\right|+\left|\sigma(f(x),P,\xi)-\int_a^b f(x)\,dx\right|$$
按 Cauchy 叙述, 对 $\forall\varepsilon>0$, $\exists\delta_\varepsilon>0$, 成立
$$\left|\sigma(f(x),P,\xi)-\int_a^b f(x)\,dx\right|<\varepsilon,\quad\forall|P|<\delta_\varepsilon$$
设 $x^\ast\in[x_{k-1},x_k]$, 其余子区间上 $\hat f$ 与 $f$ 相等, 故
$$\sigma(\hat f(x),P,\xi)-\sigma(f(x),P,\xi)=\left[\hat f(\xi_k)-f(\xi_k)\right]\Delta x_k$$
于是
$$\left|\sigma(\hat f(x),P,\xi)-\sigma(f(x),P,\xi)\right|\leqslant2\max\left\{\sup_{[a,b]}|f(x)|,|C^\ast|\right\}|P|$$
记 $M:=2\max\left\{\sup\limits_{[a,b]}|f(x)|,|C^\ast|\right\}$
取 $|P|<\min\{\delta_\varepsilon,\varepsilon/M\}$, 即有
$$\left|\sigma(\hat f(x),P,\xi)-\int_a^b f(x)\,dx\right|<2\varepsilon$$
由 $\varepsilon$ 的任意性即得所证

上述结论只考虑了一个点, 对有限个点上的改变仍成立
可以逐点考虑, 也可直接估计
此时差项满足
$$\left|\sigma(\hat f(x),P,\xi)-\sigma(f(x),P,\xi)\right|\leqslant2l\max\left\{\sup_{[a,b]}|f(x)|,|C^\ast|\right\}|P|$$
在微积分层面只处理有限离散的间断
进一步的讨论属于测度意义下的间断

## 建立方式

(1) 数学是认识自然及非自然世界的系统思想与方法, 而不只是逻辑过程
教学需要三个过程, 先从实践对象提炼数学定义
再通过逻辑研究定义, 获得性质与定理
最后将结论反馈于实际对象, 以获得更新或更深入的认识
三者对应数学建模, 数学分析, 指导实际, 亦可称为数学实验
Riemann 积分的实际来源即分割, 选取, 求和, 求极限的建模过程

(2) 积分概念的引入往往基于闭区间上曲边梯形的面积
这里改以平面曲边扇形的面积作为研究对象
以消除建模过程仅限于曲边梯形面积计算的误解
该建模过程在力学, 物理学等学科中都有广泛背景

(3) Riemann 积分的本质是部分和极限, 即部分和的一种逼近行为
对其认识有 Cauchy 叙述, Heine 叙述与 Cauchy 收敛原理, 三者等价
所涉及的思想与方法完全类比于函数极限的分析
故可作为温故而知新的机会

(4) 以阿基米得的困惑作为初步体会
将问题的解决提炼为 Riemann 积分的性质并加以证明
以此展现 Riemann 积分的特质, 即局部改变不影响整体

(5) 有限个离散点上的改变不影响积分, 其处理属于微积分层面
更一般的间断需在测度意义下讨论