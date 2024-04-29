

import matplotlib.pyplot as plt

# Create a figure and add a subplot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)

# Create Pie Chart
labels = ['Adventure Tourism', 'Culinary Tourism', 'Cultural Tourism', 'Medical Tourism', 'Eco-Tourism']
sizes = [25, 20, 30, 15, 10]
explode = (0.1, 0, 0, 0, 0)

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=45)
ax.axis('equal')

# Set figure title
ax.set_title("Types of Tourism Popularity in 2023", fontsize=16, fontweight='bold')

# Set the font of the figure
ax.set_xlabel('')
ax.set_ylabel('')
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontname('Arial')
    label.set_fontsize(13)

# Make sure the figure is not clipped
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/120.png', dpi=120)

# Clear the current image state
plt.cla()