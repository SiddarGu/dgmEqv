
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Employee Retention (%)', 'Employee Satisfaction (Score)',
               'Training Effectiveness (Score)', 'Recruiting Efficiency (Score)', 'Performance Evaluation (Score)']
data = [[70, 75, 80, 85], [50, 55, 60, 65], [60, 65, 70, 75],
        [80, 85, 90, 95], [65, 70, 75, 80]]

# Plot the data with the type of radar chart
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i in range(len(line_labels)):
    # Append the first numerical element of that row to its end for close-loop plotting of data lines
    values = np.concatenate((data[i], [data[i][0]]))
    ax.plot(angles, values, linewidth=1, label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust the radial limits to accommodate the maximum of data
ax.set_rlim(0, 100)

# Plot the legend of data lines
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.25, 1.03))

# Drawing techniques such as background grids can be used
ax.grid(True)

# Set the title of the figure
plt.title('Human Resources Performance Evaluation')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the image as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/5_202312262150.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/5_202312262150.png')

# Clear the current image state at the end of the code
plt.clf()