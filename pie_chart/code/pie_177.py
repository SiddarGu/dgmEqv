
import matplotlib.pyplot as plt

# Set figure
plt.figure(figsize=(12, 8))

# Pie chart
labels = ['Social Media', 'Search Engines', 'E-Commerce', 'Video Platforms', 'Streaming Services', 'News Platforms']
sizes = [30, 24, 20, 14, 8, 4]
explode = (0.1, 0, 0, 0, 0, 0) 

ax = plt.subplot()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
ax.axis('equal')

# Figure title
ax.set_title('Usage Distribution of the Internet Platforms in the USA, 2023', fontsize=20)

# Remove x, y ticks
ax.set_xticks([])
ax.set_yticks([])

# Save figure
plt.tight_layout()
plt.savefig('pie chart/png/127.png')

# Clear current image state
plt.clf()