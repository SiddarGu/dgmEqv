import matplotlib.pyplot as plt
import numpy as np

# Decoding data
data = "Product Type,Min Production Time (Hours),Q1 Production Time (Hours),Median Production Time (Hours),"\
       "Q3 Production Time (Hours),Max Production Time (Hours),Outlier Production Time (Hours)"\
       "/n Electronics,5,7,10,13,17,[3,20]"\
       "/n Furniture,6,9,12,15,19,[]"\
       "/n Vehicles,7,11,15,18,22,[25]"\
       "/n Clothing,4,6,8,10,14,[1,2]"\
       "/n Cosmetics,3,5,7,9,12,[15,16]"
       
data = data.split("/n")
labels, stats, outliers = [], [], []

for row in data[1:]:
   split_row = row.split(",")
   labels.append(split_row[0])
   stats.append(list(map(int, split_row[1:6])))
   outliers.append(list(map(int, split_row[6][1:-1].split())) if split_row[6][1:-1] else [])

# Creating box chart
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot()

ax1.boxplot(stats, vert=False, patch_artist=True, whis=1.5)
ax1.set_yticklabels(labels, fontsize=10)
ax1.grid(True)
ax1.set_title("Product Production Time Distribution in Manufacturing Industries (2022)")
ax1.set_xlabel("Production Time (Hours)")

# Plotting outliers
for i, outlier in enumerate(outliers):
    if outlier:
        x = [i + 1] * len(outlier)
        ax1.plot(outlier, x, "ro")

# Save the image before clearing it
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/109_202312270030.png")
plt.clf()
