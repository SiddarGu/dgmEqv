import numpy as np
import matplotlib.pyplot as plt

# Data
data_str = """
2018,200,250,300,350
2019,220,275,325,380
2020,240,300,350,410
2021,260,325,375,440
2022,280,350,400,470
"""
data_lines = data_str.strip().split('\n')

x_values = [line.split(',')[0] for line in data_lines]
y_values = ['Education & Research ($M)', 'Health ($M)', 'Services & Advocacy ($M)', 'Art & Culture ($M)']
data = np.array([list(map(np.float32, line.split(',')[1:])) for line in data_lines])

# Create figure
fig = plt.figure(figsize=(12, 8))

# 3D projection for the subplot
ax = fig.add_subplot(111, projection='3d')

# Iterate to plot each column of data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.8, 0.8, data[:, i], shade=True)

# label x-axis and y-axis
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=90)
ax.set_yticklabels(y_values, ha='left')

# add a title
ax.set_title('Annual Funding Allocation Trends in Nonprofit Sectors (2018-2022)')

# Rotate the view angle for better view
ax.view_init(elev=30., azim=-60)

# Automatically adjust the subplot
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/261_202312310050.png", dpi=300)

# Clear the current image state
plt.clf()
