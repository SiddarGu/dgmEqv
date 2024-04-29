
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))
plt.title('Carbon Emission and Renewable Energy Consumption in the US from 2020 to 2024')

x = np.array([2020, 2021, 2022, 2023, 2024])
y1 = np.array([4500, 4800, 5000, 5500, 6000])
y2 = np.array([20, 25, 30, 35, 40])

plt.plot(x, y1, label='Carbon Emission(tons/year)')
plt.plot(x, y2, label='Renewable Energy Consumption(%)')

plt.xticks(x)
plt.xlabel('Year')
plt.ylabel('Values')

plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/140.png')
plt.clf()