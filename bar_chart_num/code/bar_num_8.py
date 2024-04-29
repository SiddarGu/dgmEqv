
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[400, 250, 320], [380, 320, 300], [320, 370, 340], [350, 360, 430]])
Country = ["USA", "UK", "Germany", "France"]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

width = 0.2
x = np.arange(len(Country))

ax.bar(x, data[:, 0], width, label="Literature")
ax.bar(x + width, data[:, 1], width, label="Philosophy")
ax.bar(x + 2*width, data[:, 2], width, label="History")

ax.set_xticks(x + width)
ax.set_xticklabels(Country)
ax.set_title("Number of publications in Social Sciences and Humanities in four countries in 2021")
ax.legend(loc="upper right")

for i in range(len(x)):
    ax.annotate(data[i], (x[i] + width, data[i][1] + 5), va="center", ha="center")

plt.tight_layout()
plt.savefig('Bar Chart/png/225.png')
plt.clf()