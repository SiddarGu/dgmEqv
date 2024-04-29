
import matplotlib.pyplot as plt
import numpy as np

# transform data into three variables
y_values = ['GDP ($ Billion)', 'Unemployment Rate (%)', 'Life Expectancy (Years)']
x_values = ['USA', 'UK', 'Germany', 'Japan', 'China']
data = np.array([[20, 47, 78.9], [29, 39, 81.3], [37, 51, 81.2], [50, 24, 84.2], [13.6, 52, 76.5]])

# create figure
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111, projection='3d')

# plot data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.2, 0.2, data[:, i], shade=True, color='lightblue', alpha=0.8)

# set the dimensions of the bars
ax.set_xlabel('Country')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)

# add title
ax.set_title('Global Economic and Health Trends in Social Sciences and Humanities')

# draw background grids
ax.grid()

# resize the image
plt.tight_layout()

# save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/12_202312251036.png')

# clear the current image state
plt.clf()