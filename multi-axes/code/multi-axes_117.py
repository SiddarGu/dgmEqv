import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Data
line_labels = ["Social Networking Sites", "Video Sharing Sites", "Messaging Apps", "Online Forums", 
               "Blogging Platforms", "News Aggregation Websites", "E-commerce Platforms",
               "Online Gaming Platforms", "Search Engines", "Content Sharing Platforms"]

data_labels = ["Number of Users (Millions)", "Engagement Rate (%)", "Average Time Spent (Hours)"]

data = np.array([[250,60,3],
                [180,40,2],
                [280,80,2.5],
                [70,30,1],
                [100,50,1.5],
                [150,70,2.5],
                [200,60,2.5],
                [120,40,2],
                [300,40,3.5],
                [220,70,2]])

# Create figure and subplot
fig, ax1 = plt.subplots(figsize=(15,10))

# Plot 1st set of data as bar 
ax1.bar(list(range(len(line_labels))), data[:,0], color='b', alpha=0.6, label='Number of Users (Millions)')
ax1.set_ylabel('Number of Users (Millions)', color='b')
ax1.set_xlabel('Platforms')
ax1.set_xticks(list(range(len(line_labels))))
ax1.set_xticklabels(line_labels, rotation=45)
ax1.xaxis.grid(True)

# Plot 2nd set of data as line chart, shared x-axis
ax2 = ax1.twinx()
ax2.plot(list(range(len(line_labels))), data[:,1], color='r', label='Engagement Rate (%)')
ax2.set_ylabel('Engagement Rate (%)', color='r')

# Plot 3rd set of data as scatter chart, shared x-axis
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.scatter(list(range(len(line_labels))), data[:,2], color='g', label='Average Time Spent (Hours)')
ax3.set_ylabel('Average Time Spent (Hours)', color='g')

ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())

fig.suptitle('Social Media and Web Usage: Users, Engagement, and Time Spent')

# Save the image
plt.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/286_202312311430.png')
plt.clf()
