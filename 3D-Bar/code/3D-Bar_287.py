import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Transform the provided data
y_values = ['Internet Users (Millions)', 'Mobile Users (Millions)', 'E-commerce Sales ($ bn)', 'Software Market ($ bn)']
x_values = [2019, 2020, 2021, 2022, 2023]
data = np.array([
    [4480, 5000, 3520, 512],
    [4590, 5120, 3890, 525],
    [4700, 5280, 4123, 540], 
    [4820, 5400, 4360, 560],
    [4940, 5550, 4615, 577]
], np.float32)

# Create figure and a 3D projection for the subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), dx=0.5, dz=data[:, i], dy=0.5, alpha=0.5)

# Set the dimensions of the bars (width, depth, colors, alpha, etc)
# Rotate the X-axis labels for better readability
plt.xticks(np.arange(len(x_values)), x_values, rotation=45)

# Use ax.set_xticks and ax.set_yticks to align the label position with data position
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))

# and label the axes.
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values, ha='left')

# Set the title of the figure
plt.title('Annual Technology and Internet Trends - 2019 to 2023')

# Save the image
fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/154_202312302235.png')

# Clear the current image state
plt.clf()
