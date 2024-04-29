
import matplotlib.pyplot as plt 
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

# Plot data
x = np.array([2001, 2002, 2003, 2004, 2005])
gdp = np.array([1.2, 1.3, 1.4, 1.5, 1.6])
inflation = np.array([2.5, 2.7, 2.6, 2.8, 2.7])
unemployment = np.array([4.5, 4.6, 4.4, 4.2, 4.1])

ax.plot(x, gdp, label='GDP', color='red')
ax.plot(x, inflation, label='Inflation Rate', color='blue')
ax.plot(x, unemployment, label='Unemployment Rate', color='green')

# Set title
plt.title('Economic indicators of the US from 2001 to 2005')

# Set labels
plt.xlabel('Year')
plt.ylabel('Value')

# Set legend
ax.legend(loc='best')

# Set x ticks
plt.xticks(x)

# Save figure
plt.savefig('line chart/png/477.png')

# Clear the current image state
plt.clf()