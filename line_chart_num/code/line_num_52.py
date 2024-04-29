
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[4000, 5000], [4500, 3500], [3000, 5000], [3500, 4000]])

country = np.array(['US', 'Canada', 'UK', 'Germany'])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

for i in range(len(data)):
    ax.plot(data[i], label=country[i])

plt.xticks(np.arange(2), ["Music Download (million unit)", "Music Streaming (million unit)"])

plt.title('Music distribution in four major countries in 2021')

for i in range(len(data)):
    for j in range(2):
        ax.annotate(str(data[i,j]), xy=(j, data[i,j]))

plt.legend(loc=3, bbox_to_anchor=(1, 0))
plt.grid()
plt.tight_layout()

plt.savefig('line chart/png/413.png')
plt.cla()