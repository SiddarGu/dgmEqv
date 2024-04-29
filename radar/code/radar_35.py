
import numpy as np
import matplotlib.pyplot as plt

# Data to be represented
data_labels = ['South Africa', 'Canada', 'Australia', 'Peru', 'Brazil', 'India', 'Mexico', 'Austria']
data = [[9.25, 6.72, 4.78, 7.56, 8.62],
        [9.45, 7.98, 6.17, 8.42, 7.50],
        [9.12, 8.23, 5.53, 9.02, 6.70],
        [9.01, 7.35, 4.98, 7.78, 7.60],
        [8.23, 7.12, 3.78, 7.86, 7.28],
        [8.20, 6.22, 3.35, 7.10, 7.87],
        [8.15, 5.18, 2.72, 6.85, 8.30],
        [4.32, 2.29, 1.75, 3.26, 4.95]]
line_labels = ['Iron Ore Quality','Ease of Mining','Mining Regulations','Environmental Protection','Economic Viability']

# Create figure before plotting
fig = plt.figure(figsize=(10, 8))

# Evenly space the axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row in the data array and append the first element of that row to its end
data = np.concatenate((data, [data[0]]))

# Plot the data
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, data, 'o-', linewidth=2, label=line_labels)
ax.fill(angles, data, alpha=0.25, c="black")

# Set angles
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)

# Adjust the radial limits
ax.set_ylim(0, 10)

# Draw background grids
ax.grid(True)

ax.set_title('Resources Evaluation and Economic Analysis by Country - 2021')
# Set legend
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/radar/png_val/radar_35.png')

# Clear the current image state
plt.cla()