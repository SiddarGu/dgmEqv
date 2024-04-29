
import matplotlib.pyplot as plt
import numpy as np

data = [[2001, 1, 2, 3, 4], 
        [2002, 4, 2, 1, 3],
        [2003, 3, 4, 1, 2], 
        [2004, 2, 1, 4, 3]] 

# Create Figure
fig, ax = plt.subplots(figsize=(10, 5))

# Get x-axis data
x = [x[0] for x in data]

# Get the y-axis data 
y1 = [x[1] for x in data]
y2 = [x[2] for x in data]
y3 = [x[3] for x in data]
y4 = [x[4] for x in data]

# Plot all lines 
ax.plot(x, y1, color='#0066CC', label='Ranking A')
ax.plot(x, y2, color='#FF9933', label='Ranking B')
ax.plot(x, y3, color='#3399FF', label='Ranking C')
ax.plot(x, y4, color='#FF3300', label='Ranking D')

# Add title
ax.set_title('Changes in rankings of four football teams from 2001 to 2004')

# Add legend and set position
ax.legend(loc='upper left')

# Set x-axis label 
ax.set_xlabel('Year')

# Set y-axis label 
ax.set_ylabel('Ranking')

# Set x-axis ticks
ax.set_xticks(x)

# Add grid
ax.grid(linestyle='--', linewidth=0.5, alpha=0.5)

# Annotate each point
for x, y1, y2, y3, y4 in zip(x, y1, y2, y3, y4):
    ax.annotate('A:'+str(y1), xy=(x, y1))
    ax.annotate('B:'+str(y2), xy=(x, y2))
    ax.annotate('C:'+str(y3), xy=(x, y3))
    ax.annotate('D:'+str(y4), xy=(x, y4))

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/347.png')

# Clear the current image state
plt.clf()