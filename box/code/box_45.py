
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[100, 200, 300, 400, 500],
        [150, 250, 350, 450, 550],
        [200, 300, 400, 500, 600],
        [50, 100, 150, 200, 250],
        [100, 150, 200, 250, 300]]

outliers = [[], [650], [700, 800], [300, 350], [350, 400]]
line_labels = ['Robotics', 'Automation', 'Artificial Intelligence', 'Biomedical Engineering', 'Nanotechnology']

# Plot the data with the type of box plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5)

# Manually plot the outliers
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot([i + 1] * len(outlier), outlier, "o")

# Add grid
ax.grid(ls="--", alpha=0.5)

# Set title, x-axis title, y-axis title
ax.set_title("Cost of Science and Engineering Technologies in 2021")
ax.set_xlabel("Technology")
ax.set_xticklabels(line_labels)

ax.set_ylabel("Cost (USD)")

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/22_202312251608.png")

# Clear the current image state
plt.clf()