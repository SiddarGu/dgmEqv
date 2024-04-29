
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[350,200], [400,220], [450,240], [320,210]])

region = np.array(['North America', 'Europe', 'Asia', 'Africa'])

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

plt.bar(region, data[:,0], label='Crops', width=0.4, bottom=data[:,1])
plt.bar(region, data[:,1], label='Livestock', width=0.4)
ax.set_title("Number of crops and livestock in four regions in 2021")

ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.0))
plt.xticks(rotation=90, wrap=True)

plt.tight_layout()
plt.savefig("bar chart/png/190.png")
plt.clf()