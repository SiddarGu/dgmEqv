

import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np

x_axis = np.arange(1, 6)
y1_axis = [500, 600, 800, 900, 1000]
y2_axis = [800, 900, 1000, 1200, 1400]
y3_axis = [1000, 1200, 1500, 1800, 2000]

plt.figure(figsize=(8, 5))

plt.plot(x_axis, y1_axis, marker='o', label='Electricity')
plt.plot(x_axis, y2_axis, marker='o', label='Gas')
plt.plot(x_axis, y3_axis, marker='o', label='Nuclear')

plt.xticks(x_axis, ['Jan','Feb','Mar','Apr','May'])
plt.title('Energy Generation in the United States in 2021')
plt.xlabel('Month')
plt.ylabel('Generation (kWh)')
plt.legend(loc='upper left', shadow=True, fontsize='large')
plt.tight_layout()

for i, j in zip(x_axis, y1_axis):
    plt.annotate(str(j), xy=(i-0.1, j+20))
for i, j in zip(x_axis, y2_axis):
    plt.annotate(str(j), xy=(i-0.1, j+20))
for i, j in zip(x_axis, y3_axis):
    plt.annotate(str(j), xy=(i-0.1, j+20))

plt.savefig("line chart/png/11.png")
plt.clf()