
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(12,4))
ax = fig.add_subplot(111)

# Set x-axis
x_axis = np.arange(len(['Road','Rail','Air','Sea']))

# Set Data
speed = [120,90,900,40]
cost = [100,200,400,150]

# Set Bar Chart
ax.bar(x_axis, speed, width=0.2, label='Speed', bottom=0, align='center')
ax.bar(x_axis, cost, width=0.2, label='Cost', bottom=speed, align='center')

# Set title and xticks
plt.title("Speed and Cost of Different Transportation Modes in 2021")
plt.xticks(x_axis, ['Road','Rail','Air','Sea'])

# Set Labels
for i in range(len(x_axis)):
    plt.annotate(str(speed[i]), xy=(i-0.1, speed[i]+5), fontsize=10)
    plt.annotate(str(cost[i]), xy=(i+0.1, cost[i]+5), fontsize=10)

# Set legend
ax.legend(bbox_to_anchor=(1, 1), loc=2)

# Adjust the image
plt.tight_layout()

# Save the image
plt.savefig('Bar Chart/png/100.png')

# Clear the current image state
plt.clf()