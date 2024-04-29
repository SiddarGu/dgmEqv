

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Create figure before plotting
fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(1, 1)
ax = fig.add_subplot(gs[0, 0])

# Set chart data
labels = ['Facebook', 'YouTube', 'Instagram', 'Twitter', 'LinkedIn', 'Snapchat', 'TikTok'] # Labels
values = [35, 25, 20, 10, 5, 3, 2] # Percentage

# Set chart style
ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')

# Set chart legend
ax.legend(labels, loc='lower right')

# Set chart title
ax.set_title('Social Media Platform Popularity in the USA in 2023', fontsize=12, fontweight='bold')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/30.png')

# Clear current image state
plt.clf()