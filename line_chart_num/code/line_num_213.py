
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2020, 2021, 2022, 2023])
y1 = np.array([10000, 11000, 12000, 13000])
y2 = np.array([40, 50, 60, 70])
y3 = np.array([80, 90, 85, 90])

plt.figure(figsize=(10,8))
plt.grid(linestyle='--')
plt.plot(x, y1, label='Electricity Consumption(kWh)', color='red', marker='o')
plt.plot(x, y2, label='Renewable Energy Sources(%)', color='blue', marker='o')
plt.plot(x, y3, label='Energy Efficiency Index', color='green', marker='o')

plt.xticks(x)
plt.legend(loc='best', fontsize=12)
plt.title('Progress on Renewable Energy and Energy Efficiency in the US', fontsize=14)


plt.tight_layout()
plt.savefig('line_213.png')
plt.clf()