import matplotlib.pyplot as plt
import numpy as np

# Data consisten of several categories
data = ["Apple,160,270,320,370,460,[]","Google,190,310,370,420,540,[700]","Facebook,120,240,300,360,450,[700,800]",
        "Amazon,200,340,400,460,560,[]","Microsoft,180,290,350,410,520,[680]"]

# Restructure the data into two 2D lists
numerical_data = []
outliers = []
for item in data:
    split_item = item.split(',')
    company = split_item[0]
    numerical_data.append([float(num) for num in split_item[1:6]])
    if split_item[6] != '[]':
        outlier_list = [float(num.replace('[','').replace(']','')) for num in split_item[6:]]
        outliers.append(outlier_list)
    else:
        outliers.append([])

# Plot the data with type of box plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.boxplot(numerical_data, whis=1.5, vert=False)
plt.yticks(np.arange(1, len(data) + 1), [item.split(',')[0] for item in data])

# Plot outliers for each category
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), 'ro')

# Add grid and mirror axes
ax.grid(True)
ax.yaxis.tick_left()
ax.xaxis.tick_bottom()
ax.xaxis.set_tick_params(width=1)
ax.yaxis.set_tick_params(width=1)

# Set the y-axis title with units
ax.set_xlabel('Revenue (Millions)')

# Set the figure title
plt.title('Revenue Distribution in Major Business Companies (2023)')

# Save the image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/90_202312270030.png')

# Clear the current image state
plt.clf()
