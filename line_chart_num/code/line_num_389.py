
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,6))

# Set up axis
ax = fig.add_subplot(1,1,1)

# Plot data
x = np.arange(2001,2006)
ax.plot(x, [3000,3200,3500,4000,4300], label='Soccer Players')
ax.plot(x, [2500,2700,3000,3300,3600], label='Basketball Players')
ax.plot(x, [1500,1800,2000,2200,2500], label='Football Players')

# Set title and label
ax.set_title('Global Sports Players Trend from 2001 to 2005')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Players')

# Set major ticks
ax.set_xticks(x)

# Add legend 
ax.legend(loc='upper left')

# Annotate each point
for x, y1, y2, y3 in zip(x, [3000,3200,3500,4000,4300], [2500,2700,3000,3300,3600], [1500,1800,2000,2200,2500]):
    ax.annotate(str(y1), xy=(x, y1), xytext=(-15, 10), textcoords='offset points')
    ax.annotate(str(y2), xy=(x, y2), xytext=(-15, 10), textcoords='offset points')
    ax.annotate(str(y3), xy=(x, y3), xytext=(-15, 10), textcoords='offset points')

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('line chart/png/190.png')

# Clear the image state
plt.clf()