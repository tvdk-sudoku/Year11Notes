#### Introduction

- Proofs demonstrate the absolute truth of a statement, and should aim to achieve three things

      - Correctness

      - Clarity

      - Simplicity

- In proving statements, we should know some basic algebraic representations

	 - `Even numbers` -  *$2m$ for some $m \in \mathbb{Z}$*

     - `Odd numbers` - *$2m + 1$ for some $m \in \mathbb{Z}$*

     - `Divisible by `$a$ -  *$am$ for some $m \in \mathbb{Z}$*

     - `Perfect Square` - *There exists* $a^2$ *for some* $a \in \mathbb{Z}$

     - `Prime` - *There does not exist* $ab$ *for some* $a,b \in \mathbb{Z}$ *and* $a,b>1$

- There are different ways to prove a statement, these are discussed below




#### Direct Proof

##### Reasoning

- Direct proofs are in response to conditional statements, for example

      - `If it is raining, then the grass is wet`

      - In the form `If P is true, then Q is true`

      - This is mathematically represented $P \implies Q$ (`P` implies `Q`)

            - `P` is the hypothesis, and `Q` is the conclusion

- Not all conditional statements are true.

  

##### The Proof

- To give a **direct** proof of a statement $P \implies Q$, we must assume the hypothesis (P) to be true and show the conclusion (Q)

- **Example**

      - `If a is odd and b is even, then a + b is odd`

      - $let \space a = 2n+1 \space for \space some \space n \in \mathbb{Z}$ (we must include for some)

      - $let \space b=2m \space for \space some \space b \in \mathbb{Z}$ (second definition)

      - $a+b=2n+1+2m$

      - $=2(n+m)+1$; this is in the odd form ([[#Introduction]]) - we must complete that however by stating $for \space some \space n+m \in \mathbb{Z}$

      - $\therefore Q.E.D$; from above it is obviously proved, but we should wrap it up - **Q.E.D essentially means** *it is proved, as you can obviously see*

- There may be more complex examples

      - These will require **factorisation** and algebraic manipulation, and expanded reasoning

      - The logic stays the same though

      - **Knights and Knaves** questions will almost always require the consideration of *all cases*

  

#### Proof by Contrapositive

##### Reasoning

- Sometimes it is difficult to prove $P \implies Q$ through direct proof; consider

      - `If ` $n^{2}+2n+1$ `is even then ` $n$ `is odd`  

      - We can't assume `P` ($n^{2}+2n+1$) because it is difficult to define

      - However we can use the contrapositive

- **The contrapositive of** $P \implies Q$ is $Q' \implies P'$ (the **negated things in the opposite order**

  

###### Negation

- Making something opposite is called **negation** - the negation of $1+1=2$ is $1+1 \not = 2$

      - We can, however, encounter more difficult negations.

      - Consider `negation of (6 is divisible by 2 and 3)`

      - We can use De morgan's laws for this

            - `not (P and Q) is the same as (not P) or (not Q)`

            - `not (P or Q) is the same as (not P) and (not Q)`

      - Therefore the above becomes `6 is not divisible by 2 or 6 is not divisible by 3`

  

###### Using Negation for the Contrapositive

- For the above, `If ` $n$ `is even then ` $n^{2}+2n+1$ `is odd`

- **If the original P => Q is true, it's contrapositive will always be true, and vice versa**

      - The above is therefore true and can be directly proved

  

##### Proof

- Let us consider the above; `If ` $n^{2}+2n+1$ `is even then ` $n$ `is odd`

      - First, we should negate both sides and flip them - writing the contrapositive

      - This is `If ` $n$ `is even then ` $n^{2}+2n+1$ `is odd` in the form $P \implies Q$

      - $let \space n = 2a \space for \space some \space a \in \mathbb{Z}$

      - $n^{2}+2n+1 = (2a)^{2}+2(2a)+1$

      - $=4a^2+4a+1$; getting us into even number accounted form

      - $=2(a^{2}+2a)+1$; it may seem like we are doing little but this puts us in the traditional odd form

            - $for \space some  \space a^{2}+2a \in \mathbb{Z}$

      - $\therefore Q.E.D$

  

#### Equivalence Proofs

##### Reasoning

- Equivalent Statements are given in the form $P \iff Q$

      - To prove equivalence though, we must first prove a statement **and** [[#The converse]]

- In written form, $P \iff Q$ is `P is true if and only if Q is true`, for example;

      - `Your heart is beating if and only if you are alive` (this is an equivalent statement)

- If a question includes `if and only if`, remember to consider both cases

      - To indicate the case being proven, write $\implies$ or $\impliedby$

  

##### The converse

- If a statement $P \implies Q$ exists, then the converse is simply $Q \implies P$

      - i.e the contrapositive with less steps

  

#### Disproving of Statements

##### Reasoning

- In general, when **disproving** statements, we only need **one example**

- There are, however, two types of statements you may have to disprove;

      - **Universal Quantification** (also known as *for all*).

            - `For all natural numbers n, 2n > n + 1`

            - The above statement can only be **proved** by providing an argument concerning all natural numbers *n*

      - **Existential Quantification** (also known as *there exists*)

            - `There exists an integer m such that m^2 = 25`

            - Due to the nature of this statement, we only need one integer *m* to **prove** the statement

      - Both of these statements involve quantifiers. In order to disprove, we should know [[#Negating Quantifiers]]

  

##### Negating Quantifiers

- To negate quantifiers, we just swap 'there exists' and 'for all' and then *negate the rest of the statement*

      - `For all natural numbers n, 2n > n+1` $\rightarrow$ `There exists natural number n such that 2n < n + 1`

      - And vice versa.

  

##### Disproving

- **Universal Quantifications**

      - Can be disproved via `counterexample` - this is because it asserts truth without exception.

- **Existential Quantification**

      - This is different - because this involves a *there exists* (truth with exceptions), we must prove that there does not exist at all

		- Due to this, we must prove **the negation to be true** ([[#Negating Quantifiers]])


##### Proof by Induction
	- State the Proposition: P(n)
	- Try for P(1)
	- Assume P(k)
	- Try for P(k+1)


$7^{k} - 4 = 3m$
$7^{k+1}-4 = 7(7^{k}-4)+24$
			 $= 7(3m)+24$
			 $=3(7m+8)$





