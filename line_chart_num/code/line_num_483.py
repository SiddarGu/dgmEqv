
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

x = np.array([2020, 2021, 2022, 2023, 2024])
y1 = np.array([400, 450, 420, 500, 430])
y2 = np.array([25, 27, 28, 30, 29])

ax.plot(x, y1, '-', linewidth=2, label='Average Rainfall (mm)')
ax.plot(x, y2, '--', linewidth=2, label='Average Temperatures (Celsius)')

ax.grid(True, linestyle='-.')
ax.legend(loc='upper left')

for a, b in zip(x, y1):
    ax.annotate('{}'.format(b), xy=(a, b+5))
for a, b in zip(x, y2):
    ax.annotate('{}'.format(b), xy=(a, b+0.5))

plt.xticks(x)
plt.title('Average Rainfall and Temperatures in the USA from 2020-2024')

plt.tight_layout()
plt.savefig('line chart/png/236.png', dpi=300)
plt.clf()