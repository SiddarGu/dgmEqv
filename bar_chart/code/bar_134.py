
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 6))
# Add subplot
ax = fig.add_subplot(111)

# Define data
Employee = ['John', 'Mary', 'Mark', 'Lisa']
Leave_Days = [14, 10, 12, 11]
Bonus = [800, 700, 500, 600]

# Create bar chart
ax.bar(Employee, Leave_Days, bottom=0, label='Leave Days')
ax.bar(Employee, Bonus, bottom=Leave_Days, label='Bonus')
ax.set_title('Employee leaves and bonuses in 2021')

# Set xticks, legend and add grids
ax.set_xticks(np.arange(len(Employee)))
ax.set_xticklabels(Employee, rotation=45, wrap=True)
ax.legend(loc='upper left')
ax.grid(axis='y', linestyle='--')

# Resize image
plt.tight_layout()

# Save image
plt.savefig("bar chart/png/160.png")

# Clear current image state
plt.clf()