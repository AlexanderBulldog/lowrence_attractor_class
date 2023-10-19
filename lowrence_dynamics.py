import random
from lowrence_attractor.data import Data

class LowrenceDynamics: # Определение класса LowrenceDynamics, который будет использоваться для моделирования системы Лоренца.
    def __init__(self): # Создается объект класса Data, который содержит параметры и начальные условия системы Лоренца.
        data = Data()
        self.sigma = data.sigma # Эти строки устанавливают атрибуты класса, которые равны соответствующим параметрам из объекта Data.
        self.rho = data.rho 
        self.beta = data.beta 
        self.sigma_x = data.noise_x 
        self.sigma_y = data.noise_y
        self.sigma_z = data.noise_z
        self.dt = data.dt
        self.t0 = data.t0
        self.t_max = data.t_max
        self.x0 = data.x0
        self.y0 = data.y0
        self.z0 = data.z0

    def solve_lowrence(self, state): # Это метод класса, который решает уравнения Лоренца и возвращает новое состояние системы на основе текущего состояния state. 
        x, y, z = state
        dx = self.sigma * (y - x)
        dy = x * (self.rho - z) - y
        dz = x * y - self.beta * z
        
        noise_x = random.uniform(-self.sigma_x, self.sigma_x)
        noise_y = random.uniform(-self.sigma_y, self.sigma_y)
        noise_z = random.uniform(-self.sigma_z, self.sigma_z)
        
        x += (dx + noise_x) * self.dt
        y += (dy + noise_y) * self.dt
        z += (dz + noise_z) * self.dt

        return x, y, z