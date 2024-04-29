
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12,6))

x = np.array([2019, 2020, 2021, 2022, 2023])
y1 = np.array([30, 40, 50, 60, 70])
y2 = np.array([50, 60, 70, 80, 90])
y3 = np.array([80, 90, 100, 110, 120])

plt.plot(x, y1, marker='o', markersize=10, label='Donation A (million dollars)')
plt.plot(x, y2, marker='s', markersize=10, label='Donation B (million dollars)')
plt.plot(x, y3, marker='^', markersize=10, label='Donation C (million dollars)')

plt.xticks(x)
plt.title('Annual Global Donations to Nonprofit Organizations')
plt.xlabel('Year')
plt.ylabel('Donation (million dollars)')
plt.legend(loc='upper left', fontsize=10, ncol=3)
plt.tight_layout()

plt.savefig('line chart/png/470.png')

plt.clf()