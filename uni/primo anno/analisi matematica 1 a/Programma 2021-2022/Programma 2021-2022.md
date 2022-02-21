# Programma 2021-2022
### Principali insiemi numerici. 
I principali insiemi numerici sono 
- $\mathbb{N}$, ovvero l'insieme dei numeri naturali;
- $\mathbb{Z}$, ovvero l'insieme dei numeri interi;
- $\mathbb{Q}$, ovvero l'insieme dei numeri razionali:
$$\mathbb{Q}=\left\{\frac{m}{n}\quad\text{t.c.}\quad m \in \mathbb{Z}, n \in \mathbb{N}\setminus\{0\}\right\}$$
- $\mathbb{R}$, ovvero l'insieme dei numeri reali.
### La radice di due non è un numero razionale.
Dimostrazione 1.

### Insiemi limitati, maggioranti e minoranti, massimo e minimo. 
Un sottoinsieme $A$ di un insieme totalmente ordinato ($U, \leq$) è detto **limitato superiormente** se $$\exists\, k \in U\,|\, \forall\, a \in A, \: a\leq k$$
Un sottoinsieme $A$ di un insieme totalmente ordinato ($U, \leq$) è detto **limitato inferiormente** se $$\exists\, h \in U\,|\, \forall\, a \in A, \: h\leq a$$
- $k$ è detto **maggiorante** di $A$, mentre $h$ è detto **minorante** di $A$;
- se $k\in A$, $k$ è detto **massimo**, se $h \in A$, $h$ è detto **minimo**.

### Estremo superiore, estremo inferiore. 
Dato un insieme $A$ limitato:
- se $A$ è limitato superiormente, allora si dice $s=\sup A$ l'estremo superiore di $A$, ovvero **il più piccolo dei maggioranti**;
- se $A$ è limitato inferiormente, allora si dice $i=\inf A$ l'estremo inferiore di $A$, ovvero **il più grande dei minoranti**.

Se esiste, il massimo è unico e coincide con l'estremo superiore. Se esiste, il minimo è unico e coincide con l'estremo inferiore.

### Assioma di completezza. 
In $\mathbb{Q}$ non tutti gli insiemi limitati ammettono estremo superiore ed estremo inferiore. Per costruire l'insieme $\mathbb{R}$, quindi, si postula l'**assioma di completezza**, che afferma che qualsiasi sottoinsieme di $\mathbb{R}$
- se limitato superiormente ammette estremo superiore in $\mathbb{R}$;
- se limitato inferiormente ammette estremo inferiore in $\mathbb{R}$.
 
### Proprietà caratteristiche dell'estremo superiore.
Dato $A$ insieme limitato superiormente, vale
$$s=\sup A\quad \iff\quad \begin{cases}
	\forall\, x \in A,\: a\le s\\
	\forall\,\varepsilon>0 \: \exists\, x\in A: s-\varepsilon<x\le s
\end{cases}$$
### Esistenza della radice quadrata.
Dimostrazione 2.
$$\sqrt{a}=\sup\left\{x \in \mathbb{R}: x\ge 0, x^2<a^2\right\}$$

### Prodotto scalare in $\mathbb{R}^n$. 
Il prodotto scalare è una funzione $$\langle\cdot,\cdot\rangle: \mathbb{R}^n\times\mathbb{R}^n\to \mathbb{R}$$ ed in particolare, dati $x=(x_1, \dots, x_n), y=(y_1,\dots, y_n)$: $$\langle x, y\rangle:= \sum_{i=1}^nx_iy_i$$
Valgono le seguenti proprietà:
1. $\langle x, x\rangle\ge 0$ e $\langle x, x\rangle=0\:\iff\: x=\underline{0}$
2. $\langle x,y\rangle=\langle y,x\rangle$
3. $\lambda\langle x, y\rangle= \langle \lambda x, y\rangle=\langle x,\lambda y\rangle$
4. $\langle x+y, z\rangle= \langle x, z\rangle+ \langle y,z\rangle$

