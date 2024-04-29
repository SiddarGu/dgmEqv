
import matplotlib.pyplot as plt
import numpy as np

x_data = np.array([273, 300, 350, 400, 450, 500, 550, 600])
temperature = np.array([100, 150, 200, 250, 300, 350, 400, 450])
pressure = np.array([2, 3, 4, 6, 8, 10, 12, 14])

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot()
ax.plot(x_data, temperature, label='Temperature(Kelvin)', marker='o', linewidth=2, linestyle='--')
ax.plot(x_data, pressure, label='Pressure(kPa)', marker='o', linewidth=2, linestyle='--')
ax.legend(loc='upper right')
ax.set_title('Variation of temperature, pressure and density in air')
plt.xticks(x_data)
plt.tight_layout()
plt.savefig('line chart/png/291.png')
plt.clf()