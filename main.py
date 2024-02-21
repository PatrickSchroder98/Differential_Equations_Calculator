import RungeKutta as RK
import Equation as E
import View as V

rk = RK.RungeKutta()
e = E.Equation()
v = V.View()

_Y = []

for func in (rk.RungeKutta1, rk.RungeKutta2, rk.RungeKutta3, rk.RungeKutta4, rk.RungeKutta5, rk.RungeKutta6):
    # Initial data
    X = [0]
    Y = [1]
    h = 0.1
    X_max = 1

    # Counting number of output points
    n = int((X_max - X[0]) / h)
    func(e.equation, X, Y, n, h)

    _Y.append(Y)

v.plot("Differential Equation Solutions", ["RK1", "RK2", "RK3", "RK4", "RK5", "RK6"], _Y, X, "X axis", "Y axis")

