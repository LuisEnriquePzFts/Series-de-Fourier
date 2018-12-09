from sympy import *
from sympy.plotting.plot import plot
from sympy.abc import x
from sympy import Symbol

t = Symbol('t')
n = Symbol('n')

function = eval(input("Insertar los datos para f(x): "))
interval1 = eval(input("X1= "))
interval2 = eval(input("X2= "))

a0= 1/integrate(function, (t, interval1, interval2))

print("Los datos para a0 son:")
print(a0)
print("")
print("")
print("")
print("")

#an = integrate(function, (t, interval1, interval2))*cos(n, pi, x/t)
an = integrate((function) * cos(2*n*t), (t, interval1, interval2))
print("Los datos para an son: ")
print(an)

print("")
print("")
print("")
print("")
bn = (integrate((function) * sin(2*n*t), (t, interval1,interval2)))
print("Los datos para bn son:")
print(bn)

print ("\n"+"La Grafica es ")

armonicos = 50
serie= (a0/2)

for i in range(1, armonicos + 1):
    serie = serie + (an*cos(2*n*t)).subs(n, i)
for j in range(1, armonicos + 1):
    serie = serie + (bn*sin(2*n*t)).subs(n, j)
#pprint(serie)

plotting.plot3d(serie)

#plotting.plot(serie, ylim=(-0.5, 1.5), xlim=(-0.5,5))

