
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Q1", "Q2", "Q3", "Q4"]
line_labels = ["Education (%)", "Art (%)", "Diversity (%)", "Health (%)", 
               "Social Media (%)"]
data = np.array([[80, 85, 90, 95], 
                 [70, 75, 80, 85], 
                 [60, 65, 70, 75],
                 [50, 55, 60, 65],
                 [70, 75, 80, 85]])
# append the first numerical element of that row to the end of that row  for close-loop plotting of data lines
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Create figure and set the figsize
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, polar=True)

# Set angles 
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row in the data array
for i in range(len(data)):
    # Set color for each line
    ax.plot(angles, data[i], 
            linewidth=2, label=line_labels[i])
    # Set the first element of the row to the last element, 
    # make the chart closed
    ax.fill(angles, data[i], alpha=0.25)

# Set radial limits
ax.set_rlim(0, 100)

# Set the axis label
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)

# Get handles and labels
handles, labels = ax.get_legend_handles_labels()

# Add legend
ax.legend(handles, labels, fontsize=14)

# Draw background grids
ax.grid(True)

# Setting the title
ax.set_title("Social Sciences and Humanities Performance - 2023")

# Automatically resize the image
plt.tight_layout()

# Save image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/radar/png_val/radar_45.png")

# Clear the current image state
plt.clf()