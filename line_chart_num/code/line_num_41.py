

import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 6))

# Plot
ax = fig.add_subplot(1,1,1)
# Set x-axis values
x = np.array([2011,2012,2013,2014,2015,2016])
# Set y-axis values
y1 = [400,800,1200,1800,2500,3500]
y2 = [10,50,100,200,400,600]
y3 = [1,5,10,20,50,100]
# Draw lines
ax.plot(x, y1, color='red', marker='o', linestyle='--', label='Facebook Users (millions)')
ax.plot(x, y2, color='green', marker='o', linestyle='--', label='Twitter Users (millions)')
ax.plot(x, y3, color='blue', marker='o', linestyle='--', label='Instagram Users (millions)')
# Set xticks
ax.set_xticks(x)
# Set Title
ax.set_title('Social Media User Growth from 2011 to 2016')
# Display legend
ax.legend(loc='upper left')
# Annotate
for a,b,c in zip(x,y1,y1): 
    plt.text(a, b, str(c), fontsize=12)
for a,b,c in zip(x,y2,y2): 
    plt.text(a, b, str(c), fontsize=12)
for a,b,c in zip(x,y3,y3): 
    plt.text(a, b, str(c), fontsize=12)
# Adjust figure
fig.tight_layout()
# Save figure
plt.savefig('line chart/png/156.png')
# Clear current figure
plt.clf()