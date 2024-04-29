

import matplotlib.pyplot as plt
import numpy as np

data = [['January',1000,1200],['February',1300,1500],['March',1400,800],['April',1600,1100],['May',1800,1000],['June',2000,1300],['July',2100,1600],['August',1800,1200],['September',1400,1000],['October',1200,1400],['November',1300,1800],['December',1500,2000]]
x, y1, y2 = np.array(data).T

plt.figure(figsize=(8,5))
ax = plt.subplot()
ax.plot(x, y1, color="b", linewidth=2, label="Online Sales")
ax.plot(x, y2, color="r", linewidth=2, label="Offline Sales")
ax.set_title("Online and Offline Sales of Retail Stores in 2021")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (million dollars)")
ax.legend(bbox_to_anchor=(1, 1), loc="upper left")
ax.grid(linestyle='--', linewidth=0.5)
ax.set_xticks(x)

for i,j in zip(x,y1):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(x,y2):
    ax.annotate(str(j),xy=(i,j))

plt.tight_layout()
plt.savefig('line chart/png/259.png')
plt.cla()