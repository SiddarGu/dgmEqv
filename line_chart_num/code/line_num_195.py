
import matplotlib.pyplot as plt
import numpy as np

year = np.array([2001, 2002, 2003, 2004])
fast_food = np.array([10, 12, 14, 16])
sit_down = np.array([20, 18, 16, 14])
delivery = np.array([5, 6, 8, 10])
take_out = np.array([15, 16, 18, 20])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.plot(year, fast_food, label="Fast Food", marker='o', markersize=8, color='blue')
ax.plot(year, sit_down, label="Sit-down Restaurant", marker='o', markersize=8, color='green')
ax.plot(year, delivery, label="Delivery", marker='o', markersize=8, color='yellow')
ax.plot(year, take_out, label="Take-out", marker='o', markersize=8, color='red')
ax.legend(loc='upper left')
ax.set_title("Food Industry Sales by Type of Service in 2001 - 2004")
ax.set_xlabel('Year')
ax.set_ylabel('Sales')
ax.set_xticks(year)

for i, j in zip(year, fast_food):
    ax.annotate('{:.1f}'.format(j), xy=(i, j), xytext=(i-0.3, j+1))
for i, j in zip(year, sit_down):
    ax.annotate('{:.1f}'.format(j), xy=(i, j), xytext=(i-0.3, j+1))
for i, j in zip(year, delivery):
    ax.annotate('{:.1f}'.format(j), xy=(i, j), xytext=(i-0.3, j+1))
for i, j in zip(year, take_out):
    ax.annotate('{:.1f}'.format(j), xy=(i, j), xytext=(i-0.3, j+1))

plt.tight_layout()
plt.savefig('line chart/png/96.png')
plt.clf()