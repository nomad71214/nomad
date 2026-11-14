# Darboux 和分析

- [知识点](#知识点)
- [Darboux 和的估计](#Darboux%20和的估计)
- [Riemann 可积的判别法](#Riemann%20可积的判别法)
- [Riemann 可积函数类](#Riemann%20可积函数类)
- [拓广深化](#拓广深化)
  - [集合运算基础](#集合运算基础)
  - [Lebesgue-Stieltjes 测度](#Lebesgue-Stieltjes%20测度)
- [建立方式](#建立方式)

## 知识点

Riemann 可积性首先要求被积函数在积分区间上有界
限于有界函数类, 相对于部分和定义 Darboux 大和与小和
按确界的基本性质建立 Darboux 和的和谐式估计
由此获得两个基础极限, 大和与小和分别以各自的确界为极限
可积性等价于大和的下确界等于小和的上确界
也等价于分割的模趋于零时振幅和趋于零
Riemann 判别法给出可积性的另一充分必要叙述
据此确定连续函数, 单调函数与四则运算等可积函数类

## Darboux 和的估计

定理14-1 有界性
如有 $f(x)\in R[a,b]$, 则 $f(x)$ 在 $[a,b]$ 上有界
证明 取定 $\varepsilon^*>0$, 按可积性存在分割 $P^*$ 满足
$$\left|\sum_{i=1}^N f(\xi_i)\Delta x_i-I\right|<\varepsilon^*,\quad\forall\xi_i\in[x_{i-1},x_i]$$
其中 $I$ 为部分和的极限

对每个 $j$ 分离出第 $j$ 项, 有
$$\left|f(\xi_j)\Delta x_j+\sum_{i=1,\,i\neq j}^N f(\xi_i)\Delta x_i-I\right|<\varepsilon^*$$
即有
$$|f(\xi_j)|\Delta x_j\leqslant\sum_{i=1,\,i\neq j}^N|f(\xi_i)|\Delta x_i+|I|+\varepsilon^*$$
取定 $i\neq j$ 时的 $\xi_i=x_i$, 得
$$|f(\xi_j)|\Delta x_j\leqslant\sum_{i=1}^N|f(x_i)|\Delta x_i+|I|+\varepsilon^*$$
故有
$$|f(\xi_j)|\leqslant\dfrac{1}{\min\limits_{1\leqslant j\leqslant N}\Delta x_j}\left[\sum_{i=1}^N|f(x_i)|\Delta x_i+|I|+\varepsilon^*\right]$$
上式右端与 $j$ 及 $\xi_j$ 无关, 故 $f(x)$ 在 $[a,b]$ 上有界

以下将范围限于 $[a,b]$ 上的有界函数类, 作
$$L(f,P)=\sum_{i=1}^N\inf_{[x_{i-1},x_i]}f(x)\Delta x_i$$
$$U(f,P)=\sum_{i=1}^N\sup_{[x_{i-1},x_i]}f(x)\Delta x_i$$
分别称为 Darboux 小和与大和

定义 函数在区间上的振幅
设 $f(x)$ 在 $[a,b]$ 上有界, 称
$$\omega(f)=\sup_{\tilde x,\hat x\in[a,b]}|f(\tilde x)-f(\hat x)|$$
为 $f(x)$ 在 $[a,b]$ 上的振幅

性质14-2 振幅的表示
如 $f(x)$ 在 $[a,b]$ 上有界, 则
$$\omega(f)=\sup_{[a,b]}f(x)-\inf_{[a,b]}f(x)$$
证明 有界性保证上式右端为有限数, 且
$$f(\tilde x)-f(\hat x)\leqslant\sup_{[a,b]}f(x)-\inf_{[a,b]}f(x),\quad\forall\tilde x,\hat x\in[a,b]$$
故右端为 $\{|f(\tilde x)-f(\hat x)|\}$ 的一个上界

另一方面, 按上确界与下确界的定义, 对 $\forall\varepsilon>0$ 存在 $\tilde x_\varepsilon$, $\hat x_\varepsilon$ 满足
$$\sup_{[a,b]}f(x)-\varepsilon<f(\tilde x_\varepsilon),\quad f(\hat x_\varepsilon)<\inf_{[a,b]}f(x)+\varepsilon$$
于是
$$\sup_{[a,b]}f(x)-\inf_{[a,b]}f(x)-2\varepsilon<|f(\tilde x_\varepsilon)-f(\hat x_\varepsilon)|$$
故右端为最小上界

对分割 $P$, 记 $\omega_i(f)=\sup\limits_{[x_{i-1},x_i]}f-\inf\limits_{[x_{i-1},x_i]}f$, 称
$$\Omega(f,P)=\sum_{i=1}^N\omega_i(f)\Delta x_i=U(f,P)-L(f,P)$$
为振幅和

性质14-3 Darboux 和的和谐式估计
增加分点时大和不增, 小和不减, 且增减量可控
$$L(f,P)\leqslant L(f,P\cup\{x^*\})\leqslant L(f,P)+\omega(f)|P|$$
$$U(f,P)-\omega(f)|P|\leqslant U(f,P\cup\{x^*\})\leqslant U(f,P)$$
证明 设在 $[x_{j-1},x_j]$ 内插入分点 $x^*$
由 $\inf\limits_{[x_{j-1},x^*]}f\geqslant\inf\limits_{[x_{j-1},x_j]}f$ 与 $\inf\limits_{[x^*,x_j]}f\geqslant\inf\limits_{[x_{j-1},x_j]}f$ 得
$$L(f,P\cup\{x^*\})\geqslant L(f,P)$$
反之, 将小和的增量按两段的振幅估计, 有
$$L(f,P\cup\{x^*\})-L(f,P)=\left[\inf_{[x_{j-1},x^*]}f-\inf_{[x_{j-1},x_j]}f\right](x^*-x_{j-1})+\left[\inf_{[x^*,x_j]}f-\inf_{[x_{j-1},x_j]}f\right](x_j-x^*)$$
$$\leqslant\left[\sup_{[x_{j-1},x_j]}f-\inf_{[x_{j-1},x_j]}f\right]\Delta x_j=\omega_j(f)\Delta x_j\leqslant\omega(f)|P|$$
故有 $L(f,P\cup\{x^*\})\leqslant L(f,P)+\omega(f)|P|$

对大和, 由
$$\sup_{[x_{j-1},x^*]}f(x)(x^*-x_{j-1})+\sup_{[x^*,x_j]}f(x)(x_j-x^*)\leqslant\sup_{[x_{j-1},x_j]}f(x)\Delta x_j$$
得 $U(f,P\cup\{x^*\})\leqslant U(f,P)$
同理将大和的减量按两段的振幅估计, 有
$$\sup_{[x_{j-1},x_j]}f(x)\Delta x_j-\sup_{[x_{j-1},x^*]}f(x)(x^*-x_{j-1})-\sup_{[x^*,x_j]}f(x)(x_j-x^*)\leqslant\omega_j(f)\Delta x_j\leqslant\omega(f)|P|$$
故有 $U(f,P\cup\{x^*\})\geqslant U(f,P)-\omega(f)|P|$

推论14-4 振幅和的和谐式估计
增加分点时振幅和满足
$$\Omega(f,P)-2\omega(f)|P|\leqslant\Omega(f,P\cup\{x^*\})\leqslant\Omega(f,P)$$
证明 由 $\Omega=U-L$ 与性质14-3, 有
$$\Omega(f,P\cup\{x^*\})=U(f,P\cup\{x^*\})-L(f,P\cup\{x^*\})\leqslant U(f,P)-L(f,P)=\Omega(f,P)$$
$$\Omega(f,P\cup\{x^*\})\geqslant U(f,P)-\omega(f)|P|-\left[L(f,P)+\omega(f)|P|\right]=\Omega(f,P)-2\omega(f)|P|$$

性质14-5 有界函数 Darboux 和的性质
设 $f(x)$ 在 $[a,b]$ 上有界, 则
(1) $L(f,\tilde P)\leqslant U(f,\hat P)$, $\forall\tilde P$, $\hat P$;
(2) 两个极限存在, 且
$$\exists\lim_{|P|\to0}L(f,P)=\sup_P L(f,P)\in\mathbb{R}$$
$$\exists\lim_{|P|\to0}U(f,P)=\inf_P U(f,P)\in\mathbb{R}$$
证明 (1) 由
$$L(f,\tilde P)\leqslant L(f,\tilde P\cup\hat P)\leqslant U(f,\tilde P\cup\hat P)\leqslant U(f,\hat P)$$
即得

(2) 任一 Darboux 大和为所有小和的上界, 按确界存在性定理知 $\sup\limits_P L(f,P)$ 存在
任一 Darboux 小和为所有大和的下界, 同理知 $\inf\limits_P U(f,P)$ 存在
由和谐式估计, 增添 $P_\varepsilon$ 的分点至多使小和改变 $\mathrm{Num}(P_\varepsilon)\omega(f)|P|$, 故
$$0\leqslant\sup_P L(f,P)-L(f,P)<L(f,P_\varepsilon)+\varepsilon-L(f,P)$$
$$\leqslant L(f,P_\varepsilon\cup P)-L(f,P)+\varepsilon\leqslant\mathrm{Num}(P_\varepsilon)\omega(f)|P|+\varepsilon$$
取 $|P|<\dfrac{\varepsilon}{\mathrm{Num}(P_\varepsilon)}=\delta_\varepsilon$, 即有该量小于 $(\omega(f)+1)\varepsilon$
大和的情形同理, 有
$$0\leqslant U(f,P)-\inf_P U(f,P)<U(f,P)-U(f,P_\varepsilon)+\varepsilon\leqslant\mathrm{Num}(P_\varepsilon)\omega(f)|P|+\varepsilon$$
故两个极限存在, 且分别为上确界与下确界

## Riemann 可积的判别法

定理14-6 可积性的等价性叙述
设 $f(x)$ 在 $[a,b]$ 上有界, 以下三种叙述等价
(1) 对 $\forall\varepsilon>0$, 存在分割 $P_\varepsilon$ 满足
$$U(f,P_\varepsilon)-L(f,P_\varepsilon)<\varepsilon$$
(2) $$\sup_P L(f,P)=\inf_P U(f,P)$$
(3) $$\exists\lim_{|P|\to0}\sum_{i=1}^N f(\xi_i)\Delta x_i=:\int_a^b f(x)\,dx\in\mathbb{R}$$
证明 (1)$\Rightarrow$(2) 由 (1), 当 $|P|<\delta_\varepsilon$ 时估计
$$0\leqslant U(f,P)-L(f,P)\leqslant U(f,P\cup P_\varepsilon)-L(f,P\cup P_\varepsilon)+2\mathrm{Num}(P_\varepsilon)\omega(f)|P|$$
$$\leqslant U(f,P_\varepsilon)-L(f,P_\varepsilon)+2\mathrm{Num}(P_\varepsilon)\omega(f)|P|<(1+2\omega(f))\varepsilon$$
故 $\lim\limits_{|P|\to0}\left[U(f,P)-L(f,P)\right]=0$, 即得 (2)

(2)$\Rightarrow$(3) 对任意分割与介点有
$$L(f,P)\leqslant\sum_{i=1}^N f(\xi_i)\Delta x_i\leqslant U(f,P)$$
而两端极限相等, 按极限的夹逼性即得 (3)

(3)$\Rightarrow$(1) 按极限的 Cauchy 叙述, 对 $\forall\varepsilon>0$ 与 $|P|<\delta_\varepsilon$ 有
$$\int_a^b f(x)\,dx-\varepsilon<\sum_{i=1}^N f(\xi_i)\Delta x_i<\int_a^b f(x)\,dx+\varepsilon$$
取 $\tilde\xi_i$ 使部分和充分接近 $L(f,P_\varepsilon)$, 取 $\hat\xi_i$ 使部分和充分接近 $U(f,P_\varepsilon)$, 则
$$\int_a^b f(x)\,dx-\varepsilon<L(f,P_\varepsilon)+\varepsilon(b-a)$$
$$U(f,P_\varepsilon)-\varepsilon(b-a)<\int_a^b f(x)\,dx+\varepsilon$$
即有
$$U(f,P_\varepsilon)-L(f,P_\varepsilon)<2\varepsilon(b-a)+2\varepsilon$$

引入振幅和后, 上述等价性叙述可写为
(1) 对 $\forall\varepsilon>0$, 存在 $P_\varepsilon$ 满足 $\Omega(f,P_\varepsilon)<\varepsilon$;
(2) $\exists\lim\limits_{|P|\to0}\Omega(f,P)=0$;
(3) 部分和的极限存在

定理14-7 Riemann 判别法
$f(x)$ 在 $[a,b]$ 上 Riemann 可积的充要条件为, 对 $\forall\lambda$, $\mu>0$ 存在 $\delta_{\lambda\mu}>0$ 满足
$$\sum_{\omega_i>\lambda}\Delta x_i<\mu,\quad\forall|P|<\delta_{\lambda\mu}$$
证明 必要性 设 $f(x)\in R[a,b]$, 则 $\lim\limits_{|P|\to0}\Omega(f,P)=0$, 按 Cauchy 叙述, 对 $\forall\varepsilon>0$ 有
$$\sum_{i=1}^N\omega_i\Delta x_i<\varepsilon,\quad\forall|P|<\delta_\varepsilon$$
将和式按 $\omega_i$ 与 $\lambda$ 的大小关系拆分, 有
$$\lambda\sum_{\omega_i>\lambda}\Delta x_i<\sum_{\omega_i>\lambda}\omega_i\Delta x_i<\varepsilon$$
取 $\mu=\varepsilon/\lambda$ 即得所需

充分性 设条件成立, 估计
$$\sum_{i=1}^N\omega_i\Delta x_i=\sum_{\omega_i>\lambda}\omega_i\Delta x_i+\sum_{\omega_i\leqslant\lambda}\omega_i\Delta x_i$$
$$\leqslant\omega(f)\sum_{\omega_i>\lambda}\Delta x_i+\lambda\sum_{\omega_i\leqslant\lambda}\Delta x_i<\omega(f)\mu+(b-a)\lambda$$
取 $\mu=\lambda=\varepsilon$, 即有 $\Omega(f,P)<\left[\omega(f)+(b-a)\right]\varepsilon$, 故 $f(x)\in R[a,b]$

## Riemann 可积函数类

性质14-8 连续函数的可积性
如 $f(x)\in C[a,b]$, 则 $f(x)\in R[a,b]$
证明 分析一, 按振幅和估计
由 $f(x)$ 在 $[a,b]$ 上一致连续, 对 $\forall\varepsilon>0$ 存在 $\delta_\varepsilon>0$ 使
$$|f(\tilde x)-f(\hat x)|<\varepsilon,\quad\forall\tilde x,\hat x\in[a,b],\ |\tilde x-\hat x|<\delta_\varepsilon$$
故当 $|P|<\delta_\varepsilon$ 时
$$\Omega(f,P)=\sum_{i=1}^N\sup_{\tilde x,\hat x\in[x_{i-1},x_i]}|f(\tilde x)-f(\hat x)|\Delta x_i\leqslant\varepsilon\sum_{i=1}^N\Delta x_i=(b-a)\varepsilon$$
即有 $\exists\lim\limits_{|P|\to0}\Omega(f,P)=0$, 故 $f(x)\in R[a,b]$

分析二, 按 Riemann 判别法
由一致连续性, 当 $|P|<\delta_\varepsilon$ 时不存在振幅大于 $\varepsilon$ 的子区间, 即有
$$\sum_{\omega_i>\varepsilon}\Delta x_i=0$$
按定理14-7 即得 $f(x)\in R[a,b]$

性质14-9 单调函数的可积性
如 $f(x)$ 在 $[a,b]$ 上单调, 则 $f(x)\in R[a,b]$
证明 不妨设 $f(x)$ 单调上升, 则 $\omega_i=f(x_i)-f(x_{i-1})$, 有
$$\Omega(f,P)=\sum_{i=1}^N\left[f(x_i)-f(x_{i-1})\right]\Delta x_i\leqslant\sum_{i=1}^N\left[f(x_i)-f(x_{i-1})\right]|P|=\left[f(b)-f(a)\right]|P|$$
故当 $|P|\to0$ 时 $\Omega(f,P)\to0$, 即有 $f(x)\in R[a,b]$

性质14-10 可积函数的四则运算
如 $f(x)$, $g(x)\in R[a,b]$, 则
(1) $(\alpha f+\beta g)(x)\in R[a,b]$;
(2) $(fg)(x)\in R[a,b]$;
(3) $\left(\dfrac{f}{g}\right)(x)\in R[a,b]$, 要求 $|g(x)|\geqslant\delta>0$, $\forall x\in[a,b]$
证明 均按振幅和估计
(1) 由
$$|(\alpha f+\beta g)(\tilde x)-(\alpha f+\beta g)(\hat x)|\leqslant|\alpha||f(\tilde x)-f(\hat x)|+|\beta||g(\tilde x)-g(\hat x)|$$
得 $\Omega(\alpha f+\beta g,P)\leqslant|\alpha|\Omega(f,P)+|\beta|\Omega(g,P)\to0$

(2) 由
$$|(fg)(\tilde x)-(fg)(\hat x)|\leqslant\sup_{[a,b]}|g||f(\tilde x)-f(\hat x)|+\sup_{[a,b]}|f||g(\tilde x)-g(\hat x)|$$
得 $\Omega(fg,P)\leqslant\sup\limits_{[a,b]}|f|\Omega(g,P)+\sup\limits_{[a,b]}|g|\Omega(f,P)\to0$

(3) 由 $|g(x)|\geqslant\delta$ 有
$$\left|\left(\dfrac{f}{g}\right)(\tilde x)-\left(\dfrac{f}{g}\right)(\hat x)\right|=\dfrac{|f(\tilde x)g(\hat x)-f(\hat x)g(\tilde x)|}{|g(\tilde x)g(\hat x)|}\leqslant\dfrac{1}{\delta^2}\left[\sup_{[a,b]}|g||f(\tilde x)-f(\hat x)|+\sup_{[a,b]}|f||g(\tilde x)-g(\hat x)|\right]$$
得
$$\Omega\left(\dfrac{f}{g},P\right)\leqslant\dfrac{1}{\delta^2}\left[\sup_{[a,b]}|f|\Omega(g,P)+\sup_{[a,b]}|g|\Omega(f,P)\right]\to0$$
故三种运算的结果均属于 $R[a,b]$

性质14-11 连续函数复合可积函数
如 $\theta(x)\in R[\alpha,\beta]$, $\Theta(y)\in C[a,b]$, 且 $\theta([\alpha,\beta])\subset[a,b]$, 则
$$\Theta\circ\theta(x)\in R[\alpha,\beta]$$
证明 由 $\Theta(y)$ 在 $[a,b]$ 上一致连续, 对 $\forall\varepsilon>0$ 存在 $\delta_\varepsilon>0$ 使
$$|\Theta(\tilde y)-\Theta(\hat y)|<\varepsilon,\quad\forall\tilde y,\hat y\in[a,b],\ |\tilde y-\hat y|<\delta_\varepsilon$$
故有包含关系
$$\left\{[x_{i-1},x_i]\ |\ \omega_i^\theta<\delta_\varepsilon\right\}\subset\left\{[x_{i-1},x_i]\ |\ \omega_i^{\Theta\circ\theta}\leqslant\varepsilon\right\}$$
即
$$\left\{[x_{i-1},x_i]\ |\ \omega_i^{\Theta\circ\theta}>\varepsilon\right\}\subset\left\{[x_{i-1},x_i]\ |\ \omega_i^\theta\geqslant\delta_\varepsilon\right\}$$
于是
$$\sum_{\omega_i^{\Theta\circ\theta}>\varepsilon}\Delta x_i\leqslant\sum_{\omega_i^\theta\geqslant\delta_\varepsilon}\Delta x_i<\mu$$
最后的不等号基于 $\theta(x)\in R[\alpha,\beta]$ 的 Riemann 判别法, 故 $\Theta\circ\theta(x)\in R[\alpha,\beta]$

性质14-12 绝对可积性
如 $f(x)\in R[a,b]$, 则 $|f(x)|\in R[a,b]$
证明 由
$$\bigl|\,|f(\tilde x)|-|f(\hat x)|\,\bigr|\leqslant|f(\tilde x)-f(\hat x)|,\quad\forall\tilde x,\hat x\in[a,b]$$
得 $\Omega(|f|,P)\leqslant\Omega(f,P)\to0$, 故 $|f(x)|\in R[a,b]$

## 拓广深化

### 集合运算基础

性质14-13 集合运算的基本性质
设各集合均在同一个基本集合中讨论, 则
(1) $$F-E=F\cap E^c$$
(2) $$F\cap(\tilde E\cup\hat E)=(F\cap\tilde E)\cup(F\cap\hat E)$$
(3) $$(\tilde E\cup\hat E)-F=(\tilde E-F)\cup(\hat E-F)$$
(4) $$F-\bigcup_{i=1}^\infty E_i=\bigcap_{i=1}^\infty(F-E_i)$$
(5) $$F-\bigcap_{i=1}^\infty E_i=\bigcup_{i=1}^\infty(F-E_i)$$
证明 逐条按元素隶属关系作等价变形
(1) $x\in F-E$ 等价于 $x\in F$ 且 $x\notin E$, 即 $x\in F\cap E^c$
(2) $x\in F\cap(\tilde E\cup\hat E)$ 等价于 $x\in F$ 且 $x\in\tilde E\cup\hat E$, 即 $x$ 属于两个交集的并
(3) 按 (1) 与交并对分配的运算律, 有
$$(\tilde E\cup\hat E)-F=(\tilde E\cup\hat E)\cap F^c=(\tilde E\cap F^c)\cup(\hat E\cap F^c)=(\tilde E-F)\cup(\hat E-F)$$
(4) $x\in F-\bigcup\limits_{i=1}^\infty E_i$ 等价于 $x\in F$ 且 $x\notin E_i$, $\forall i$, 即 $x\in\bigcap\limits_{i=1}^\infty(F-E_i)$
(5) $x\in F-\bigcap\limits_{i=1}^\infty E_i$ 等价于 $x\in F$ 且存在 $i$ 使 $x\notin E_i$, 即 $x\in\bigcup\limits_{i=1}^\infty(F-E_i)$

### Lebesgue-Stieltjes 测度

Riemann 积分的特点在于定义域分割, 对应于极限
$$\lim_{|P_x|\to0}\sum_{i=1}^N f(\xi_i)\Delta x_i,\quad\forall\xi_i\in[x_{i-1},x_i]$$
其中 $P_x$ 为定义域的分割
Lebesgue-Stieltjes 积分的特点在于值域分割, 对应于极限
$$\lim_{|P_y|\to0}\sum_{i=1}^N\eta_i\left|D_f(y_{i-1}\leqslant f(x)<y_i)\right|_\mu,\quad\forall\eta_i\in[y_{i-1},y_i]$$
其中 $P_y$ 为值域的分割, $D_f$ 为 $f(x)$ 的定义域, 且
$$D_f(y_{i-1}\leqslant f(x)<y_i)=\left\{x\in D_f\ |\ y_{i-1}\leqslant f(x)<y_i\right\}$$
按值域分割定义积分, 需要为非规则的集合赋予大小的度量, 即引入测度
同时还需要引入可测函数

![图14-1]()

![图14-2]()

定理14-14 闭区间的有限覆盖定理
(1) 如 $[a,b]\subset\bigcup\limits_{\alpha\in\Lambda}U_\alpha$, 各 $U_\alpha$ 为开区间, 则存在有限个 $U_{\alpha_i}$ 使
$$[a,b]\subset\bigcup_{i=1}^NU_{\alpha_i}$$
(2) 如 $[a,b]\subset\bigcup\limits_{n=1}^\infty U_n$, 各 $U_n$ 为开区间, 则存在有限个 $U_{n_k}$ 使
$$[a,b]\subset\bigcup_{k=1}^NU_{n_k}$$
证明 (1) 采用反证法, 设覆盖需要无穷多个元素
对分 $[a,b]$, 则至少有一个闭子区间需要无穷多覆盖, 记为 $[a_1,b_1]$
再对分 $[a_1,b_1]$, 同样取需要无穷多覆盖的闭子区间 $[a_2,b_2]$, 依此类推得
$$[a,b]\supset[a_1,b_1]\supset[a_2,b_2]\supset\cdots\supset[a_n,b_n]\supset\cdots$$
$$\lim_{n\to\infty}(b_n-a_n)=0$$
且每个 $[a_n,b_n]$ 都需要无穷多覆盖
按闭区间套定理, 存在唯一 $\xi\in[a_n,b_n]$, $\forall n\in\mathbb{N}$, 且 $\xi\in[a,b]$
设 $\xi\in U_\alpha$, 由 $U_\alpha$ 为开区间, 存在 $B_\delta(\xi)\subset U_\alpha$
又 $a_n\uparrow\xi$ 与 $b_n\downarrow\xi$, 故当 $n$ 充分大时有 $[a_n,b_n]\subset B_\delta(\xi)\subset U_\alpha$, 与上述结论矛盾

(2) 采用反证法, 设需要 $\{U_n\}_{n\in\mathbb{N}}$ 中的无穷多个元素
取
$$x_n\in U_n-\bigcup_{k=1}^{n-1}U_k,\quad\forall n\in\mathbb{N}$$
由 $\{x_n\}\subset[a,b]$ 与 Bolzano-Weierstrass 定理, 存在子列 $x_{n_k}\to x^*\in[a,b]$
设 $x^*\in U_{n^*}$, 由 $U_{n^*}$ 为开区间, 存在 $B_\delta(x^*)\subset U_{n^*}$, 故 $x_{n_k}\in U_{n^*}$ 当 $k$ 充分大
取 $n>\max\{n_{N_\delta},n^*\}$, 按构造有 $x_n\in U_n$ 而 $x_n\notin U_{n^*}$, 产生矛盾

作 $\mathcal{P}=\left\{(a,b]\ |\ a<b,\ a,b\in\mathbb{R}\right\}$, 即 $\mathbb{R}$ 上左开右闭区间的全体
作 $\mathcal{R}=\left\{\bigcup\limits_{i=1}^NE_i\ |\ E_i\in\mathcal{P}\right\}$, 即有限个左开右闭区间之并的全体

性质14-15 环结构
$\mathcal{R}$ 对并与差运算封闭, 即有
$$E\cup F\in\mathcal{R},\quad E-F\in\mathcal{R},\quad\forall E,F\in\mathcal{R}$$
证明 只需讨论左开右闭区间, 有
$$(a,b]\cup(c,d]=\begin{cases}(a,b]\cup(c,d], & (a,b]\cap(c,d]=\varnothing\\ (a,d], & (a,b]\cap(c,d]\neq\varnothing\end{cases}$$
$$(a,b]-(c,d]=\begin{cases}(a,b], & (a,b]\cap(c,d]=\varnothing\\ (a,c], & (a,b]\cap(c,d]\neq\varnothing\\ (a,c]\cup(d,b], & (a,b]\supset(c,d]\end{cases}$$
一般元素由有限并的情形按上述两式整理即得

对 $\forall E\in\mathcal{R}$, 可取互不相交的 $\left\{(a_i,b_i]\right\}_{i=1}^N\subset\mathcal{P}$ 使
$$E=\bigcup_{i=1}^N(a_i,b_i]$$
称 $\left\{(a_i,b_i]\right\}_{i=1}^N$ 为 $E$ 的一个初等分解

定义 环上的 Lebesgue-Stieltjes 测度
设 $g(x)$ 为 $\mathbb{R}$ 上单调上升的右连续函数, 定义
$$|(a,b]|_\mu=g(b)-g(a),\quad\forall(a,b]\in\mathcal{P}$$
$$|E|_\mu=\sum_{i=1}^N|(a_i,b_i]|_\mu=\sum_{i=1}^N\left[g(b_i)-g(a_i)\right]$$
其中 $\left\{(a_i,b_i]\right\}_{i=1}^N$ 为 $E$ 的初等分解
单调上升右连续函数的一个实际背景, 是数轴上一般分布的正电荷的电量

![图14-3]()

性质14-16 测度与初等分解的选取无关
上述定义不依赖 $E$ 的初等分解的选择, 且具有
(1) 对 $E=(a,b]=\bigcup\limits_{i=1}^N(x_{i-1},x_i]$ 有 $\sum\limits_{i=1}^N|(x_{i-1},x_i]|_\mu=g(b)-g(a)$;
(2) 非负性 $|E|_\mu\geqslant0$, $\forall E\in\mathcal{R}$;
(3) 有限可加性, 对互不相交的 $\{E_i\}_{i=1}^N\subset\mathcal{R}$ 有
$$\left|\bigcup_{i=1}^NE_i\right|_\mu=\sum_{i=1}^N|E_i|_\mu$$
(4) 可列可加性, 对互不相交的 $\{E_i\}_{i\in\mathbb{N}}\subset\mathcal{R}$ 且 $\bigcup\limits_{n=1}^\infty E_n\in\mathcal{R}$, 有
$$\left|\bigcup_{i=1}^\infty E_i\right|_\mu=\sum_{i=1}^\infty|E_i|_\mu$$
证明 (1) 区间的情形由逐项相消得
$$\sum_{i=1}^N|(x_{i-1},x_i]|_\mu=\sum_{i=1}^N\left[g(x_i)-g(x_{i-1})\right]=g(b)-g(a)$$
一般情形取两个初等分解 $E=\bigcup\limits_{i=1}^MF_i=\bigcup\limits_{j=1}^NG_j$, 由
$$E=\bigcup_{i=1}^M\bigcup_{j=1}^N(F_i\cap G_j)$$
及区间情形的结论, 有
$$\sum_{i=1}^M|F_i|_\mu=\sum_{i=1}^M\sum_{j=1}^N|F_i\cap G_j|_\mu=\sum_{j=1}^N|G_j|_\mu$$
故定义与分解的选取无关
(2) 按 $g(x)$ 的单调性即见
(3) 将各 $E_i$ 的初等分解合并, 即得 $\bigcup\limits_{i=1}^NE_i$ 的初等分解
(4) 设 $\bigcup\limits_{i=1}^\infty E_i=\bigcup\limits_{\alpha=1}^N(A_\alpha,B_\alpha]$ 为一个初等分解, 又
$$\bigcup_{i=1}^\infty E_i=\bigcup_{k=1}^\infty(a_k,b_k]$$
式中各区间互不相交
由 $\bigcup\limits_{k=1}^n(a_k,b_k]\subset\bigcup\limits_{\alpha=1}^N(A_\alpha,B_\alpha]$ 得
$$\sum_{k=1}^n|(a_k,b_k]|_\mu\leqslant\sum_{\alpha=1}^N|(A_\alpha,B_\alpha]|_\mu,\quad\forall n\in\mathbb{N}$$
故只需再证反向不等式
对 $\forall\varepsilon>0$, 按 $g(x)$ 的右连续性取 $\lambda_\alpha$, $\mu_k>0$ 使
$$g(A_\alpha+\lambda_\alpha)<g(A_\alpha)+\dfrac{\varepsilon}{N},\quad g(b_k+\mu_k)<g(b_k)+\dfrac{\varepsilon}{2^k}$$
考虑到
$$\bigcup_{\alpha=1}^N[A_\alpha+\lambda_\alpha,B_\alpha]\subset\bigcup_{k=1}^\infty(a_k,b_k+\mu_k)$$
按有限覆盖定理取出有限子覆盖 $\bigcup\limits_{j=1}^M(a_{k_j},b_{k_j}+\mu_{k_j})$, 由测度的单调性有
$$\sum_{\alpha=1}^N\left[g(B_\alpha)-g(A_\alpha+\lambda_\alpha)\right]\leqslant\sum_{k=1}^\infty\left[g(b_k+\mu_k)-g(a_k)\right]$$
于是
$$\sum_{\alpha=1}^N\left[g(B_\alpha)-g(A_\alpha)\right]-\varepsilon\leqslant\sum_{k=1}^\infty\left[g(b_k)-g(a_k)\right]+\varepsilon$$
由 $\varepsilon$ 的任意性即得所证

定理14-17 环上测度的扩张
设 $(X,\mathcal{R},\mu)$ 为环上的测度, 作
$$\mathcal{H}(\mathcal{R})=\left\{F\subset X\ |\ \exists\{E_i\}_{i\in\mathbb{N}}\subset\mathcal{R},\ F\subset\bigcup_{i=1}^\infty E_i\right\}$$
$$\mu^*(F)=\inf\left\{\sum_{i=1}^\infty\mu(E_i)\ |\ F\subset\bigcup_{i=1}^\infty E_i\right\}$$
则 $\mu^*$ 为 $\mathcal{H}(\mathcal{R})$ 上的外测度

性质14-18 外测度的性质
(1) $\mathcal{H}(\mathcal{R})$ 为 $\sigma$-环, 即对可列并及差运算封闭;
(2) $\mu^*$ 在 $\mathcal{H}(\mathcal{R})$ 上非负;
(3) $\mu^*$ 具有单调性, 即 $F\subset G$ 时有 $\mu^*(F)\leqslant\mu^*(G)$;
(4) $\mu^*$ 具有次可列可加性
$$\mu^*\left(\bigcup_{i=1}^\infty F_i\right)\leqslant\sum_{i=1}^\infty\mu^*(F_i)$$
证明 (1) 设 $F_i\subset\bigcup\limits_{j=1}^\infty E_i^{(j)}$, 则 $\bigcup\limits_{i=1}^\infty F_i\subset\bigcup\limits_{i,j}E_i^{(j)}$, 故对可列并封闭
又 $F-G\subset\bigcup\limits_{i=1}^\infty E_i$, 故对差运算封闭
(2) 按 $\mu^*$ 的定义即见
(3) $G$ 的覆盖必为 $F$ 的覆盖, 按下确界的定义即得
(4) 对 $\forall\varepsilon>0$, 取覆盖使
$$\sum_{j=1}^\infty\mu(E_i^{(j)})<\mu^*(F_i)+\dfrac{\varepsilon}{2^i}$$
相加得
$$\sum_{i=1}^\infty\sum_{j=1}^\infty\mu(E_i^{(j)})\leqslant\sum_{i=1}^\infty\mu^*(F_i)+\varepsilon$$
由 $\varepsilon$ 的任意性即得次可列可加性

性质14-19 Caratheodory 集类
称
$$\mathcal{R}^*=\left\{E\in\mathcal{H}(\mathcal{R})\ |\ \mu^*(F)=\mu^*(F\cap E)+\mu^*(F-E),\ \forall F\in\mathcal{H}(\mathcal{R})\right\}$$
为 Caratheodory 集类, 则有
(1) $\mathcal{R}\subset\mathcal{R}^*$;
(2) $\mathcal{R}^*$ 为环;
(3) 对互不相交的 $\{E_i\}_{i=1}^N\subset\mathcal{R}^*$ 有
$$\mu^*\left(F\cap\bigcup_{i=1}^NE_i\right)=\sum_{i=1}^N\mu^*(F\cap E_i),\quad\forall F\in\mathcal{H}(\mathcal{R})$$
(4) $\mathcal{R}^*$ 为 $\sigma$-环;
(5) $\mu^*$ 为 $\mathcal{R}^*$ 上的测度;
(6) $\mu^*$ 限制于 $\mathcal{R}$ 上即为 $\mu$, 亦即 $\mu^*|_{\mathcal{R}}=\mu$
证明 (1) 对 $E\in\mathcal{R}$, 次可加性给出
$$\mu^*(F)\leqslant\mu^*(F\cap E)+\mu^*(F-E),\quad\forall F\in\mathcal{H}(\mathcal{R})$$
反之取 $F$ 的覆盖 $\{E_i\}_{i\in\mathbb{N}}\subset\mathcal{R}$ 使 $\sum\limits_{i=1}^\infty\mu(E_i)<\mu^*(F)+\varepsilon$, 按 $\mu$ 在 $\mathcal{R}$ 上的有限可加性有
$$\mu^*(F\cap E)+\mu^*(F-E)\leqslant\sum_{i=1}^\infty\left[\mu(E_i\cap E)+\mu(E_i-E)\right]=\sum_{i=1}^\infty\mu(E_i)<\mu^*(F)+\varepsilon$$
故 $E\in\mathcal{R}^*$

(2) 设 $\tilde E$, $\hat E\in\mathcal{R}^*$, 按定义计算
$$\mu^*(F)=\mu^*(F\cap\tilde E)+\mu^*(F-\tilde E)=\mu^*(F\cap\tilde E\cap\hat E)+\mu^*(F\cap\tilde E-\hat E)+\mu^*(F-\tilde E)$$
再将 $F-\tilde E$ 按 $\hat E$ 分解并整理, 得
$$\mu^*(F)=\mu^*(F\cap\tilde E\cap\hat E)+\mu^*(F-\tilde E\cap\hat E)$$
故 $\tilde E\cap\hat E\in\mathcal{R}^*$
把 $F-\tilde E$ 作另一种分拆并合并相应的项, 同理可得 $\tilde E\cup\hat E\in\mathcal{R}^*$, 由此 $\tilde E-\hat E\in\mathcal{R}^*$

(3) 对 $N$ 作归纳. $N=1$ 时由定义. 设已有 $N$ 的情形, 则
$$\mu^*\left(F\cap\bigcup_{i=1}^{N+1}E_i\right)=\mu^*(F\cap E_{N+1})+\mu^*\left(F\cap\bigcup_{i=1}^NE_i\right)=\sum_{i=1}^{N+1}\mu^*(F\cap E_i)$$
(4) 设 $\{E_i\}_{i\in\mathbb{N}}\subset\mathcal{R}^*$, 由 (3) 与单调性有
$$\mu^*(F)\geqslant\sum_{i=1}^n\mu^*(F\cap E_i)+\mu^*\left(F-\bigcup_{i=1}^\infty E_i\right)$$
令 $n\to\infty$, 再按次可加性即得
$$\mu^*(F)\geqslant\mu^*\left(F\cap\bigcup_{i=1}^\infty E_i\right)+\mu^*\left(F-\bigcup_{i=1}^\infty E_i\right)$$
故 $\bigcup\limits_{i=1}^\infty E_i\in\mathcal{R}^*$

(5) 在 (4) 的估计中取 $F=\bigcup\limits_{i=1}^\infty E_i$, 得
$$\mu^*\left(\bigcup_{i=1}^\infty E_i\right)\geqslant\sum_{i=1}^n\mu^*(E_i),\quad\forall n\in\mathbb{N}$$
令 $n\to\infty$ 并利用次可列可加性, 即得可列可加性
(6) 由覆盖 $\{E,\varnothing,\cdots\}$ 得 $\mu^*(E)\leqslant\mu(E)$
反之对 $\forall\varepsilon>0$ 取覆盖使 $\sum\limits_{i=1}^\infty\mu(E_i)<\mu^*(E)+\varepsilon$, 由
$$\mu(E)\leqslant\mu\left(\bigcup_{i=1}^\infty E_i\right)\leqslant\sum_{i=1}^\infty\mu(E_i)<\mu^*(E)+\varepsilon$$
即得 $\mu^*(E)=\mu(E)$

性质14-20 测度的基本性质
设 $\mu$ 为环 $\mathcal{R}$ 上的测度, 则
(1) 单调性 $\mu(E)\leqslant\mu(F)$, $\forall E,F\in\mathcal{R}$, $E\subset F$;
(2) 有限可加性 $\mu\left(\bigcup\limits_{i=1}^nE_i\right)=\sum\limits_{i=1}^n\mu(E_i)$, 要求各 $E_i$ 互不相交;
(3) 次可列可加性 $\mu\left(\bigcup\limits_{i=1}^\infty E_i\right)\leqslant\sum\limits_{i=1}^\infty\mu(E_i)$, 要求 $\bigcup\limits_{i=1}^\infty E_i\in\mathcal{R}$;
(4) 单调上升集列的测度, 如 $E_1\subset E_2\subset\cdots$ 且 $\bigcup\limits_{i=1}^\infty E_i\in\mathcal{R}$, 则
$$\mu\left(\bigcup_{i=1}^\infty E_i\right)=\lim_{i\to\infty}\mu(E_i)$$
(5) 单调下降集列的测度, 如 $E_1\supset E_2\supset\cdots$, $\bigcap\limits_{i=1}^\infty E_i\in\mathcal{R}$ 且 $\mu(E_{i^*})<+\infty$, 则
$$\mu\left(\bigcap_{i=1}^\infty E_i\right)=\lim_{i\to\infty}\mu(E_i)$$
(6) 可减性, 如 $E\subset F$ 且 $\mu(E)<+\infty$, 则 $\mu(F-E)=\mu(F)-\mu(E)$
证明 (1) 由 $F=(F\cap E)\cup(F-E)$ 且两项不交, 按有限可加性与非负性得
$$\mu(F)=\mu(E)+\mu(F-E)\geqslant\mu(E)$$
(2) 在可列可加性中取 $E_i=\varnothing$, $i>n$, 并注意 $\mu(\varnothing)=0$
(3) 作 $F_1=E_1$ 与 $F_i=E_i-\bigcup\limits_{j=1}^{i-1}E_j$, 则各 $F_i$ 互不相交且 $\bigcup\limits_{i=1}^\infty F_i=\bigcup\limits_{i=1}^\infty E_i$, 按可列可加性与单调性有
$$\mu\left(\bigcup_{i=1}^\infty E_i\right)=\sum_{i=1}^\infty\mu(F_i)\leqslant\sum_{i=1}^\infty\mu(E_i)$$
(4) 作 $F_1=E_1$ 与 $F_i=E_i-E_{i-1}$, 则 $\bigcup\limits_{i=1}^nF_i=E_n$, 故
$$\mu\left(\bigcup_{i=1}^\infty E_i\right)=\sum_{i=1}^\infty\mu(F_i)=\lim_{n\to\infty}\mu(E_n)$$
(5) 作 $F_i=E_1-E_i$, 则 $F_1\subset F_2\subset\cdots$ 且 $\bigcup\limits_{i=1}^\infty F_i=E_1-\bigcap\limits_{i=1}^\infty E_i$, 按 (4) 与可减性得
$$\mu(E_1)-\mu\left(\bigcap_{i=1}^\infty E_i\right)=\mu(E_1)-\lim_{i\to\infty}\mu(E_i)$$
(6) 由 $F=E\cup(F-E)$ 且两项不交, 按有限可加性即得

性质14-21 区间的 Lebesgue-Stieltjes 测度
按上述测度, 有
$$|\{a\}|_\mu=g(a)-g(a-0)$$
$$|(a,b)|_\mu=g(b-0)-g(a)$$
$$|[a,b]|_\mu=g(b)-g(a-0)$$
$$|[a,b)|_\mu=g(b-0)-g(a-0)$$
证明 由 $\{a\}=\bigcap\limits_{n=1}^\infty\left(a-\dfrac{1}{n},a\right]$ 为单调下降集列且 $|(a-1,a]|_\mu=g(a)-g(a-1)<+\infty$, 按性质14-20 有
$$|\{a\}|_\mu=\lim_{n\to\infty}\left[g(a)-g\left(a-\dfrac{1}{n}\right)\right]=g(a)-g(a-0)$$
再由测度的可加性与可减性得
$$|(a,b)|_\mu=|(a,b]|_\mu-|\{b\}|_\mu=g(b)-g(a)-g(b)+g(b-0)=g(b-0)-g(a)$$
$$|[a,b]|_\mu=|(a,b]|_\mu+|\{a\}|_\mu=g(b)-g(a)+g(a)-g(a-0)=g(b)-g(a-0)$$
$$|[a,b)|_\mu=|\{a\}|_\mu+|(a,b)|_\mu=g(a)-g(a-0)+g(b-0)-g(a)=g(b-0)-g(a-0)$$
上述结论给出数轴上任意形式的有界区间的 Lebesgue-Stieltjes 测度, 已具有实际使用价值

## 建立方式

(1) 结合实际使用的背景, Riemann 可积性定义为部分和的极限
设定部分和极限存在, 则可获得被积函数必有界的必要性结论
分析上可按正向方式获得被积函数的界的估计

(2) 基于可积性对有界性的要求, 将被积函数限定于有界函数的范畴
由此定义 Darboux 大和与小和, 并按确界的基本性质建立和谐式估计
以此为 Riemann 积分的分析理论奠定基础
基于和谐式估计获得两个基础极限, 即分割的模趋于零时大和与小和分别以各自的确界为极限
对任意闭区间上的有界函数这两个极限都存在, 可视为有界性的内蕴刻画

(3) 结合可积性的定义获得其等价性刻画
Darboux 大和的下确界等于 Darboux 小和的上确界, 可视为可积性的内蕴刻画
按极限的运算性质, 该等式对应于分割的模趋于零时振幅和以零为极限
此结论是判定可积性的重要分析方法
另一方面建立 Riemann 可积性的 Riemann 判别法, 据此确定连续函数复合于可积函数仍可积
基于振幅和极限趋于零的判别法与 Riemann 判别法都是充分必要的判别法

(4) 基于上述两个判别法获得基本的 Riemann 可积函数类
连续函数与单调函数可积, 可积函数对四则运算封闭, 且绝对可积