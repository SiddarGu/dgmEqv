
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111)

# Data
x=np.arange(2020, 2025)
y1=np.array([2.0, 2.2, 2.4, 2.8, 3.2])
y2=np.array([200, 210, 220, 240, 260])
y3=np.array([2.5, 2.9, 3.3, 3.7, 4.1])

# Plot
ax.plot(x, y1, color='blue', marker='o',label='Median Home Prices(million dollars)')
ax.plot(x, y2, color='red', marker='o',label='Average Price per Square Foot(dollars)')
ax.plot(x, y3, color='green', marker='o',label='Projected Home Prices(million dollars)')

# Add x,y label
ax.set_xlabel('Year')
ax.set_ylabel('Price(million dollars)')

# Add title
ax.set_title('Real Estate Market Analysis in the US from 2020-2024')

# Add grid
ax.grid(linestyle='-.', linewidth='0.5', color='green')

# Add legend
ax.legend(loc='best')

# Add annotations
for i,j in zip(x,y1):
    ax.annotate(str(round(j,1)),xy=(i,j))

for i,j in zip(x,y2):
    ax.annotate(str(j),xy=(i,j))

for i,j in zip(x,y3):
    ax.annotate(str(round(j,1)),xy=(i,j))

# Set x ticks
plt.xticks(x)

# Resize the figure
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/457.png')

# Clear the figure
plt.clf()