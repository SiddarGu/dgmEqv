import numpy as np
import matplotlib.pyplot as plt

data = np.array([[45, 30, 35, 28, 40],
                 [40, 35, 30, 32, 43],
                 [50, 38, 45, 30, 50],
                 [38, 45, 50, 25, 43],
                 [48, 42, 36, 33, 46]])

data_labels = ['Trucks', 'Delivery Vans', 'Trailers', 'Navigational Equipment', 'Staff']
line_labels = ['XYZ Transport', 'ABC Freight', 'PQR Logistics', 'KLM Movers', 'RST Couriers']

# Extend the data array to include the first element for closed-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Set up the figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Set evenly spaced angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot each row of data as a line on the radar chart
colors = ['red', 'blue', 'green', 'orange', 'purple']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], label=line_labels[i])

# Set the axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits to accommodate maximum value
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Add a legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Set the title
plt.title('Transportation and Logistics Resources Comparison')

# Add a grid
ax.grid(True)

# Automatically resize the image to fit the content
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/206_202312310100.png')

# Clear the current image state
plt.clf()