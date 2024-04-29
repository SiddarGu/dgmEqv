
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[100000, 200000, 400000, 600000, 800000], 
        [150000, 250000, 400000, 550000, 700000], 
        [130000, 230000, 370000, 500000, 650000], 
        [80000, 160000, 270000, 380000, 450000], 
        [120000, 220000, 330000, 460000, 600000]]
outliers = [np.empty(0), 
            np.array([1000000]), 
            np.array([110000]), 
            np.array([800000]), 
            np.array([400000])]

# Plot the data with the type of box plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5)

# Plot outliers manually
for i, outlier in enumerate(outliers):
    if len(outlier):
        ax.plot(np.full(len(outlier), i+1), outlier, "o")

# Add background grids
ax.yaxis.grid(True)
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xticklabels(["Single Family Home", "Condo", "Townhouse", "Apartment", "Co-op"])
ax.set_ylabel("Price (USD)")
ax.set_title("Price Distribution of Housing Types in Real Estate Market (2020)")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/31_202312251608.png")
plt.clf()