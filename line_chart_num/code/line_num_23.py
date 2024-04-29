
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(20, 10))

# Set the data
x = [2016, 2017, 2018, 2019]
y1 = [20, 25, 17, 30]
y2 = [10, 12, 14, 15]
y3 = [15, 20, 18, 25]

# Plot the data
plt.plot(x, y1, marker='o', linestyle='-', color='r', label='Number of Art Exhibitions')
plt.plot(x, y2, marker='o', linestyle='-', color='b', label='Number of Music Festivals')
plt.plot(x, y3, marker='o', linestyle='-', color='g', label='Number of Theater Plays')

# Label the data points
for i, j in zip(x, y1):
    plt.annotate(str(j), xy=(i, j+0.5))
for i, j in zip(x, y2):
    plt.annotate(str(j), xy=(i, j+0.5))
for i, j in zip(x, y3):
    plt.annotate(str(j), xy=(i, j+0.5))

# Set the title
plt.title('Cultural Events Trend in the Last Four Years')

# Set the legend
plt.legend(loc='best')

# Set the x-ticks
plt.xticks(x)

# Set the background grid
plt.grid()

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/164.png')

# Clear the current image state
plt.clf()