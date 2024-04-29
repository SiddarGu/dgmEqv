
import matplotlib.pyplot as plt
import numpy as np

# data
region = ["North America", "Europe", "Asia", "South America"]
Air_Freight = [1000, 900, 1100, 800] 
Ground_Freight = [1500, 1300, 1400, 1500]
Water_Freight = [1200, 1100, 1200, 1400]

# plot
x_pos = np.arange(len(region))
width = 0.2
fig, ax = plt.subplots(figsize=(10,6))
ax.bar(x_pos-width, Air_Freight, width, label="Air Freight(tons)")
ax.bar(x_pos, Ground_Freight, width, label="Ground Freight(tons)")
ax.bar(x_pos+width, Water_Freight, width, label="Water Freight(tons)")

# labeling
ax.set_xticks(x_pos)
ax.set_xticklabels(region, fontsize=10)
ax.set_title("Freight transportation in four regions in 2021")
ax.legend(bbox_to_anchor=(1.04,1), loc="upper left")

# adding value labels
for i in ax.patches:
    ax.annotate(format(i.get_height()), (i.get_x()+i.get_width()/2., i.get_height()), ha='center', va='center', xytext=(0, 10), rotation=90, textcoords="offset points")

# adjust the figure
plt.tight_layout()

# save the file
plt.savefig("Bar Chart/png/217.png")

# clear the current image state
plt.clf()