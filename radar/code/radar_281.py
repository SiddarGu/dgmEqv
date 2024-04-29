import matplotlib.pyplot as plt
import numpy as np

# Transforming the given data into variables as requested
data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
data = [[80,85,90,95],
        [70,75,80,85],
        [75,80,85,90],
        [60,55,50,45],
        [85,90,95,100]]
line_labels = ['Sales', 'Customer Retention', 'Online Traffic', 'Product Returns', 'Market Expansion']

# Create figure before plotting
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

# Evenly space the axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plotting the data and creating gridlines
for i, row in enumerate(data):
    row.append(row[0])
    ax.plot(angles, row, label=line_labels[i])
    ax.fill(angles, row, alpha=0.25)
    gridline_values = np.full_like(angles, (i+1)*max([item for sublist in data for item in sublist])/len(data))
    ax.plot(angles, gridline_values, color='black', linestyle=':')

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Plotting the axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjusting the radial limits
ax.set_rlim(0,100)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", bbox_to_anchor=(1.1,1.1))

# Set the title
plt.title('Retail and E-commerce Business Quarterly Report')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/43_2023122292141.png')

# Clear the current image state
plt.clf()
