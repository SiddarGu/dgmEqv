
import matplotlib.pyplot as plt
import numpy as np

# Create figure and set size
fig = plt.figure(figsize=(13,8))
ax = fig.add_subplot(1,1,1)

# Set data
year = np.array([2001, 2002, 2003, 2004, 2005, 2006])
employees = np.array([50, 60, 70, 80, 90, 100])
absentees = np.array([2, 5, 7, 10, 12, 15])

# Plot line chart
ax.plot(year, employees, label="Employees")
ax.plot(year, absentees, label="Absentees")

# Set ticks
ax.set_xticks(year)

# Set legend
ax.legend(loc="upper left")

# Set title
ax.set_title("Absenteeism rate of employees over five years")

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig("line chart/png/10.png")

# Clear current image state
plt.clf()