import RungeKutta as RK
import Equation as E

rk = RK.RungeKutta()
e = E.Equation()

# Initial data
X = [0]
Y = [1]
h = 0.1

X_max = 1

# Counting number of output points
n = int((X_max - X[0])/h)

rk.RungeKutta6(e.equation, X, Y, n, h)

print(Y)