
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Interest (%)', 'Equity (%)', 'Debt (%)', 'Tax (%)', 'Credit (%)']
data = np.array([[50, 55, 60, 65], [70, 75, 80, 85], [60, 65, 70, 75], [80, 85, 90, 95], [65, 70, 75, 80]])

# Append the first numerical element of each row to the end of the row for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Set the figure size
plt.figure(figsize=(10, 8))

# Plot the data
ax = plt.subplot(111, polar=True)

# Set the angles
angles = np.linspace(0, 2 * np.pi, len(data_labels)+1, endpoint=True)

# Set the axes range
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, 100)

# Draw the lines
for i in range(data.shape[0]):
    ax.plot(angles, data[i], label=line_labels[i], linewidth=2)

# Add the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.2, 1))

# Set the title
plt.title('Financial Evaluation - 2023')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/5_202312262300.png')

# Clear the current image state
plt.cla()