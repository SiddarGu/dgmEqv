
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.arange(4)
y1 = [120, 110, 100, 150]
y2 = [130, 140, 120, 170]
y3 = [90, 100, 80, 110]
ax.bar(x - 0.2, y1, width=0.2, label="Food bank")
ax.bar(x, y2, width=0.2, label="Homeless shelter")
ax.bar(x + 0.2, y3, width=0.2, label="Animals shelter")
ax.set_xticks(x)
ax.set_xticklabels(["USA","UK","Germany","France"])
ax.legend()
ax.set_title("Number of charitable organizations in four countries in 2021")
for a,b in zip(x-0.2, y1):
    ax.annotate(str(b), xy=(a,b+0.5), ha='center')
for a,b in zip(x, y2):
    ax.annotate(str(b), xy=(a,b+0.5), ha='center')
for a,b in zip(x+0.2, y3):
    ax.annotate(str(b), xy=(a,b+0.5), ha='center')
plt.figure(figsize=(10,6))
plt.savefig('Bar Chart/png/118.png')
plt.tight_layout()
plt.clf()