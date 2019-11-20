from random import randint
import random
from sympy import Symbol, symbols, Sum, latex, simplify, Rational

# Choose an integer that is actually interesting and can be both negative and positive
a = int((-1)**randint(0,1))*randint(2,5)

# Half the time, do fractions
if randint(0,1) == 1:
    a = Rational('{}/{}'.format(1, a))

# Choose random symbols for n and i
n_symbol = random.choice(["n", "m", "N"])
n = Symbol(n_symbol)
i_symbol = random.choice(["j", "i"])
i = Symbol(i_symbol)

# The sum of the a's
lhs = Sum(a**i, (i, 0, n))
# The sum as predicted with the recursive formula: x_n = a*x_{n-1} + 1 with x_0 = 1
rhs = simplify(a**n + (1-a**n)  / (1-a))

print("\\section{Lukket formel for $" + latex(lhs) + "$}")
print("\\subsection{Opgave}")
print("Bevis at:")
print("$${} = {} {} {} \geq 0$$\n".format( latex(lhs), latex(rhs), "\\text{ for }" , latex(n) ) )

zero = Symbol("0")
print("\\subsection{Bevis}")
print("Først vises base case, nemlig for ${}=0$.".format(n_symbol))
print("Altså skal vises $${} = {}$$".format( latex(lhs.subs(n, zero)), latex(rhs.subs(n,zero)) ))
print("Først beregnes venstre side:")
print("$${} = {} = 1$$".format( latex(lhs.subs(n,zero)), latex(a**zero)  ))
print("Da beregnes højre side:")
print("$${} = 1$$".format(latex( rhs.subs(n, zero)  ) ))
print("Da ses at begge sider er lig hinanden, hvorfor base case er bevist")
print("\nDa vises induktionsskridtet. Altså vises:")
print("$${} = {} \Rightarrow {} = {}$$".format( latex(lhs), latex(rhs), latex(lhs.subs(n, n+1)), latex(rhs.subs(n, n+1) )))
print("hvor ${} = {}$ er induktionshypotesen.".format( latex(lhs), latex(rhs) ))
print("Der omskrives fra induktionshypotesen:")
print("\\begin{align*}")

next_line = "\Rightarrow & {} = {}"
print("&{} = {}\\\\".format( latex(lhs), latex(rhs) ))
added = a**(n+1)
print(next_line.format( latex( added + lhs ), latex(  added + rhs) ))

print( " & \\text{(Læg " + "${}$".format(latex(added)) + " til.)}\\\\" )

print(next_line.format( latex( lhs.subs(n, n+1) ), latex(added + rhs) )  )
print(" & \\\\ &&\\text{(Da " + "${} = {}$".format(latex(added), latex(a * (a**n))) + " og fælles nævner.)}\\\\" ) 
print(next_line.format( latex( lhs.subs(n, n+1) ), latex( simplify(added + rhs)) ) + "\\\\"  )

print(next_line.format( latex(lhs.subs(n,n+1) ), latex( rhs.subs(n, n+1) ) ))
print("&(\\text{Da " + "$({})^{} = {}$)".format( a,2, a**2  )  + "}" )


print("\\end{align*}")

print("Dermed er induktionsskridtet vist og det konkluderes at ${} = {}$ for alle ${}\geq 0$".format(latex(lhs), latex(rhs), n_symbol))
