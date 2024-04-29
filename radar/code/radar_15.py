
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ["Location A","Location B","Location C","Location D"]
line_labels = ["Air Quality","Water Quality","Renewable Energy","Waste Management","Biodiversity"]
data = [[95,90,85,80],[90,85,80,75],[75,80,85,90],[85,90,95,100],[65,70,75,80]]

# Plot the data with the type of radar chart
angles = np.linspace(0, 2 * np.pi, len(data_labels)+1, endpoint=True)
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Iterate over each row in the data array 
for i in range(len(line_labels)):
    data_to_plot = np.append(data[i],data[i][0])
    ax.plot(angles, data_to_plot, linewidth=1, linestyle='solid', label=line_labels[i])
    ax.fill(angles, data_to_plot, alpha=0.1)

# Generate a angle-like radius vector with constant values
    angle_like_radius = np.full_like(angles, (i+1)*np.max(data)/len(data))
    ax.plot(angles, angle_like_radius, linewidth=1, linestyle='solid', label="", color='black', alpha=0.3)

# Plot the axis label
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=12, fontweight='normal', rotation=90, wrap=True)

# Adjust the radial limits to accommodate the maximum of data
ax.set_ylim(0, np.max(data))

# Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, -0.07), ncol=5, fontsize=12, frameon=False)

# Remove the circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Set the title of the figure
ax.set_title("Environmental Sustainability Compariso", fontsize=14, fontweight='normal')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/3.png')

# Clear the current image state
plt.clf()