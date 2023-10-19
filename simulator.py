import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from lowrence_attractor.lowrence_dynamics import LowrenceDynamics

class Simulator: # Определение класса который будет использоваться для симуляции и визуализации аттрактора Лоренца
    def __init__(self, dynamics, x0, y0, z0, t0, t_max): # Инициализация класса "Simulator"
        self.dynamics = dynamics
        self.x = x0
        self.y = y0
        self.z = z0
        self.t0 = t0
        self.t_max = t_max

    def simulate(self): # Метод класса 'Simulator' который выполняет симуляцию и визуализацию аттрактора
        t_values = np.arange(self.t0, self.t_max)
        x_values = []
        y_values = []
        z_values = []

        for t in t_values:
            x_values.append(self.x)
            y_values.append(self.y)
            z_values.append(self.z)

            self.x, self.y, self.z = self.dynamics.solve_lowrence((self.x, self.y, self.z))

        # Визуализируем аттрактор
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x_values, y_values, z_values, lw=0.5, color = 'darkmagenta')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Аттрактор Лоренца')
        plt.show()
