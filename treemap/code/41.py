import matplotlib.pyplot as plt
import squarify

# Given data
data_str = """Social Media Platform,Active Users (%)
Facebook,30
YouTube,25
Instagram,20
Twitter,10
TikTok,7
LinkedIn,5
Pinterest,2
Snapchat,1"""

# Parsing the data into separate variables
lines = data_str.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Set the color palette, one different color for each segment
colors = plt.cm.Spectral([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8][:len(data)])

# Create a figure with larger figsize to prevent content from being squished
plt.figure(figsize=(12, 8))

# Creating the treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7, text_kwargs={'fontsize':12, 'wrap': True})

# Add the title of the figure
plt.title('Percentage of Active Users Across Major Social Media Platforms', fontsize=15)

# Remove the axes
plt.axis('off')

# Use tight_layout() to automatically adjust the subplot params for the image layout
plt.tight_layout()

# Save the figure using the absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/41.png'
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current image state
plt.clf()
plt.close()
