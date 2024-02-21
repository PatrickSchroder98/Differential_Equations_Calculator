class RungeKutta:

    def RungeKutta1(self, F, X, Y1, n, h):

        for i in range(n):
            k1 = h * F(X[i], Y1[i])

            X.append(X[i] + h)
            Y1.append(Y1[i] + k1)

    def RungeKutta2(self, F, X, Y1, n, h):

        for i in range(n):
            k1 = h * F(X[i], Y1[i])
            k2 = h * F(X[i] + (2.0 / 3.0) * h, Y1[i] + (2.0 / 3.0) * k1)

            X.append(X[i] + h)
            Y1.append(Y1[i] + (0.25 * k1) + (0.75 * k2))

    def RungeKutta3(self, F, X, Y1, n, h):
        for i in range(n):
            k1 = h * F(X[i], Y1[i])
            k2 = h * F(X[i] + 0.5 * h, Y1[i] + 0.5 * k1)
            k3 = h * F(X[i] + 0.75 * h, Y1[i] + 0.75 * k2)

            X[i + 1] = X[i] + h
            Y1[i + 1] = Y1[i] + ((2.0 / 9.0) * k1) + ((1.0 / 3.0) * k2) + ((4.0 / 9.0) * k3)

    def RungeKutta4(self, F, X, Y1, n, h):

        for i in range(n):
            k1 = h * F(X[i], Y1[i])
            k2 = h * F(X[i] + 0.5 * h, Y1[i] + 0.5 * k1)
            k3 = h * F(X[i] + 0.5 * h, Y1[i] + 0.5 * k2)
            k4 = h * F(X[i] + h, Y1[i] + k3)

            X[i + 1] = X[i] + h
            Y1[i + 1] = Y1[i] + (1.0 / 6.0) * (k1 + (2.0 * k2) + (2.0 * k3) + k4)

    def RungeKutta5(self, F, X, Y1, n, h):

        for i in range(n):
            k1 = h * F(X[i], Y1[i])
            k2 = h * F(X[i] + 0.25 * h, Y1[i] + 0.25 * k1)
            k3 = h * F(X[i] + 0.25 * h, Y1[i] + 0.125 * k1 + 0.125 * k2)
            k4 = h * F(X[i] + 0.5 * h, Y1[i] - 0.5 * k2 + k3)
            k5 = h * F(X[i] + 0.75 * h, Y1[i] + 0.1875 * k1 + 0.5625 * k4)
            k6 = h * F(X[i] + h, Y1[i] - (3.0 / 7.0) * k1 + (2.0 / 7.0) * k2 + (12.0 / 7.0) * k3 - (12.0 / 7.0) * k4 + (
                        8.0 / 7.0) * k5)

            X[i + 1] = X[i] + h
            Y1[i + 1] = Y1[i] + (1.0 / 90.0) * (7.0 * k1 + 32.0 * k2 + 12.0 * k4 + 32.0 * k5 + 7.0 * k6)

    def RungeKutta6(self, F, X, Y1, n, h):

        for i in range(n):
            k1 = h * F(X[i], Y1[i])
            k2 = h * F(X[i] + (1.0 / 9.0) * h, Y1[i] + (1.0 / 9.0) * k1)
            k3 = h * F(X[i] + (1.0 / 6.0) * h, Y1[i] + (1.0 / 24.0) * (k1 + k2))
            k4 = h * F(X[i] + (1.0 / 3.0) * h, Y1[i] + (1.0 / 6.0) * (k1 - 3.0 * k2 + 4.0 * k3))
            k5 = h * F(X[i] + (1.0 / 2.0) * h, Y1[i] + (1.0 / 8.0) * (k1 + 3 * k4))
            k6 = h * F(X[i] + (2.0 / 3.0) * h,
                       Y1[i] + (1.0 / 3.0) * (-4.0 * k1 - 21.0 * k2 + 46.0 * k3 - 29.0 * k4 + 10.0 * k5))
            k7 = h * F(X[i] + (5.0 / 6.0) * h,
                       Y1[i] + (1.0 / 72.0) * (-8.0 * k1 + 99.0 * k2 - 84.0 * k3 + 44.0 * k5 + 9.0 * k6))
            k8 = h * F(X[i] + h, Y1[i] + (1.0 / 82.0) *
                       (107.0 * k1 - 234.0 * k2 + 354.0 * k4 - 172.0 * k5 - 36.0 * k6 + 72.0 * k7),)

            X[i + 1] = X[i] + h
            Y1[i + 1] = Y1[i] + (1.0 / 840.0) * (41.0 * (k1 + k8) + 216.0 * (k3 + k7) + 27.0 * (k4 + k6) + 272.0 * k5)
