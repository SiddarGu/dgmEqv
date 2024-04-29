
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig=plt.figure(figsize=(14, 7))

# Plotting
ax=fig.add_subplot(111)

# Data
data=[[2001,2.5,3.2,4.2],
      [2002,3.4,4.0,4.5],
      [2003,2.7,3.4,4.8],
      [2004,3.2,2.9,4.3],
      [2005,2.6,3.7,4.0]]
x=np.array([row[0] for row in data])
y1=np.array([row[1] for row in data])
y2=np.array([row[2] for row in data])
y3=np.array([row[3] for row in data])

# Plotting
ax.plot(x, y1, label='Inflation Rate(%)')
ax.plot(x, y2, label='Interest Rate(%)')
ax.plot(x, y3, label='Unemployment Rate(%)')

# Titles
plt.title('Economic Indicators in the US from 2001 to 2005', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Rate (%)')

# Legend
plt.legend(loc='lower right', fontsize=10, bbox_to_anchor=(1.0, 0.0))

# Ticks
plt.xticks(x, rotation=45, wrap=True)

# Automatically resize
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/423.png')

# Clear the current image state
plt.cla()