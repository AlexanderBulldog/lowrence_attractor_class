from dataclasses import dataclass

@dataclass
class Data:
  rho: float = 28.0
  sigma: float = 10.0
  beta: float = 8.0/3.0
  noise_x: float = 10.0
  noise_y: float = 10.0
  noise_z: float = 10.0
  t0: float = 0.0
  t_max: float = 10000.0
  dt: float = 0.01
  x0: float = 3.0  # Начальное значение x
  y0: float = 5.0  # Начальное значение y
  z0: float = 8.0  # Начальное значение z
