import matplotlib.pyplot as plt
import squarify

# Parsing given data
data_labels = ['User Engagement (%)']
line_labels = ['Social Networking', 'Search Engines', 'Online Shopping', 'Video Streaming', 'Blogging Platforms', 'Email Services', 'Online Gaming', 'News Websites']
data = [35, 25, 15, 10, 5, 5, 3, 2]

# Setting the figure size
plt.figure(figsize=(12, 8))

# Colors for each segment
colors = plt.cm.tab20.colors

# Creating the treemap
squarify.plot(sizes=data, label=line_labels, color=colors[:len(data)],
              bar_kwargs={'linewidth':1, 'edgecolor':'white'}, text_kwargs={'wrap':True})

# Setting the title of the treemap
plt.title('User Engagement Across Web Platforms in Social Media Era')

# Removing the axes frames
plt.axis('off')

# Adjust the layout of the plot
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1120.png', format='png')

# Clear the current figure's state to prepare for the next plot if necessary
plt.clf()
