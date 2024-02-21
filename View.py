import matplotlib.pyplot as plt

class View:

    def plot(self, title, legend, _Y, X, x_label, y_label):
        for Y in _Y:
            plt.plot(X, Y)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(legend)

        plt.show()