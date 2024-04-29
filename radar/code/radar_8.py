
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["East", "West", "North", "South"]
line_labels = ["Education Quality", "Public Safety", "Infrastructure", "Taxes", "Employment"]
data = [[75, 80, 85, 90],
        [70, 75, 80, 85],
        [85, 90, 95, 100],
        [60, 65, 70, 75],
        [80, 85, 90, 95]]

# Plot the data with the type of radar chart, i.e., set 'polar=True'. Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, polar=True)

# Evenly space the axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
max_value = max([max(d) for d in data])

# Iterate over each row in the data array, append the first numerical element of that row to its end for close-loop plotting of data lines
# The plottig of different data lines should use different colors
for i in range(len(data)):
    data[i].append(data[i][0])
    ax.plot(angles, data[i], color=plt.cm.Set1(i/len(data)), linewidth=2, label=line_labels[i])

# Generate a angle-like radius vector with constant values
    ax.plot(angles, np.full_like(angles, (i+1) * (max_value/len(data))), color='black', linestyle='dashed', linewidth=1)

# Plot the axis label
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)

# Adjust the radial limits to accommodate the maximum of data
ax.set_ylim(0, max(data[i]) + 5)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# For the plot of legend
leg = ax.legend(loc='lower center', ncol=5)

# Drawing techniques such as background grids can be used
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# The title of the figure
plt.title('Government and Public Policy Performance Report', fontsize=16)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/radar/png_val/radar_8.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/radar/png_val/radar_8.png')

# Clear the current image state at the end of the code
plt.clf()