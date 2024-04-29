
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,6))

x = np.array([2010,2011,2012,2013,2014,2015,2016,2017])
y1 = np.array([45,50,58,55,48,51,57,54])
y2 = np.array([58,60,65,68,70,75,80,82])

# Plot 
plt.plot(x, y1, label = 'Attendance per match(in thousands)', marker='o')
plt.plot(x, y2, label = 'Average ticket price', marker='^')

# Label the value of each data point directly on the figure
for a,b in zip(x,y1):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a,b in zip(x,y2):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

# Set background grids
plt.grid(linestyle='--', linewidth=0.5)

# Set the title of the figure
plt.title('Average attendances and ticket prices for sports matches in the US from 2010 to 2017', fontsize=12)

# Set legend
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=2, fancybox=True, shadow=True)

# Set x ticks
plt.xticks(x)

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('line chart/png/51.png')

# Clear the current image state
plt.clf()