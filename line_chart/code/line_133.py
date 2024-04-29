
import matplotlib.pyplot as plt
import numpy as np

# data
year = np.array([2001, 2002, 2003, 2004])
total_tax_rev = np.array([3000, 3200, 3500, 3700])
state_tax_rev = np.array([1500, 1600, 1700, 1800])
fed_tax_rev = np.array([1500, 1600, 1800, 1900])

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# Plot data
ax.plot(year, total_tax_rev, color='b', label='Total')
ax.plot(year, state_tax_rev, color='r', label='State')
ax.plot(year, fed_tax_rev, color='g', label='Federal')

# Set ticks
ax.set_xticks(year)

# Label axis
ax.set_xlabel('Year')
ax.set_ylabel('Tax Revenue (billion dollars)')

# Set legend
ax.legend(loc='upper left')

# Set title
ax.set_title('Total and State/Federal Tax Revenue in the US from 2001 to 2004')

# Tight layout
plt.tight_layout()

# Save image
plt.savefig('line chart/png/382.png')

# Clear figure
plt.clf()