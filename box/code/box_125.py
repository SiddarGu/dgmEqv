import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
data = [
    ["Facebook", 100, 200, 300, 400, 500, []],
    ["Instagram", 150, 250, 350, 450, 550, [50, 600]],
    ["Twitter", 120, 220, 320, 420, 520, [25, 540]], 
    ["LinkedIn", 90, 190, 290, 390, 490, [700]], 
    ["Snapchat", 80, 180, 280, 380, 480, [640]] 
]

labels, min_val, q1, median, q3, max_val, outliers = zip(*data)

list_data = [list(a) for a in zip(min_val, q1, median, q3, max_val)]
outliers_list = list(outliers)

# Create the figure and axes
fig, ax = plt.subplots(figsize=(10,6))

# Boxplot
bplot = ax.boxplot(list_data, notch=True, vert=True, patch_artist=True, labels=labels, whis=1.5)

# Outlier plot
for i, outlier in enumerate(outliers_list):
    if outlier:
        ax.plot([i+1]*len(outlier), outlier, 'ko')

# Add grids and other styles
ax.yaxis.grid(True)
ax.xaxis.grid(True)

# Set titles and labels
ax.set_title('User Engagement Distribution on Social Media Platforms (2022)', fontsize=13)
ax.set_ylabel('User Engagement (Posts)', fontsize=13)
plt.xticks(rotation = 90)

# Save and show the figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/240_202312310058.png", dpi=300)

plt.show()

# Clear figure
plt.clf()
