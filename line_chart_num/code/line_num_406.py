
import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(12, 8))

# Set Subplot
ax = plt.subplot()

# Set x and y axis
x_axis = np.array([2000, 2001, 2002, 2003, 2004])
y_axis_1 = np.array([600, 800, 1000, 1200, 1400])
y_axis_2 = np.array([1000, 1200, 1500, 1800, 2000])
y_axis_3 = np.array([2000, 3000, 4000, 3000, 2000])

# Plot three lines
ax.plot(x_axis, y_axis_1, label="Local Tax Revenue(million dollars)")
ax.plot(x_axis, y_axis_2, label="State Tax Revenue(million dollars)")
ax.plot(x_axis, y_axis_3, label="Federal Tax Revenue(million dollars)")

# Set x and y ticks
plt.xticks(x_axis)
plt.yticks(np.arange(0, 5000, 1000))

# Set title and legend
ax.set_title("Tax Revenues in the USA from 2000 to 2004")
ax.legend(loc="best")

# Set grid
ax.grid()

# Set annotation
for x, y_1, y_2, y_3 in zip(x_axis, y_axis_1, y_axis_2, y_axis_3):
    ax.annotate('{},{},{}'.format(y_1, y_2, y_3), (x, y_1), 
                xytext=(-20, 10), textcoords='offset points', 
                rotation=45, wrap=True)

# Adjust figure
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/286.png')

# Clean figure
plt.cla()