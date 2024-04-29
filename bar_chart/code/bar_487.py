
import matplotlib.pyplot as plt
import numpy as np

data = [['East', 10, 4500],
        ['West', 15, 5000],
        ['South', 12, 4000],
        ['North', 17, 5500]]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

x_coordinates = np.arange(len(data))
width = 0.2
for i in range(len(data[0])-1):
    ax.bar(x_coordinates + width * i, [x[i+1] for x in data], 
           width, label=data[0][i+1])

plt.xticks(x_coordinates + width, [x[0] for x in data], 
           rotation=90, wrap=True)

ax.set_title("Number of hospitals and patients by region in 2021", fontsize=14)
ax.legend(loc="upper left")
fig.tight_layout()
plt.savefig("bar chart/png/561.png")
plt.clf()