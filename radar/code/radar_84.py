import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
data_labels = np.array(["Gross Profit Margin (%)", "Operating Profit Margin (%)", "Net Profit Margin (%)", "Return on Assets (%)", "Return on Equity (%)"])
line_labels = np.array(["Small Business", "Franchise", "Online Store", "Corporation", "Startup"])
data = np.array([[22, 25, 23, 26, 28],
                [12, 16, 15, 18, 20],
                [8, 12, 11, 14, 16],
                [6, 8, 7, 9, 11],
                [10, 14, 12, 16, 18]])

# Create figure before plotting
figure = plt.figure()
ax = figure.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row in the data array
for i, row in enumerate(data):
    # Append the first numerical element of that row to the end of that row
    row = np.concatenate((row, row[:1]))
    # Plot the data lines with different colors
    ax.plot(angles, row, marker='o', label=line_labels[i])

# Plot the axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits to accommodate the maximum of data
ax.set_ylim([0, np.max(data) + 5])
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

# Set title
plt.title("Financial Performance Comparison across Business Types")

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/154_202312310100.png')

# Clear the current image state
plt.clf()