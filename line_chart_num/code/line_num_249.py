
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1,1,1)

x = [2020, 2021, 2022, 2023, 2024, 2025]
y1 = [20, 25, 30, 35, 40, 45]
y2 = [3.5, 3.2, 2.8, 2.5, 2.2, 2.0]

ax.plot(x, y1, label="GDP (billion dollars)", marker='o', color='blue', linestyle='-')
ax.plot(x, y2, label="Unemployment Rate (%)", marker='o', color='orange', linestyle='-')

plt.xticks(np.arange(min(x), max(x)+1, 1.0))
ax.grid()
ax.legend(loc='best')
ax.set_title("Changes in GDP and Unemployment Rate in the US from 2020-2025")

for i,j in zip(x,y1):
    ax.annotate(str(j),xy=(i,j), color='blue')
for i,j in zip(x,y2):
    ax.annotate(str(j),xy=(i,j), color='orange')

plt.tight_layout()
plt.savefig('line chart/png/485.png')
plt.clf()