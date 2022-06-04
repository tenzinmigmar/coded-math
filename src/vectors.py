import matplotlib.pyplot as plt


class Vector:
    color_value = 0
    colors = ["coral", "rosybrown", "royalblue",
              "fuchsia", "mediumaquamarine",
              "lightgreen", "pink", "skyblue"]

    def __init__(self, x_component, y_component, x=0, y=0):
        self.x = x
        self.y = y
        self.x_component = x_component
        self.y_component = y_component
        if Vector.color_value == 7:
            Vector.color_value = 0
        Vector.color_value += 1
        self.color = Vector.colors[Vector.color_value]

    def __add__(self, vector):
        return Vector(self.x_component + vector.x_component,
                      self.y_component + vector.y_component)

    def __sub__(self, vector):
        return Vector(self.x_component - vector.x_component,
                      self.y_component - vector.x_component)


def plot_vectors(*args):
    x_pos = [arg.x for arg in args]
    y_pos = [arg.y for arg in args]
    x_direct = [arg.x_component for arg in args]
    y_direct = [arg.y_component for arg in args]
    colors = [arg.color for arg in args]

    fig, ax = plt.subplots()
    ax.quiver(x_pos, y_pos, x_direct, y_direct, color=colors, angles='xy', scale_units="xy", scale=1)

    plt.xlim([min(x_direct) - 5, max(x_direct) + 5])
    plt.ylim([min(y_direct) - 5, max(y_direct) + 5])
    plt.show()


vector1 = Vector(0, 1)
vector2 = Vector(1, 0)
vector3 = vector1 + vector2
vector4 = vector1 - vector2

plot_vectors(vector1, vector2, vector3, vector4)
