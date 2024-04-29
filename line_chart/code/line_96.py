
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# Get data
year = np.array([2001, 2002, 2003, 2004])
incomeA = np.array([10000, 12000, 8000, 15000])
incomeB = np.array([8000, 9000, 11000, 12000])
costA = np.array([7000, 8000, 9000, 10000])
costB = np.array([6000, 7000, 6000, 7000])

# Plot
ax.plot(year, incomeA, color='#33cccc', label='Income A')
ax.plot(year, incomeB, color='#ff9933', label='Income B')
ax.plot(year, costA, color='#339999', label='Cost A')
ax.plot(year, costB, color='#009933', label='Cost B')

# Set labels
ax.set_title('Financial Balance of Two Companies in 2001-2004', fontsize=14)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Balance', fontsize=12)

# Set ticks
ax.set_xticks(year)

# Set legend, grid, and save
ax.legend(loc='best', fontsize=12, ncol=4)
ax.grid()
fig.tight_layout()
fig.savefig('line chart/png/19.png', dpi=300)
plt.clf()