
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2020, 3000, 2200], [2021, 3200, 2500], [2022, 3300, 2700], [2023, 3100, 2800]])
x = data[:, 0]
y1, y2 = data[:, 1], data[:, 2]

fig, ax = plt.subplots(figsize=(10, 5))

bar_width = 0.3

ax.bar(x - bar_width/2, y1, width=bar_width, color='#377eb8', label='Energy Production(TWh)')
ax.bar(x + bar_width/2, y2, width=bar_width, color='#e41a1c', label='Energy Consumption(TWh)')

ax.set_title('Energy Production and Consumption in 2020-2023')
ax.set_xticks(x)
ax.set_xlabel('Year')
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('bar chart/png/63.png')
plt.clf()