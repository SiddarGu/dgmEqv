
import matplotlib.pyplot as plt
import numpy as np

# Define data
Region = np.array(["North", "South", "East", "West"])
Average_House_Price = np.array([1.5, 2.3, 1.8, 2.1])
Number_of_Houses_Sold = np.array([250, 320, 280, 300])

# Create a figure
fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(111)

# Plot data
ax.bar(Region, Average_House_Price, width=0.3, bottom=0, label="Average House Price (million)")
ax.bar(Region, Number_of_Houses_Sold, width=0.3, bottom=Average_House_Price, label="Number of Houses Sold")

# Label data
for i, j in enumerate(Average_House_Price):
    ax.annotate(str(j)+"\n"+str(Number_of_Houses_Sold[i]), xy=(i-0.15, j/2+Number_of_Houses_Sold[i]/2), rotation=90)

# Settings
ax.set_title("Average House Prices and Number of Houses Sold in Four Regions in 2021")
ax.set_xticks(np.arange(4))
ax.set_xticklabels(Region, rotation=-45, ha="left")
ax.set_yticks(np.arange(0, 4, 0.5))
ax.set_yticklabels(np.arange(0, 4, 0.5))
ax.legend(loc="upper left")

# Display
plt.tight_layout()
plt.savefig("Bar Chart/png/132.png")
plt.clf()