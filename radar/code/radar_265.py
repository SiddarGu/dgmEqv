import numpy as np
import matplotlib.pyplot as plt

# the given data
raw_data = [
    ['Beverages',85,90,80,85,90,95],
    ['Pastries',55,60,65,70,75,80],
    ['Dairy Products',70,75,80,85,90,95],
    ['Fruits & Vegetables',90,95,100,105,110,115],
    ['Meats',75,80,85,90,95,100]
]

data_labels = ['January','February','March','April','May','June']
line_labels = ['Beverages', 'Pastries', 'Dairy Products', 'Fruits & Vegetables', 'Meats']
data = [row[1:] for row in raw_data]  # exclude the first column, which is the line labels

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

fig = plt.figure(figsize=(10, 10))  # create figure
ax = fig.add_subplot(111, polar=True)  # add subplot
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)  # set the axis labels
ax.set_rlim(0,np.max(data))  # adjust the radial limits

for i, row in enumerate(data):
    data_line = np.append(row, row[0])  # join the first and last point
    ax.plot(angles, data_line, label = line_labels[i])  # plot data lines
    ax.fill(angles, data_line, alpha=0.25)  # fill the area under the lines with color

    gridline_radius = np.full_like(angles, (i+1) * np.max(data) / len(data))  # radius for gridlines
    ax.plot(angles, gridline_radius, color='gray', linestyle='dashed')  # draw gridlines

max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=-120)

# plot legend and title
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')
ax.set_title('Sales Analysis - Food and Beverage Industry', size=20, color='blue', y=1.1)

# Hide the circular gridlines and background.
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

plt.tight_layout()  # Automatically resize the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/103_2023122292141.png')  # save figure
plt.clf()  # Clear the current image state
