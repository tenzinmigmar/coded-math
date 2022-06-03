import matplotlib.pyplot as plt

class Vector:
    scale = 1

    def __init__(self, x_component, y_component, x=0, y=0):
        self.x = x
        self.y = y
        self.x_component = x_component
        self.y_component = y_component

    def __add__(self, vector):
        return Vector(self.x_component + vector.x_component,
                      self.y_component + vector.y_component)

    def __sub__(self, vector):
        return Vector(self.x_component - vector.x_component,
                      self.y_component - vector.x_component)


vector1 = Vector(1, 1)
vector2 = Vector(1, 2, 1, 2)
vector3 = vector1 + vector2

fig, ax = plt.subplots()

x_pos = [vector1.x, vector2.x, vector3.x]
y_pos = [vector1.y, vector2.y, vector3.y]
x_direct = [vector1.x_component, vector2.x_component, vector3.x_component]
y_direct = [vector1.y_component, vector2.y_component, vector3.y_component]

ax.quiver(x_pos, y_pos, x_direct, y_direct, angles='xy', scale_units='xy', scale=1)
plt.xlim([0, 5])
plt.ylim([0, 5])

plt.show()

print(vector3.x_component, vector3.y_component)