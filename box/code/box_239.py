import matplotlib.pyplot as plt
import numpy as np

# Define the data
data = [["Immigration Policy", 5, 10, 15, 20, 25, []],
        ["Economic Policy", 3, 8, 12, 17, 22, [2, 30]],
        ["Health Policy", 6, 11, 15, 19, 24, [5, 28]],
        ["Education Policy", 5, 9, 14, 19, 24, [7, 32]],
        ["Environmental Policy", 7, 12, 16, 21, 26, [33]]]

# Separate the categories, values and the outliers
categories = [i[0] for i in data]
values = [i[1:6] for i in data]
outliers = [i[6] for i in data]

# Create the figure and the axes
fig, ax = plt.subplots(figsize=(10, 8))

# Create the box plot
bp = ax.boxplot(values, widths = 0.4, whis=1.5)

# Add outliers manually
for i, outlier in enumerate(outliers):
    if outlier: # Check if there are outliers
        ax.plot([i + 1] * len(outlier), outlier, "x")

# Add grid, title and labels
ax.set_title("Approval Duration of Government Policies (2020-2025)")
ax.set_ylabel("Approval Duration (Days)")
plt.xticks(np.arange(1, len(categories)+1), categories, rotation=45, ha='right')
ax.yaxis.grid(True)

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/197_202312310058.png')

# Clear the current figure
plt.clf()
