
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
data_labels = ['Number of Users (Millions)', 'Revenue (Billions of Dollars)', 'Average Daily Use (Hours)']
line_labels = ['Social Media', 'Search Engines', 'News Sites', 'Video Sites', 'Blogs', 'Online Shopping', 'Streaming Services', 'Web Browsers', 'Forums', 'Online Gaming']
data = np.array([[950, 230, 3.5], [1300, 200, 2.5], [850, 100, 1.5], [550, 90, 2.0], [200, 12, 1.5], [700, 500, 1.0], [750, 150, 5.0], [1300, 20, 2.0], [300, 7, 0.5], [600, 70, 4.0]])

# Create figure
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# Plot the data
ax1.bar(line_labels, data[:, 0], width=0.3, color='#FF99FF', alpha=0.6, label=data_labels[0])
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], '-o', color='#99CCFF', alpha=0.8, label=data_labels[1])
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], '-*', color='#33CCCC', alpha=0.8, label=data_labels[2])

# Set y-axis positions
ax3.spines["right"].set_position(("axes", 1.2))

# Label all axes
ax1.set_ylabel('Number of Users (Millions)', color='#FF99FF')
ax2.set_ylabel('Revenue (Billions of Dollars)', color='#99CCFF')
ax3.set_ylabel('Average Daily Use (Hours)', color='#33CCCC')
ax1.set_xlabel('Category')

# Show the legends of all plots
ax1.legend(loc=(0.6, 0.8))
ax2.legend(loc=(0.6, 0.7))
ax3.legend(loc=(0.6, 0.9))

# Drawing techniques such as background grids
ax1.grid(linestyle='--')

# Use autolocator for all ax
ax1.xaxis.set_major_locator(plt.AutoLocator())
ax1.yaxis.set_major_locator(plt.AutoLocator())
ax2.yaxis.set_major_locator(plt.AutoLocator())
ax3.yaxis.set_major_locator(plt.AutoLocator())

# Set the title of the figure
ax1.set_title('Online Platforms Usage and Revenue Trends')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/2_2023122261325.png')

# Clear the current image state
plt.clf()