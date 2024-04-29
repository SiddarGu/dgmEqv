
import matplotlib.pyplot as plt
import numpy as np

data = [[400, 500, 600, 800, 1200], [200, 300, 400, 500, 700], [400, 600, 800, 1000, 1500], [300, 400, 500, 600, 800], [30, 50, 70, 100, 150]]
outlier = [[], [900, 1000], [2, 1800, 1900], [1000, 1100], [200, 250]]

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111)
# Set the whisker as 1.5
ax.boxplot(data, whis=1.5)
ax.set_title('Price Distribution of Technology and Internet Devices (2022)', fontsize=15)
ax.set_ylabel('Price (USD)', fontsize=13)
ax.set_xticklabels(['Laptop', 'Smartphone', 'TV', 'Console', 'Router'], fontsize=13)
# Manually plotting the outliers
for i, out in enumerate(outlier):
    if not out:
        continue
    ax.plot([i + 1] * len(out), out, marker="o", color="r", ls="None")

# Set the grid
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# Adjust the label to prevent overlap
ax.tick_params(axis='x', labelrotation=45)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/6_202312251520.png')
plt.clf()