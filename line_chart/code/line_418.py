
import matplotlib.pyplot as plt
import numpy as np

data = [['00:00', 0, 0], ['01:00', 50, 50], ['02:00', 100, 50], ['03:00', 150, 50],
        ['04:00', 200, 50], ['05:00', 250, 50], ['06:00', 300, 50], ['07:00', 350, 50]]

x = np.array([i[0] for i in data])
y1 = np.array([i[1] for i in data])
y2 = np.array([i[2] for i in data])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.plot(x, y1, label="Distance(km)", marker='o', color='#FF9900')
ax.plot(x, y2, label="Speed(km/hr)", marker='o', color='#0066FF')

ax.set_title("Distance travelled and speed of a car on a highway on July 15th, 2023")
ax.set_xlabel("Time")
ax.set_ylabel("Distance(km) & Speed(km/hr)")
ax.grid(True)
ax.legend(loc="upper left")

plt.xticks(x, rotation=90, wrap=True)
fig.tight_layout()
plt.savefig('line chart/png/280.png')
plt.clf()