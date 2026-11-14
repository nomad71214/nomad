# Riemann 积分的应用

- [知识点](#知识点)
- [数学实验 实验结果可直接确认为真理](#数学实验%20实验结果可直接确认为真理)
- [数学实验 实验结果需经实践检验](#数学实验%20实验结果需经实践检验)
- [拓广深化](#拓广深化)
  - [力学中的相关应用](#力学中的相关应用)
  - [曲线上积分](#曲线上积分)
- [应用事例](#应用事例)
- [建立方式](#建立方式)

## 知识点

按实际背景建立数学模型, 是积分学处理几何量与力学量的基本方式
涉及平面曲边扇形与曲边梯形, 柱型体体积, 曲线弧长与旋成体侧面积
模型的建立一般包括分割, 选取, 求和与求极限四个过程
实际建立的和式与 Riemann 积分理论中的部分和不一定完全相同
前者可含子区间中的若干点, 后者仅含一个点
这一差别在求极限的过程中可被处理
真实值若可由 Darboux 小和与大和夹逼, 则结论可直接确认为真理
否则数学分析只能保证逻辑上的正确性, 是否反映真理须经实践检验
拓广深化将同一结构用于力学量的计算与曲线上的积分

## 数学实验 实验结果可直接确认为真理

平面曲边扇形与曲边梯形的面积, 柱型体的体积都属于此类
其真实值可由对应的 Darboux 小和与大和夹逼
按夹逼性即可获得确定性结论

设有曲线 $R=R(\theta)$, $\theta\in[\theta_a,\theta_b]$
它与两条射线 $\theta=\theta_a$ 与 $\theta=\theta_b$ 围成曲边扇形, 如图16-1

![图16-1]()

按分割, 选取, 求和与求极限的过程, 面积的计算方案为
$$S=\int_{\theta_a}^{\theta_b}\frac{1}{2}R^2(\theta)\,d\theta$$
相应的 Riemann 和为
$$\sigma\left(\frac{1}{2}R^2(\theta),P,\xi\right)=\sum_{i=1}^{N}\frac{1}{2}R^2(\xi_i)\Delta\theta_i$$
式中 $\xi_i\in[\theta_{i-1},\theta_i]$

定理16-1 曲边扇形与曲边梯形的面积
如 $R(\theta)\in R[\theta_a,\theta_b]$, 则曲边扇形的面积为
$$S_{\mathrm{real}}=\int_{\theta_a}^{\theta_b}\frac{1}{2}R^2(\theta)\,d\theta$$
如 $f(x)\in R[a,b]$, 则曲边梯形的面积为
$$S_{\mathrm{real}}=\int_a^b f(x)\,dx$$
曲边梯形如图16-2 所示

![图16-2]()

证明 对应分割 $P$, 每子块的真实面积 $S_{\mathrm{real},i}$ 满足
$$\left(\inf_{[\theta_{i-1},\theta_i]}\frac{1}{2}R^2(\theta)\right)\Delta\theta_i\leqslant S_{\mathrm{real},i}\leqslant\left(\sup_{[\theta_{i-1},\theta_i]}\frac{1}{2}R^2(\theta)\right)\Delta\theta_i$$
式中 $i=1,2,\cdots,N$
求和即有
$$L\left(\frac{1}{2}R^2(\theta),P\right)\leqslant\sum_{i=1}^{N}S_{\mathrm{real},i}=S_{\mathrm{real}}\leqslant U\left(\frac{1}{2}R^2(\theta),P\right)$$
由 $R(\theta)\in R[\theta_a,\theta_b]$ 可有 $\frac{1}{2}R^2(\theta)\in R[\theta_a,\theta_b]$
此时 Darboux 小和与大和有相同的极限
$$\lim_{|P|\to0}L\left(\frac{1}{2}R^2(\theta),P\right)=\lim_{|P|\to0}U\left(\frac{1}{2}R^2(\theta),P\right)=\int_{\theta_a}^{\theta_b}\frac{1}{2}R^2(\theta)\,d\theta$$
按夹逼性即得曲边扇形面积的确定性结论
曲边梯形的情形同理, 真实面积由 $f$ 的小和与大和夹逼

需指出, 上述确定性结论基于共同的数学结构
即真实值可由 Darboux 小和与大和控制
Riemann 可积时小和与大和具有相同的极限, 即为积分值
故根据夹逼性, 真实值必为 Riemann 积分值
这类数学实验的结论可直接确认为真理

柱形体指如下集合所表示的体积形态
$$\{(x,y,z)\mid(x,y)\in S(z),\ z\in[0,H]\}$$
即对每个 $z\in[0,H]$, $z$ 平面上的截面为 $S(z)\subset\mathbb{R}^2$
沿 $z$ 方向作分割
$$P:\ 0=z_0<z_1<\cdots<z_{i-1}<z_i<\cdots<z_N=H$$
体积的计算方案为
$$Vol=\int_0^H S(z)\,dz=\lim_{|P|\to0}\sum_{i=1}^{N}S(\xi_i)\Delta z_i$$
式中 $\xi_i\in[z_{i-1},z_i]$, $S(z)$ 既表示截面又表示其面积

定理16-2 柱型体的体积
如截面面积 $S(z)$ 在 $[0,H]$ 上 Riemann 可积, 则柱型体的体积为
$$Vol=\int_0^H S(z)\,dz$$
证明 设 $Vol_{\mathrm{real},i}$ 为 $z=z_{i-1}$ 与 $z=z_i$ 所截得的真实体积
有
$$L(S(z),P)\leqslant\sum_{i=1}^{N}Vol_{\mathrm{real},i}=Vol_{\mathrm{real}}\leqslant U(S(z),P)$$
由 $S(z)$ 可积, 小和与大和的极限同为积分值
按夹逼性即得所证

旋转体是柱型体的特例
如曲线 $y=y(x)\geqslant0$, $x\in[a,b]$ 绕 $x$ 轴旋转一周
则截面 $S(x)$ 为半径 $y(x)$ 的圆, 其面积为 $\pi y^2(x)$
按定理16-2 即得旋转体的体积
$$V=\int_a^b\pi y^2(x)\,dx$$

实际建立的和式与部分和不完全相同
前者可能含有参数域子区间中的若干点, 后者仅含有一个点
以下曲线弧长的讨论即给出这种和式
这一差别在求极限的过程中可被处理

## 数学实验 实验结果需经实践检验

曲线弧长与旋成体侧面积没有相应的 Darboux 小和与大和作控制
其计算方案只能保证数学分析上的正确性
是否为真理则须经实践检验
以下按曲线弧长, 旋成体侧面积与柱面面积分别讨论

设 $\mathbb{R}^3$ 中的曲线由向量值映照给出
$$r(t):[\alpha,\beta]\ni t\mapsto r(t)=\begin{pmatrix}x(t)\\y(t)\\z(t)\end{pmatrix}\in\mathbb{R}^3$$
在参数域 $[\alpha,\beta]$ 上作分割
$$P:\ \alpha=t_0<t_1<\cdots<t_{i-1}<t_i<\cdots<t_N=\beta$$
分割点所截的弧长仍无实际的计算方法, 故用直线段近似, 如图16-3

![图16-3]()

$$\Delta L_i=|r(t_i)-r(t_{i-1})|_{\mathbb{R}^3}=\left[(x(t_i)-x(t_{i-1}))^2+(y(t_i)-y(t_{i-1}))^2+(z(t_i)-z(t_{i-1}))^2\right]^{\frac{1}{2}}$$
按 Lagrange 中值定理, 部分和为
$$\sum_{i=1}^{N}\Delta L_i=\sum_{i=1}^{N}\sqrt{\dot{x}^2(\xi_i)+\dot{y}^2(\eta_i)+\dot{z}^2(\zeta_i)}\,\Delta t_i$$
式中 $\xi_i$, $\eta_i$, $\zeta_i\in(t_{i-1},t_i)$ 取值各不相同
这与原来的部分和选取有所不同
但极限仍可按 Cauchy 叙述与 Cauchy 收敛原理认识
为此引入条件
$$x(t)\in C[\alpha,\beta],\ \exists\dot{x}(t)\in\mathbb{R},\ \forall t\in(\alpha,\beta)$$
其余两个分量同理, 可记作 $r(t)\in C[\alpha,\beta]$ 与 $\exists\dot{r}(t)\in\mathbb{R}^3$
进一步要求 $\dot{r}(t)\in R[\alpha,\beta]$
即各分量在 $[\alpha,\beta]$ 上 Riemann 可积

猜测下述极限存在, 且等于弧长的积分
$$\lim_{|P|\to0}\sum_{i=1}^{N}\sqrt{\dot{x}^2(\xi_i)+\dot{y}^2(\eta_i)+\dot{z}^2(\zeta_i)}\,\Delta t_i=\int_\alpha^\beta\sqrt{\dot{x}^2(t)+\dot{y}^2(t)+\dot{z}^2(t)}\,dt$$
估计时须比较两个不同点处的被积函数, 为此引入如下引理

引理16-3 三元向量模差的估计
对 $\forall A$, $B$, $C$, $E$, $F$, $G\in\mathbb{R}$, 有
$$\left|\sqrt{A^2+B^2+C^2}-\sqrt{E^2+F^2+G^2}\right|\leqslant|A-E|+|B-F|+|C-G|$$
证明 分子有理化, 有
$$\left|\sqrt{A^2+B^2+C^2}-\sqrt{E^2+F^2+G^2}\right|=\frac{\left|A^2+B^2+C^2-E^2-F^2-G^2\right|}{\sqrt{A^2+B^2+C^2}+\sqrt{E^2+F^2+G^2}}$$
$$\leqslant\frac{|A+E||A-E|+|B+F||B-F|+|C+G||C-G|}{\sqrt{A^2+B^2+C^2}+\sqrt{E^2+F^2+G^2}}$$
注意 $|A+E|\leqslant|A|+|E|\leqslant\sqrt{A^2+B^2+C^2}+\sqrt{E^2+F^2+G^2}$
对三对分量均有同样的估计, 故三个系数都不超过 $1$
即得所需不等式

现将和式与积分之差分为两段
$$\left|\sum_{i=1}^{N}\sqrt{\dot{x}^2(\xi_i)+\dot{y}^2(\eta_i)+\dot{z}^2(\zeta_i)}\,\Delta t_i-\int_\alpha^\beta|\dot{r}(t)|_{\mathbb{R}^3}\,dt\right|$$
$$\leqslant\left|\sum_{i=1}^{N}\left[\sqrt{\dot{x}^2(\xi_i)+\dot{y}^2(\eta_i)+\dot{z}^2(\zeta_i)}-\sqrt{\dot{x}^2(\tau_i)+\dot{y}^2(\tau_i)+\dot{z}^2(\tau_i)}\right]\Delta t_i\right|$$
$$+\left|\sum_{i=1}^{N}\sqrt{\dot{x}^2(\tau_i)+\dot{y}^2(\tau_i)+\dot{z}^2(\tau_i)}\,\Delta t_i-\int_\alpha^\beta\sqrt{\dot{x}^2(t)+\dot{y}^2(t)+\dot{z}^2(t)}\,dt\right|$$
式中 $\tau_i\in[t_{i-1},t_i]$ 任意
右端第二项按 $\dot{r}(t)\in R[\alpha,\beta]$ 可小于 $\varepsilon$, 当 $|P|<\delta_\varepsilon$
右端第一项按引理16-3 有
$$\leqslant\sum_{i=1}^{N}\left[|\dot{x}(\xi_i)-\dot{x}(\tau_i)|+|\dot{y}(\eta_i)-\dot{y}(\tau_i)|+|\dot{z}(\zeta_i)-\dot{z}(\tau_i)|\right]\Delta t_i$$
$$\leqslant\omega(\dot{x}(t),P)+\omega(\dot{y}(t),P)+\omega(\dot{z}(t),P)$$
式中 $\omega(f(t),P)$ 表示 $f$ 在分割 $P$ 下的振幅和
按 Riemann 可积的等价刻画有
$$f\in R[\alpha,\beta]\iff\lim_{|P|\to0}\omega(f(t),P)=0$$
故第一项也趋于零, 所猜测的极限存在

综上, 当 $r(t)\in C[\alpha,\beta]$ 且 $\dot{r}(t)\in R[\alpha,\beta]$ 时, 曲线弧长为
$$L=\int_\alpha^\beta\sqrt{\dot{x}^2(t)+\dot{y}^2(t)+\dot{z}^2(t)}\,dt=\int_\alpha^\beta|\dot{r}(t)|_{\mathbb{R}^3}\,dt$$
需指出, 真实弧长没有被 Darboux 小和与大和所控制
故上述结论不能直接确认为真理, 必须经实践检验
经实践, 用折线逼近曲线弧长的方案是正确的

将曲线绕 $x$ 轴旋转一周形成旋转体, 现给出其侧面积的计算方案
针对局部侧面积的近似方法不同, 有两种方案, 如图16-4

![图16-4]()

方案一 局部侧面积用圆台侧面积近似, 如图16-5

![图16-5]()

按几何关系有
$$S_i=\frac{1}{2}(R_i^2-r_i^2)\theta_i=\frac{\theta_i}{2}(R_i+r_i)(R_i-r_i)=\pi(y_{i-1}+y_i)\sqrt{(x_i-x_{i-1})^2+(y_i-y_{i-1})^2}$$
按 Lagrange 中值定理有
$$x_i-x_{i-1}=\dot{x}(\xi_i)\Delta t_i,\quad y_i-y_{i-1}=\dot{y}(\eta_i)\Delta t_i$$
式中 $\xi_i$, $\eta_i\in(t_{i-1},t_i)$
对 $\forall\zeta_i\in(t_{i-1},t_i)$ 又有
$$y_{i-1}=y(\zeta_i)+\dot{y}(\alpha_i)(t_{i-1}-\zeta_i),\quad y_i=y(\zeta_i)+\dot{y}(\beta_i)(t_i-\zeta_i)$$
式中 $\alpha_i\in(t_{i-1},\zeta_i)$, $\beta_i\in(\zeta_i,t_i)$
由此可有
$$S_i=2\pi y(\zeta_i)\sqrt{\dot{x}^2(\xi_i)+\dot{y}^2(\eta_i)}\,\Delta t_i+\pi\dot{y}(\alpha_i)\sqrt{\dot{x}^2(\xi_i)+\dot{y}^2(\eta_i)}(t_{i-1}-\zeta_i)\Delta t_i$$
$$+\pi\dot{y}(\beta_i)\sqrt{\dot{x}^2(\xi_i)+\dot{y}^2(\eta_i)}(t_i-\zeta_i)\Delta t_i$$
借此易得估计
$$\left|\sum_{i=1}^{N}S_i-\sum_{i=1}^{N}2\pi y(\zeta_i)\sqrt{\dot{x}^2(\xi_i)+\dot{y}^2(\eta_i)}\,\Delta t_i\right|\leqslant2\pi\sup_{[\alpha,\beta]}|\dot{y}(t)|\left(\sup|\dot{x}|+\sup|\dot{y}|\right)(\beta-\alpha)|P|$$
上述估计利用基本关系式 $\sqrt{A^2+B^2}\leqslant|A|+|B|$
其前提为 $r(t)\in C[\alpha,\beta]$ 与 $\dot{r}(t)\in R[\alpha,\beta]$
进一步考虑
$$\left|\sum_{i=1}^{N}2\pi y(\zeta_i)\sqrt{\dot{x}^2(\xi_i)+\dot{y}^2(\eta_i)}\,\Delta t_i-\int_\alpha^\beta2\pi y(t)\sqrt{\dot{x}^2(t)+\dot{y}^2(t)}\,dt\right|$$
$$\leqslant\left|\sum_{i=1}^{N}2\pi y(\zeta_i)\left[\sqrt{\dot{x}^2(\xi_i)+\dot{y}^2(\eta_i)}-\sqrt{\dot{x}^2(\zeta_i)+\dot{y}^2(\zeta_i)}\right]\Delta t_i\right|$$
$$+\left|\sum_{i=1}^{N}2\pi y(\zeta_i)\sqrt{\dot{x}^2(\zeta_i)+\dot{y}^2(\zeta_i)}\,\Delta t_i-\int_\alpha^\beta2\pi y(t)\sqrt{\dot{x}^2(t)+\dot{y}^2(t)}\,dt\right|$$
右端第二项由可积性小于 $\varepsilon$, 当 $|P|<\delta_\varepsilon$
右端第一项按引理16-3 有
$$\leqslant2\pi\sup_{[\alpha,\beta]}|y(t)|\left[\omega(\dot{x}(t),P)+\omega(\dot{y}(t),P)\right]$$
综上, 按圆台侧面积近似, 当 $r(t)\in C[\alpha,\beta]$ 且 $\dot{r}(t)\in R[\alpha,\beta]$ 时有
$$S=\int_\alpha^\beta2\pi y(t)\sqrt{\dot{x}^2(t)+\dot{y}^2(t)}\,dt$$

方案二 局部侧面积用圆柱侧面积近似, 如图16-6

![图16-6]()

基于局部圆柱侧面积近似有
$$S_i=2\pi y(\xi_i)|\Delta x_i|=2\pi y(\xi_i)|x_i-x_{i-1}|=2\pi y(\xi_i)|\dot{x}(\eta_i)|\Delta t_i$$
考虑估计
$$\left|\sum_{i=1}^{N}S_i-\int_\alpha^\beta2\pi y(t)|\dot{x}(t)|\,dt\right|\leqslant\left|\sum_{i=1}^{N}2\pi y(\xi_i)\left[|\dot{x}(\eta_i)|-|\dot{x}(\xi_i)|\right]\Delta t_i\right|$$
$$+\left|\sum_{i=1}^{N}2\pi y(\xi_i)|\dot{x}(\xi_i)|\Delta t_i-\int_\alpha^\beta2\pi y(t)|\dot{x}(t)|\,dt\right|$$
第二项由可积性小于 $\varepsilon$, 当 $|P|<\delta_\varepsilon$
第一项有
$$\leqslant2\pi\sup_{[\alpha,\beta]}|y(t)|\sum_{i=1}^{N}\left||\dot{x}(\eta_i)|-|\dot{x}(\xi_i)|\right|\Delta t_i\leqslant2\pi\sup_{[\alpha,\beta]}|y(t)|\,\omega(\dot{x}(t),P)$$
故按圆柱侧面积近似有
$$S=\int_\alpha^\beta2\pi y(t)|\dot{x}(t)|\,dt$$

至此对旋转体的侧面积给出两种方案, 即
$$S=\int_\alpha^\beta2\pi y(t)\sqrt{\dot{x}^2(t)+\dot{y}^2(t)}\,dt,\quad S=\int_\alpha^\beta2\pi y(t)|\dot{x}(t)|\,dt$$
两方案的数学建模与数学分析过程均符合逻辑
然而经实践检验, 圆台方案的结论正确, 圆柱方案的结论错误
对此仅需考虑圆锥的侧面积即可鉴别

柱面可基于如下向量值映照刻画, 如图16-7

![图16-7]()

$$D_{tz}\ni\begin{pmatrix}t\\z\end{pmatrix}\mapsto\Sigma(t,z)=\begin{pmatrix}x(t)\\y(t)\\z\end{pmatrix}\in\mathbb{R}^3$$
式中 $t\in[\alpha,\beta]$, 而 $z$ 的范围由 $\varphi(t)$ 与 $\psi(t)$ 给出
考虑局部的面积近似
$$S_i=\sqrt{(x(t_i)-x(t_{i-1}))^2+(y(t_i)-y(t_{i-1}))^2}\,(\psi-\varphi)(\xi_i)$$
由此考虑
$$\lim_{|P|\to0}\sum_{i=1}^{N}S_i=\lim_{|P|\to0}\sum_{i=1}^{N}\sqrt{(x(t_i)-x(t_{i-1}))^2+(y(t_i)-y(t_{i-1}))^2}\,(\psi-\varphi)(\xi_i)$$
按 Lagrange 中值定理, 并特取 $\zeta_i=\xi_i$, 可估计
$$\left|\sum_{i=1}^{N}S_i-\int_\alpha^\beta\sqrt{\dot{x}^2(t)+\dot{y}^2(t)}\,(\psi-\varphi)(t)\,dt\right|\leqslant\left|\sum_{i=1}^{N}\left[\sqrt{\dot{x}^2(\alpha_i)+\dot{y}^2(\beta_i)}-\sqrt{\dot{x}^2(\xi_i)+\dot{y}^2(\xi_i)}\right](\psi-\varphi)(\xi_i)\Delta t_i\right|+\varepsilon$$
$$\leqslant\sup_{[\alpha,\beta]}|\psi-\varphi|(t)\left[\omega(\dot{x}(t),P)+\omega(\dot{y}(t),P)\right]+\varepsilon<\left[2\sup_{[\alpha,\beta]}|\psi-\varphi|(t)+1\right]\varepsilon$$
当
$$|P|<\min\left\{P_{\dot{x},\varepsilon},P_{\dot{y},\varepsilon}\right\}$$
式中
$$\omega(\dot{x}(t),P)<\varepsilon,\ \forall|P|<P_{\dot{x},\varepsilon};\quad\omega(\dot{y}(t),P)<\varepsilon,\ \forall|P|<P_{\dot{y},\varepsilon}$$
综上, 柱面的面积为
$$S=\int_\alpha^\beta\sqrt{\dot{x}^2(t)+\dot{y}^2(t)}\,(\psi-\varphi)(t)\,dt$$
该方案经实践检验可保证其正确性

## 拓广深化

### 力学中的相关应用

研究盛水旋成体容器所受的压力, 如图16-8

![图16-8]()

设容器壁由 $[\alpha,\beta]\ni t\mapsto r(t)=(x(t),y(t))\in\mathbb{R}^2$ 绕 $y$ 轴旋转而成
其单位切向与法向为
$$[\tau,n]=[i_1,i_2]\frac{1}{\sqrt{\dot{x}^2+\dot{y}^2}}\begin{pmatrix}\dot{x}&\dot{y}\\\dot{y}&-\dot{x}\end{pmatrix}(t)$$
局部压力的竖直分量为
$$\Delta F_{i,y}=-\left[p_a+\rho g(H-y(\xi_i))\right]2\pi x(\xi_i)\dot{x}(\xi_i)\Delta t_i$$
对所受的压力进行建模, 有
$$F_y=\lim_{|P|\to0}\sum_{i=1}^{N}\Delta F_{i,y}-\pi\rho g(H-y(\alpha))x^2(\alpha)$$
分析其中的极限
$$\lim_{|P|\to0}\sum_{i=1}^{N}\Delta F_{i,y}=-\lim_{|P|\to0}\sum_{i=1}^{N}\left[p_a+\rho g(H-y(\xi_i))\right]2\pi x(\xi_i)\dot{x}(\xi_i)\Delta t_i$$
$$=-\int_\alpha^\beta\left[p_a+\rho g(H-y(t))\right]2\pi x(t)\dot{x}(t)\,dt$$
$$=-2\pi p_a\int_\alpha^\beta x(t)\dot{x}(t)\,dt-2\pi\rho g\int_\alpha^\beta(H-y(t))x(t)\dot{x}(t)\,dt$$
故有
$$F_y=-p_a\pi\left(x^2(\beta)-x^2(\alpha)\right)-\rho g\int_\alpha^\beta\pi x^2(t)\,dy(t)$$
第一项代表旋成体容器上下底面的大气压 $p_a$ 所造成的压力
第二项代表容器中水的质量所造成的压力

研究坝体柱型表面所受的压力, 如图16-9

![图16-9]()

设 $[\alpha,\beta]\ni t\mapsto(x(t),y(t))\in\mathbb{R}^2$, 有
$$\tau(t)=\frac{1}{\sqrt{\dot{x}^2+\dot{y}^2}}\begin{pmatrix}\dot{x}\\\dot{y}\end{pmatrix}(t),\quad n=\tau(t)\times j=\frac{1}{\sqrt{\dot{x}^2+\dot{y}^2}}\begin{pmatrix}-\dot{y}\\\dot{x}\end{pmatrix}(t)$$
由此局部压力为
$$\Delta\mathbf{F}_i=-\left[p_a+\rho g(H-y(\xi_i))\right]\sqrt{(x(t_i)-x(t_{i-1}))^2+(y(t_i)-y(t_{i-1}))^2}L\,n$$
$$=L\left[p_a+\rho g(H-y(\xi_i))\right]\frac{\sqrt{\dot{x}^2(\alpha_i)+\dot{y}^2(\beta_i)}}{\sqrt{\dot{x}^2(\xi_i)+\dot{y}^2(\xi_i)}}\begin{pmatrix}\dot{y}\\-\dot{x}\end{pmatrix}(\xi_i)\Delta t_i$$
故有
$$\frac{F_x}{L}=\lim_{|P|\to0}\sum_{i=1}^{N}\left[p_a+\rho g(H-y(\xi_i))\right]\frac{\sqrt{\dot{x}^2(\alpha_i)+\dot{y}^2(\beta_i)}}{\sqrt{\dot{x}^2(\xi_i)+\dot{y}^2(\xi_i)}}\dot{y}(\xi_i)\Delta t_i$$
$$\frac{F_y}{L}=-\lim_{|P|\to0}\sum_{i=1}^{N}\left[p_a+\rho g(H-y(\xi_i))\right]\frac{\sqrt{\dot{x}^2(\alpha_i)+\dot{y}^2(\beta_i)}}{\sqrt{\dot{x}^2(\xi_i)+\dot{y}^2(\xi_i)}}\dot{x}(\xi_i)\Delta t_i$$
可有
$$\frac{F_x}{L}=\int_\alpha^\beta\left[p_a+\rho g(H-y(t))\right]\dot{y}(t)\,dt=p_aH+\frac{1}{2}\rho gH^2$$
$$\frac{F_y}{L}=-\int_\alpha^\beta\left[p_a+\rho g(H-y(t))\right]\dot{x}(t)\,dt=-\left[p_aW+\rho gS\right]$$
式中 $S$ 表示自由水面, 堤表面与 $x=W$ 所围的面积

### 曲线上积分

设 $f(x,y,z)$ 为定义在曲线 $\Gamma$ 上的线密度, 现要求曲线 $\Gamma$ 的质量
以下按分割, 选取, 求和与求极限四个步骤开展, 如图16-10

![图16-10]()

第一步 分割
在 $\Gamma(t)$ 的定义域 $[\alpha,\beta]$ 上引入分割
$$P_t:\ \alpha=t_0<t_1<\cdots<t_{i-1}<t_i<\cdots<t_N=\beta$$
由曲线 $\Gamma$ 的向量值映照, 对应物理区域上的分割为
$$P:\ \Gamma(\alpha)=\Gamma(t_0),\cdots,\Gamma(t_{i-1}),\Gamma(t_i),\cdots,\Gamma(t_N)=\Gamma(\beta)\in\mathbb{R}^3$$
第二步 选取
用折线段 $\Gamma(t_i)-\Gamma(t_{i-1})$ 替代 $\Gamma(t_{i-1})$ 与 $\Gamma(t_i)$ 之间的弧
并取 $f\circ\Gamma(\xi_i)$, $\xi_i\in[t_{i-1},t_i]$ 作为此段弧的等效线密度
$$m_i=f\circ\Gamma(\xi_i)\left|\Gamma(t_i)-\Gamma(t_{i-1})\right|_{\mathbb{R}^3}$$
第三步 求和
$$\sum_{i=1}^{N}m_i=\sum_{i=1}^{N}f\circ\Gamma(\xi_i)\left|\Gamma(t_i)-\Gamma(t_{i-1})\right|_{\mathbb{R}^3}$$
第四步 求极限
$$m=\lim_{|P_t|\to0}\sum_{i=1}^{N}m_i$$

性质16-4 第一类曲线积分
如 $f\circ\Gamma(t)\in R[\alpha,\beta]$ 且 $\frac{d\Gamma}{dt}(t)\in R[\alpha,\beta]$, 则有
$$\int_\Gamma f\,ds=\lim_{|P_t|\to0}\sum_{i=1}^{N}f\circ\Gamma(\xi_i)\left|\Gamma(t_i)-\Gamma(t_{i-1})\right|_{\mathbb{R}^3}=\int_\alpha^\beta f\circ\Gamma(t)\left|\frac{d\Gamma}{dt}(t)\right|_{\mathbb{R}^3}dt$$
证明 按 Lagrange 中值定理有
$$f\circ\Gamma(\xi_i)\left|\Gamma(t_i)-\Gamma(t_{i-1})\right|_{\mathbb{R}^3}=f\circ\Gamma(\xi_i)\sqrt{(x'(\alpha_i))^2+(y'(\beta_i))^2+(z'(\gamma_i))^2}\,\Delta t_i$$
式中 $\alpha_i$, $\beta_i$, $\gamma_i\in(t_{i-1},t_i)$
将和式与积分之差分为 $I_1$ 与 $I_2$ 两段, 有
$$\left|\sum_{i=1}^{N}f\circ\Gamma(\xi_i)\sqrt{(x'(\alpha_i))^2+(y'(\beta_i))^2+(z'(\gamma_i))^2}\,\Delta t_i-\int_\alpha^\beta f\circ\Gamma(t)\left|\frac{d\Gamma}{dt}(t)\right|dt\right|\leqslant I_1+I_2$$
其右端第二项满足
$$I_2<\varepsilon,\ \forall|P_t|<\delta_\varepsilon$$
考虑右端第一项
$$I_1\leqslant\sup_{[\alpha,\beta]}|f\circ\Gamma(t)|\sum_{i=1}^{N}\left[|x'(\alpha_i)-x'(\xi_i)|+|y'(\beta_i)-y'(\xi_i)|+|z'(\gamma_i)-z'(\xi_i)|\right]\Delta t_i$$
$$\leqslant\sup_{[\alpha,\beta]}|f\circ\Gamma(t)|\left[\omega(x'(t),P_t)+\omega(y'(t),P_t)+\omega(z'(t),P_t)\right]$$
由 $x'(t)$, $y'(t)$, $z'(t)\in R[\alpha,\beta]$ 知三个振幅和当 $|P_t|\to0$ 时均趋于零
由此得结论

以下考虑做功形式的曲线积分
设 $\mathbf{F}(x,y,z)$ 为定义在曲线上的力, 现要求力从曲线一端到另一端的做功
对局部作均匀化假设
(1) 以直线段 $\Gamma(t_i)-\Gamma(t_{i-1})$ 近似局部的路径
(2) 取 $\mathbf{F}\circ\Gamma(\xi_i)$ 作为整个局部路径上的力
则有
$$W_i=\mathbf{F}\circ\Gamma(\xi_i)\cdot\left(\Gamma(t_i)-\Gamma(t_{i-1})\right),\quad i=1,2,\cdots,N$$
$$\sum_{i=1}^{N}W_i=\sum_{i=1}^{N}\mathbf{F}\circ\Gamma(\xi_i)\cdot\left(\Gamma(t_i)-\Gamma(t_{i-1})\right)$$
取其极限形式为
$$\lim_{|P_t|\to0}\sum_{i=1}^{N}W_i=\lim_{|P_t|\to0}\sum_{i=1}^{N}\mathbf{F}\circ\Gamma(\xi_i)\cdot\left(\Gamma(t_i)-\Gamma(t_{i-1})\right)$$

性质16-5 第二类曲线积分
如 $\mathbf{F}\circ\Gamma(t)\in R[\alpha,\beta]$ 且 $\frac{d\Gamma}{dt}(t)\in R[\alpha,\beta]$, 则有
$$\int_\Gamma\mathbf{F}\cdot d\mathbf{r}=\lim_{|P_t|\to0}\sum_{i=1}^{N}\mathbf{F}\circ\Gamma(\xi_i)\cdot\left(\Gamma(t_i)-\Gamma(t_{i-1})\right)=\int_\alpha^\beta\mathbf{F}\circ\Gamma(t)\cdot\frac{d\Gamma}{dt}(t)\,dt$$
证明 按 Lagrange 中值定理有
$$\sum_{i=1}^{N}\mathbf{F}\circ\Gamma(\xi_i)\cdot\left(\Gamma(t_i)-\Gamma(t_{i-1})\right)=\sum_{i=1}^{N}\left[F_1(\Gamma(\xi_i))x'(\alpha_i)+F_2(\Gamma(\xi_i))y'(\beta_i)+F_3(\Gamma(\xi_i))z'(\gamma_i)\right]\Delta t_i$$
式中 $\alpha_i$, $\beta_i$, $\gamma_i\in(t_{i-1},t_i)$
将差分为 $I_1$ 与 $I_2$ 两段, 其中 $I_2<\varepsilon$, 当 $|P_t|<\delta_\varepsilon$
第一项有
$$I_1\leqslant\sup|F_1\circ\Gamma|\sum_{i=1}^{N}|x'(\alpha_i)-x'(\xi_i)|\Delta t_i+\sup|F_2\circ\Gamma|\sum_{i=1}^{N}|y'(\beta_i)-y'(\xi_i)|\Delta t_i$$
$$+\sup|F_3\circ\Gamma|\sum_{i=1}^{N}|z'(\gamma_i)-z'(\xi_i)|\Delta t_i$$
$$\leqslant\left[\sup_{[\alpha,\beta]}|F_1\circ\Gamma(t)|+\sup_{[\alpha,\beta]}|F_2\circ\Gamma(t)|+\sup_{[\alpha,\beta]}|F_3\circ\Gamma(t)|\right]\varepsilon$$
当 $|P_t|<\delta_\varepsilon$, 综上即得结论

## 应用事例

例16-1: 救生圈的表面积
救生圈可由图16-11 所示的曲线旋转而成, 其向量值映照为
$$r(\theta):[0,2\pi]\ni\theta\mapsto r(\theta)=\begin{pmatrix}x(\theta)\\y(\theta)\end{pmatrix}\triangleq\begin{pmatrix}R\cos\theta\\a+R\sin\theta\end{pmatrix}$$
故救生圈的表面积隶属旋成体的侧面积, 现求其值

![图16-11]()

解: 由 $x(\theta)=R\cos\theta$ 与 $y(\theta)=a+R\sin\theta$ 有
$$\dot{x}(\theta)=-R\sin\theta,\quad\dot{y}(\theta)=R\cos\theta,\quad\sqrt{\dot{x}^2(\theta)+\dot{y}^2(\theta)}=R$$
按旋成体侧面积的计算式有
$$S=\int_0^{2\pi}2\pi y(\theta)\sqrt{\dot{x}^2(\theta)+\dot{y}^2(\theta)}\,d\theta=\int_0^{2\pi}2\pi(a+R\sin\theta)R\,d\theta$$
即
$$S=2\pi R\left[a\theta-R\cos\theta\right]_0^{2\pi}=4\pi^2Ra$$
故救生圈的表面积为 $4\pi^2Ra$

## 建立方式

(1) 基于 Riemann 积分理论, 研究平面曲边扇形与曲边梯形, 柱型体体积, 曲线弧长与旋成体侧面积
由此体会数学建模, 数学分析, 指导实践这三个基本过程
其中建模按分割, 选取, 求和与求极限进行

(2) 数学实验的结论有时可直接确认为真理, 有时必须经实践检验
前者对应真实值可由 Darboux 小和与大和夹逼的情形
此时小和与大和的共同极限即为真实值
后者对应真实值没有相应控制的情形, 只能由实践鉴别

(3) 旋成体侧面积的两种方案表明, 建模与分析都合逻辑仍可能给出错误结论
圆台近似与圆柱近似的差别在于局部近似的形态
仅考察圆锥的侧面积即可鉴别两者的对错

(4) 相关处理追求一般形式, 如旋成体侧面积基于曲线的一般参数表达
以此尽量获得一般化的结论
同一积分结构可覆盖面积, 体积, 弧长与压力等不同对象
