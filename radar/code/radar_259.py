import matplotlib.pyplot as plt
import numpy as np

# Parsing the data from string to respective data structures
data_rows = 'Sector,Q1,Q2,Q3,Q4/n Technology (Billion $),65,70,75,80/n Healthcare (Billion $),55,60,65,70/n Retail (Billion $),50,55,60,65/n Real Estate (Billion $),60,65,70,75/n Energy (Billion $),50,55,60,65'.split('/n')

line_labels = []
data = []
for row in data_rows[1:]:
    parsed_row = row.split(',')
    line_labels.append(parsed_row[0])
    data.append([int(i) for i in parsed_row[1:]])
data_labels = data_rows[0].split(',')[1:]

# Creating the figure and axes
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

# Evenly spaced angles for the data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterating over the rows in the data array
max_val = max([max(row) for row in data])
for i, row in enumerate(data):
    row.append(row[0])   
    
    # Plot data lines
    ax.plot(angles, row, label=line_labels[i])
    # Plot gridlines with a single color
    ax.plot(angles, np.full_like(angles, (i+1) * max_val / len(data)), color='lightgrey')

# Plotting the axis label
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)

# Adjusting the radial limits
ax.set_rlim(0, max_val)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Legend positioning
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Further adjustments and visual presentation
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

plt.title("Market Sector Performance - 2023", y=1.1)

plt.tight_layout()
# Saving the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/189_2023122292141.png')

# Clear the current image state
plt.clf()
