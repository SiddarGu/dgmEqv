
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,6))

# Create data
Region = ['Asia', 'Europe', 'North America', 'South America']
Research_Projects = [200, 250, 220, 180]
Experiments = [400, 450, 500, 400]
Inventions = [50, 70, 60, 80]

# Create bar chart
x = np.arange(len(Region))
width = 0.2
ax = fig.add_subplot(111)
ax.bar(x, Research_Projects, width, label='Research Projects', color='#F7B829')
ax.bar(x + width, Experiments, width, label='Experiments', color='#B2DFDB')
ax.bar(x + width * 2, Inventions, width, label='Inventions', color='#FC4F30')

# Set figure parameters
ax.set_title('Science and Engineering activities in four regions in 2021')
ax.set_xticks(x + width * 1.5)
ax.set_xticklabels(Region)
ax.set_ylabel('Amout')
ax.legend()

# Label the value of each data point for every variables directly on the figure
for a,b in zip(x, Research_Projects):
    ax.annotate(str(b), xy=(a, b + 4), rotation=90, va='bottom', ha='center')
for a,b in zip(x, Experiments):
    ax.annotate(str(b), xy=(a + width, b + 4), rotation=90, va='bottom', ha='center')
for a,b in zip(x, Inventions):
    ax.annotate(str(b), xy=(a + width * 2, b + 4), rotation=90, va='bottom', ha='center')

# Automatically resize the image by tight_layout
fig.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/131.png')

# Clear current image state
plt.clf()