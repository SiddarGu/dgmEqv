import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Given data
csv = '''Social Media Platform, Daily Active Users (Millions), Revenue (Millions USD), Average Time Spent (Minutes)
Facebook,1900,70420,39
Instagram,600,20240,29
Pinterest,459,1660,15
Snapchat,280,2390,26
YouTube,2000,15840,40
Twitter,330,3900,31
Linkedin,310,7760,17
Reddit,430,100,11
TikTok,680,6920,52
WhatsApp,2000,5080,30'''

# Transform data into list and array
lines = csv.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = np.array([[float(value) for value in line.split(',')[1:]] for line in lines[1:]])

# Create new figure and subplots
fig = plt.figure(figsize=(24, 10))
ax1 = fig.add_subplot(111)

# Plot data (plot types: bar chart,line chart,scatter chart,area chart)
ax1.bar(line_labels, data[:, 0], color='blue', alpha=0.6)
ax1.set_ylabel(data_labels[0], color='blue') 

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='orange')
ax2.set_ylabel(data_labels[1], color='orange')

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], color='green')
ax3.set_ylabel(data_labels[2], color='green')
ax3.spines['right'].set_position(('outward', 60))

plt.title("Social Media Platforms: User Engagement and Revenue")
# Draw legend, adjust chart layout, and set title
fig.legend(loc="upper left", labels=data_labels, bbox_to_anchor=(0.1, 0.95)) 
fig.tight_layout()

# Save figure and clear plot
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/176_202312310108.png")
plt.clf()