### Norma in $\mathbb{R}^n$.
Si definisce **norma** di un vettore di $\mathbb{R}^n$ la funzione $$||\cdot||: \mathbb{R}^n\to \mathbb{R}$$ data da $$||x||=\sqrt{\langle x, x\rangle}$$ Se $x=(x_1, \dots, x_n)$, $$||x||=\sqrt{\sum_{i=1}^nx_i^2}$$
In $\mathbb{R}$, la norma coincide con il valore assoluto, infatti, dato $x \in \mathbb{R}$: $$||x||=\sqrt{x^2}=|x|$$
### Disuguaglianza di Cauchy-Schwarz.
Vale $$|\langle x,y\rangle|\le ||x||\cdot ||y||$$
### Disuguaglianza triangolare. 
Vale $$||x+y||\le ||x||+||y||$$
### La nozione di distanza in $\mathbb{R}$, $\mathbb{R}^2$, $\mathbb{R}^3$ e in $\mathbb{R}^n$
Dati due elementi di $\mathbb{R}^n$, $x, y \in \mathbb{R}^n$, si definisce una funzione distanza $d(x,y)$ una funzione che soddisfi le seguenti proprietà:
1. $d(x,y)\ge 0$ e $d(x,y)=0\:\iff\: x=y$ ;
2. $d(x,y)=d(y,x)$
3. $d(a,b)\le d(a,c)+d(c,b)$

In generale, in $\mathbb{R}^n$, dati $x=(x_1, \dots, x_n), y=(y_1,\dots, y_n)$ la funzione distanza è definita come $$d(x,y)=||x-y||=\sqrt{\sum_{i=1}^n(x_i-y_i)^2}$$
### Palle e sfere in $\mathbb{R}^n$.
Si definiscono i seguenti insiemi:
- disco aperto di raggio $r$$$D_r=\left\{x \in \mathbb{R}^n: ||x||<r\right\}$$
- disco chiuso di raggio $r$, centrato in $x_0$: $$\overline{D_r}=\left\{x \in \mathbb{R}^n: ||x||\le r\right\}$$
### Intorni e loro proprietà. 
Dato $x_0\in \mathbb{R}^n$, si definisce **intorno** (sferico) di $x_0$ di raggio $r$ l'insieme: $$B_r(x_0)=\left\{z\in\mathbb{R}^n: d(x_0, z)<r\right\}$$Valgono le seguenti proprietà:
1. $x\in B_r(x)$
2. $B_{r_1}(x)\cap B_{r_2}(x)$ è sempre un intorno di $x$;
3. dato $y \in B_r(x)$, $\exists B_s(y)$ tale che $B_s(y)\subseteq B_r(x)$;
4. se $x\neq y$ $\implies$ $\exists\: B_{r_1}(x), B_{r_2}(y)$ tali che $B_{r_1}(x)\cap B_{r_2}(y)=\emptyset$.
### Punti interni, punti esterni, punti di frontiera.
Dato $x_0 \in E$, $ E \subseteq \mathbb{R}^{n} $, si ha che 
- $ x_0 $ è punto interno se $ \exists r $ tale che $ B_{r}(x_0) \subseteq E  $;
- $ x_0 $ è punto esterno se $ x_0 $ è interno a $ E^{C} = \mathbb{R}^{n}\setminus E $;
- $ x_0 $ è di frontiera se $ x_0 $ non appartiene ne ad $ E $, ne ad $ E^{C} $.
### Insiemi aperti, insiemi chiusi e loro proprietà rispetto a unione e intersezione.
Un insieme $ E $ è **aperto** se $$
\forall\,x \in E, \exists\,r: B_{r}(x) \subseteq E $$.

Un insieme $E$ è **chiuso** se $ E^{C} $ è un insieme aperto. 

Valgono le seguenti proprietà:
1. se $H \subseteq P(\mathbb{R}^{n})$, tale che $ \forall\,A \in H $ vale $ A $ aperto, si ha che $\bigcup_{A \in H} A$ è un insieme aperto;
2. se $ H=\{A_{1}, \cdots, A_{k}  \} $ è una famiglia finita di insiemi aperti, vale che $\bigcap_{A_{i} } A_{i}$ è un insieme aperto;  
3. se $H \subseteq P(\mathbb{R}^{n})$, tale che $ \forall\,A \in H $ vale $ A $ chiuso, si ha che $\bigcap_{A \in H} A$ è un insieme chiuso;
4. se $ H=\{A_{1}, \cdots, A_{k}  \} $ è una famiglia finita di insiemi chiusi, vale che $\bigcup_{A_{i} } A_{i}$ è un insieme chiuso.

### Punti di accumulazione. 

Dato $ x_0 \in E $, $ E \subseteq \mathbb{R}^{n} $, $ x_0 $ è di accumulazione per $ E $ se 
$$
\forall\, \varepsilon : \exists\, y \in E, y\neq x_0, y \in B_{ \varepsilon} (x_0)
$$

