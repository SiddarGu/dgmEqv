
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[40000,20,30],[45000,25,35],[50000,30,40],[55000,35,45]])
region = ["North America","South America","Europe","Asia"]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1,1,1)

ax.bar(region, data[:, 0], label="Pollution Level(tonnes)", color="green")
ax.bar(region, data[:, 1], bottom=data[:, 0], label="Renewable Energy(%)", color="blue")
ax.bar(region, data[:, 2], bottom=data[:, 0]+data[:, 1], label="Recycling(%)", color="yellow")

ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0., fontsize=10)
ax.set_title("Pollution level, renewable energy, and recycling data in four regions in 2021")
ax.set_xticklabels(region, rotation=45, ha="right", fontsize=10, wrap=True)
plt.tight_layout()
plt.savefig('bar chart/png/465.png')
plt.clf()