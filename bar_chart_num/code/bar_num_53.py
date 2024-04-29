
import matplotlib.pyplot as plt
import numpy as np

# Set the data
mode = ['Road','Rail','Air','Sea'] 
distance = [400, 450, 500, 550] 
cost = [50, 60, 90, 100] 

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
ax.bar(mode, distance, label='Distance(km)', color='#A9A9A9', width=0.35)
ax.bar(mode, cost, label='Cost(USD)', bottom=distance, color='#FFA500', width=0.35)

# Set the values on the chart
for i in range(len(mode)):
    plt.annotate(str(distance[i]), xy=(np.arange(len(mode))[i], distance[i]))
    plt.annotate(str(cost[i]), xy=(np.arange(len(mode))[i], cost[i]+distance[i]))

# Adjust the figure
plt.xticks(mode)
plt.title('Cost and distance of four transportation modes in 2021')
plt.legend(loc='upper left')
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/476.png')

# Clear the current image state
plt.clf()