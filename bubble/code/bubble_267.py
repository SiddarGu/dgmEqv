
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

# Transform the given data into three variables:
data_labels = ['Revenue (Billion $)', 'Tourists (Millions)', 'Employment (Millions)', 'Satisfaction (Score)']

data = [[1300, 60, 8, 9], [1000, 50, 6, 7], [750, 40, 4, 6], [650, 35, 3, 8], [400, 30, 2, 7], [250, 25, 1, 9]]

line_labels = ['USA', 'UK', 'France', 'Spain', 'India', 'Japan']

# Plot the data with the type of bubble chart
fig = plt.figure()
ax = fig.add_subplot()

# Set parameters to accurately reflect the differences in data values
norm = colors.Normalize(vmin=min([x[3] for x in data]), vmax=max([x[3] for x in data]))
cmap = cm.get_cmap('coolwarm')

# Iterate through each row of data
for i in range(len(data)):
    ax.scatter(data[i][0], data[i][1], label=None, s= 60 + 500 * (data[i][2] - min([x[2] for x in data])) / (max([x[2] for x in data]) - min([x[2] for x in data])), c=cmap(norm(data[i][3])))
    ax.scatter([], [], label=line_labels[i] + ' ' + str(data[i][2]), s=20, c=cmap(norm(data[i][3])))

# Plot the legend with the title
ax.legend(title=data_labels[2])

# Add a color bar for the bubble colors
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, ax=ax, label=data_labels[3])

# Adjust other parameters
ax.grid(linestyle='-.')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Tourism and Hospitality Performance of Popular Destinations')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/33_2023122270050.png')
plt.clf()