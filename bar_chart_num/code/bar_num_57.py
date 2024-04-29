
import matplotlib.pyplot as plt
import numpy as np

# Data to plot
Country = ['USA', 'UK', 'India', 'China']
Internet_Users = [350, 100, 900, 1000]
Smartphone_Users = [400, 150, 1000, 1200]

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot bar chart
ax.bar(Country, Internet_Users, label = 'Internet Users', bottom = Smartphone_Users, width = 0.5, color = 'b')
ax.bar(Country, Smartphone_Users, label = 'Smartphone Users', color = 'r')

# Set title
plt.title('Number of Internet and Smartphone Users in four countries in 2021')

# Set legend
plt.legend(loc='upper left')

# Set x, y-axis labels
ax.set_xlabel('Country')
ax.set_ylabel('Number of Users (million)')

# Add grid
ax.grid(axis='y')

# Add labels on each bar
for i, v in enumerate(Internet_Users):
    ax.text(i-0.25, v+50, str(v), color='b', fontweight='bold')
for i, v in enumerate(Smartphone_Users):
    ax.text(i-0.25, v+50, str(v), color='r', fontweight='bold')

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Set x, y-axis ticks
plt.xticks(np.arange(len(Country)), Country)
plt.yticks(np.arange(0, 1300, step=100))

# Save figure
plt.savefig('Bar Chart/png/41.png')

# Clear current image
plt.clf()