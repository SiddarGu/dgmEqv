
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2000,2500],[3000,3000],[3500,4000],[2800,3500]])
x = np.arange(4)
fig, ax = plt.subplots(figsize=(8,5))
bar1 = ax.bar(x-0.2, data[:,0], width=0.4, label="Crops(tons)")
bar2 = ax.bar(x+0.2, data[:,1], width=0.4, label="Vegetables(tons)")
ax.set_xticks(x)
ax.set_xticklabels(["East", "West", "North", "South"])
ax.legend()
ax.set_title("Crop and Vegetable Production in Four Regions in 2021")
plt.xticks(rotation=90, wrap=True)
plt.tight_layout()
plt.savefig("bar chart/png/13.png")
plt.clf()