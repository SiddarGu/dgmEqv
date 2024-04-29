

import matplotlib.pyplot as plt
import numpy as np

# Set the figure size
plt.figure(figsize=(8, 5))

# Set the x, y axis data
ageGroup = ["0-18", "19-35", "36-50", "50+"]
museums = [1000, 800, 500, 200]
galleries = [2000, 1800, 1400, 1000]
theaters = [500, 400, 300, 200]

# Set the bar width
barWidth = 0.2

# Set the position for each bar
r1 = np.arange(len(ageGroup))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Set the chart title
plt.title("Arts and culture visits by age group in 2021")

# Set the x-axis labels
plt.xticks(r1, ageGroup, rotation=45, wrap=True)

# Plot the bars
plt.bar(r1, museums, color='#fbe8c1', width=barWidth, label='Museums')
plt.bar(r2, galleries, color='#fcc2b4', width=barWidth, label='Galleries')
plt.bar(r3, theaters, color='#f9a8a1', width=barWidth, label='Theaters')

# Add a legend
plt.legend(bbox_to_anchor=(1.2, 1))

# Automatically adjust the subplot parameters to give specified padding
plt.tight_layout()

# Save the figure
plt.savefig('bar chart/png/150.png')

# Clear the current image state
plt.clf()