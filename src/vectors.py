import matplotlib.pyplot as plt

class Vector:
    scale = 5

    def __init__(self, x_component, y_component, color, x=0, y=0):
        self.x = x
        self.y = y
        self.x_component = x_component
        self.y_component = y_component
        self.color = color

    def __add__(self, vector):
        return Vector()