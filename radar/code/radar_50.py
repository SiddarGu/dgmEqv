
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
data_labels = ["Q1", "Q2", "Q3", "Q4"]
line_labels = ["Education (%)", "Empathy (Score)", "Creativity (Score)", "Communication (Score)", "Leadership (Score)"]
data = [[80,85,90,95], [80,85,90,95], [60,65,70,75], [70,75,80,85], [75,80,85,90]]

# Plot the data with the type of radar chart
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)

# Evenly space the axes for the number of data points
angles=np.linspace(0, 2*np.pi, len(data_labels)+1, endpoint=True)

# Iterate over each row in the data array
for i, line in enumerate(data):
    line.append(line[0])
    ax.plot(angles, line, 'o-', linewidth=2, label=line_labels[i])
    ax.fill(angles, line, alpha=0.25)

# Plot the axis label
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust the radial limits to accommodate the maximum of data
ax.set_rlim(0, 100)

# Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=(0.9, .95), labelspacing=0.1, fontsize=10)

# Drawing techniques such as background grids can be used
ax.grid(True)

# Set the title of the figure
plt.title("Social and Human Development - 2023", fontsize=12)

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout() 

# The image must be saved as
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/15_202312262150.png")

# Clear the current image state
plt.clf()