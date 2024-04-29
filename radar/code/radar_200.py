import numpy as np
import matplotlib.pyplot as plt

# To transform data into variables
raw_data = ['Area,Year 1,Year 2,Year 3,Year 4', 'Criminal Cases,50,55,60,65', 
            'Civil Cases,65,70,75,80', 'Legal Services,80,85,90,95', 
            'Legislation,70,75,80,85', 'Court Efficiency,55,60,65,70']

data = []
line_labels = []
for line in raw_data[1:]:
    parts = line.split(',')
    line_labels.append(parts[0])
    data.append([float(x) for x in parts[1:]])

data = np.array(data)
data_labels = raw_data[0].split(',')[1:]

# Create the figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)
ax.set_title("Law and Legal Affairs Metrics Analysis", size=20, color='black', y=1.1)

# Evenly space the axes for the number of data points, and adjust the angles for radar chart
angles = np.linspace(0, 2*np.pi, len(data_labels)+1, endpoint=True)

# Iterate over each row of the array (each line in radar chart)
for i, row in enumerate(data):
    row = np.concatenate((row, [row[0]]))  # Close the loop by appending the first element at the end
    ax.plot(angles, row, label=line_labels[i])
    radii = np.full_like(angles, (i+1)*data.max() / (len(raw_data) - 1), dtype=float)
    ax.plot(angles, radii, color='gray', linestyle='dashed')

# Set the radial limits to accommodate the maximum of data
ax.set_rlim(0, np.ceil(data.max()))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Plot the axis label, removing labels at cardinal directions
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Remove the circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)


# Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", bbox_to_anchor=(1.1,1.1))

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/125_2023122292141.png")

# Clear the current image state
plt.clf()
