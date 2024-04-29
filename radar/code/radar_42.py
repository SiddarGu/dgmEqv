
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Crop Yield (Ton)', 'Pesticide Use (kg)', 'Water Usage (KL)', 'Fertilizer Use (kg)', 'Soil Quality (Score)']
data = np.array([[300,320,340,360], [150,200,250,300], [200,210,220,230], [500,600,700,800], [80,85,90,95]])

# Add the first column to the end of the data for plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Set up the figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)

# Set angles and labels
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)

# Plot the data
ax.plot(angles, data.T, linewidth=2, label=line_labels)
ax.fill(angles, data.T, alpha=0.25)

# Set the radial limits
ax.set_ylim(0, np.max(data))

# Add a title
ax.set_title('Agriculture and Food Production Report - 2023', fontsize=18)

# Get legend handles and labels
handles, labels = ax.get_legend_handles_labels()

# Place the legend in the corner
ax.legend(handles, line_labels, loc=(0.9, 0.9), fontsize=14)

# Add gridlines
ax.grid(True)

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/36_202312262320.png')

# Clear the current figure
plt.clf()