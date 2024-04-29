
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

x = np.array([2019, 2020, 2021, 2022, 2023])
y1 = np.array([200, 150, 100, 250, 200])
y2 = np.array([10, 8, 7, 9, 10])
y3 = np.array([5, 4, 3, 6, 5])

plt.plot(x, y1, color='blue', label='Number of Tourists')
plt.plot(x, y2, color='red', label='Hotel Revenue(billion dollars)')
plt.plot(x, y3, color='green', label='Restaurant Revenue(billion dollars)')
for a, b, c in zip(x, y1, y2):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.text(a, c, c, ha='center', va='bottom', fontsize=10)

plt.annotate('2023', xy=(2023, 200), xytext=(2023, 220),
             fontsize=10, arrowprops=dict(facecolor='black', shrink=0.05))

plt.xticks(x)
plt.yticks(np.arange(0, 350, 50))
plt.title('Tourism and Revenue in the travel industry from 2019 to 2023')
plt.xlabel('Year')
plt.legend(loc='best')
plt.grid(axis='y', linestyle='-.')

plt.tight_layout()
plt.savefig('line chart/png/60.png', dpi=60)
plt.clf()