In ogni intorno di un punto di accumulazione per $ E $ ci sono infiniti punti di $ E $.

### Proprietà equivalenti al fatto di essere chiuso. 
Dimostrazione 3.

Sono fatti equivalenti:
1. $ E $ è un insieme chiuso;
2. la frontiera di $ E $ è sottoinsieme di $ E $;
3. tutti i punti di accumulazione per $ E $ sono interni ad $ E$.
### Chiusura di un insieme. 
La chiusura di un insieme è definita come $$\overline{E}=\partial E\cup E$$

### Il teorema di Bolzano-Weierstrass. 
Dimostrazione 8.

Dato $ E \subseteq \mathbb{R}^{n} $, $ E $ limitato e $ E $ infinito 

$\implies$ $ E $ ammette almeno un punto di accumulazione. 
### La retta estesa.
Si definisce l'insieme $ \mathbb{R}^{*} $, $$\mathbb{R}^{*}:=\mathbb{R}\cup\{-\infty, + \infty\}$$

Su $ \mathbb{R}^{*} $ è definita una relazione d'ordine totale $ \le' $:
1. $ \forall\,x,y \in \mathbb{R} $, $ x\le' y $ $ \iff $ $ x\le y $;
2. $ \forall\,x \in \mathbb{R}^{*} $, $ - \infty\le x\le + \infty $

Si definiscono gli intorni di $ + \infty $ e di $ - \infty $ di ampiezza $ a> 0 $:
$$
I_a(+ \infty)=(a, + \infty) \cup {+ \infty}=(a, + \infty]
$$
$$
I_a(- \infty)=(- \infty, -a) \cup {- \infty}=[- \infty, -a)
$$
### Parte positiva e parte negativa. 
Data una qualsiasi funzione $ f: A\to B $, $ B \subseteq \mathbb{R} $, si definiscono 
$$
f_{+}(x):=\begin{cases}
	f(x) & f(x)\ge 0\\
	0 & f(x)<0
\end{cases} 
$$
$$
f_{+}(x)= \max{f(x), 0} = \frac{|f(x)|+f(x)}{2} 
$$
$$
f_{-}(x):=\begin{cases}
	-f(x) & f(x)\le 0\\
	0 & f(x)>0
\end{cases} 
$$
$$
f_{-}(x)= \max{-f(x), 0} = \frac{|f(x)|-f(x)}{2} 
$$
Vale inoltre
$$f=f_{+}-f_{-}  \qquad |f|=f_{+}+f_{-} $$
### Funzioni limitate. 
Una funzione $ f: D\to \mathbb{R} $ è limitata se l'insieme $ f(D) $ è limitato.
### Per le funzioni: estremo superiore, massimo, punti di massimo, estremo inferiore, minimo, punti di minimo. 
Data $ f:D\to \mathbb{R} $, si definisicono
- estremo superiore: $ \sup_{D}  f := \sup f(D) $
- massimo: $ \max_{D} f := \max f(D) $
- punto di massimo $ x_0 $:
	- locale: esiste un intorno di $ x_0 $, $ U(x_0)  $, tale per cui
	$$ \forall\,x \in U(x_0), f(x)\le f(x_0) $$
	- globale:
	$$ \forall\, x \in D, f(x)\le f(x_0) $$
- estremo inferiore: $ \inf_{D}  f := \inf f(D) $
- massimo: $ \min_{D} f := \min f(D) $
- punto di massimo $ x_0 $:
	- locale: esiste un intorno di $ x_0 $, $ U(x_0)  $, tale per cui
	$$ \forall\,x \in U(x_0), f(x)\ge f(x_0) $$
	- globale:
	$$ \forall\, x \in D, f(x)\ge f(x_0) $$

### Funzioni monotone.

Una funzione è monotona in un dato intervallo $I$ se su $I$ è (strettamente) crescente o decrescente. 
Crescente: 
$$ x_1<x_2 \,\implies\, f(x_1)\le f(x_2) $$
Strettamente crescente:
$$ x_1<x_2 \,\implies\, f(x_1)<f(x_2) $$
Decrescente: 
$$ x_1<x_2 \,\implies\, f(x_1)\ge f(x_2) $$
Strettamente decrescente:
$$ x_1<x_2 \,\implies\, f(x_1)>f(x_2) $$