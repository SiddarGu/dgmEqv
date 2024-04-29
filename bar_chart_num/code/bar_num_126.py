
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[800000, 10000], [1000000, 20000], [1500000, 3000], [500000, 20000]])

# Create the figure
fig = plt.figure(figsize=(10,6))

# Plot the data
ax = fig.add_subplot()
ax.bar(['Olympics','World Cup','Super Bowl','Tour de France'], data[:,0], label='Attendees')
ax.bar(['Olympics','World Cup','Super Bowl','Tour de France'], data[:,1], bottom=data[:,0], label='Participants')

# Add labels to value of each data point
for i in range(4):
    ax.text(x=i-0.2, y=data[i,0]+data[i,1]/2, s=data[i,0]+data[i,1], color='black', fontsize=10)

# Add legend
ax.legend()

# Change the label of x axis
ax.set_xticklabels(['Olympics','World Cup','Super Bowl','Tour de France'], fontsize=10, rotation=45)

# Set the title
ax.set_title('Number of attendees and participants in major sports events in 2021')

# Resize the figure
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/272.png')

# Clear the current image state
plt.clf()