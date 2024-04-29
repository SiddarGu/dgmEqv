import matplotlib.pyplot as plt
import numpy as np

# Data for the radar chart
data_labels = ['Customer Satisfaction', 'Delivery Time', 'Product Quality', 'Online Experience', 'Return Rate']
line_labels = ['Q1', 'Q2', 'Q3', 'Q4']
data = np.array([[90, 85, 80, 75], [75, 80, 85, 90], [85, 90, 95, 100], [80, 85, 90, 95], [65, 70, 75, 80]])
# Repeat the first column to close the circle
data = np.concatenate((data, data[0:1, :]), axis=0).T
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
max_val = np.max(data)

# Create a radar chart
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, polar=True)

# Plot each data series
for row in range(len(data)):
    line_color = np.random.choice(range(256), size=3)/255  # Generating random colors
    ax.plot(angles, data[row], color=line_color, linewidth=2, label=line_labels[row])
    ax.fill(angles, data[row], color=line_color, alpha=0.25)

# Set the labels for each angle
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=12)

# Set the range for the radial axis
ax.set_rlim(0, max_val + 5)

# Improve layout
ax.grid(False)
ax.spines['polar'].set_visible(False)

# Add a legend
legend = ax.legend(loc='upper right', bbox_to_anchor=(1.25, 0.5))

# Add a title
plt.title('Retail and E-commerce Performance Evaluation', fontsize=18)

# Adjust layout
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/4.png', bbox_inches='tight')
plt.clf()