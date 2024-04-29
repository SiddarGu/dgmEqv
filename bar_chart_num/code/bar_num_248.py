
import matplotlib.pyplot as plt
import numpy as np

# Get data
country = ('USA', 'UK', 'Germany', 'France')
Courts = np.array([100, 80, 90, 70])
Prisoners = np.array([2000, 1700, 1500, 1900])

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Set legend
ax.set_title('Number of Courts and Prisoners in four countries in 2021', fontsize=16)
ax.set_xlabel('Country', fontsize=14)
ax.set_ylabel('Number', fontsize=14)

# Plot data
width = 0.3
ax.bar(np.arange(len(Courts))-width/2, Courts, width, color='#FFA07A', label='Courts')
ax.bar(np.arange(len(Prisoners))+width/2, Prisoners, width, color='#20B2AA', label='Prisoners')
ax.legend(loc='best')

# Set xticks
ax.set_xticks(np.arange(len(country)))
ax.set_xticklabels(country)

# Adjust figure
fig.tight_layout()

# Annotate
for x, y in zip(np.arange(len(Courts)), Courts):
    ax.text(x-width/2, y+50, '%.0f' % y, ha='center', va='bottom')

for x, y in zip(np.arange(len(Prisoners)), Prisoners):
    ax.text(x+width/2, y+50, '%.0f' % y, ha='center', va='bottom')

# Save figure
plt.savefig('Bar Chart/png/260.png')

# Clear current image state
plt.clf()