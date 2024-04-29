import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
data_labels = ['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Pinterest', 'Reddit']
line_labels = ['Active Users (Millions)', 'Average Time Spent (Minutes)', 'Ad Revenue (Billions)', 'Share of Voice (%)', 'Video Views Daily (Billions)']
data = np.array([[25, 10, 33, 31, 42, 43],
                 [20, 27, 10, 17, 14, 15],
                 [84.2, 20, 3.4, 2.58, 1, 0.12],
                 [40, 25, 15, 10, 5, 5],
                 [8, 3.5, 2, 1, 1.6, 1.9]])

# Plot the data with radar chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append the first numerical element of each row to the end for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot each data line with different colors
colors = ['b', 'g', 'r', 'c', 'm', 'y']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], 'o-', color=colors[i], label=line_labels[i])

# Plot axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits
ax.set_ylim(0, np.max(data) * 1.1)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Set title and adjust layout
plt.title('Social Media Usage and Monetization Analysis')
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/195_202312310100.png')

# Clear image state
plt.clf()
