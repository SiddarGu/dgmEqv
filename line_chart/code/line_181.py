

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# Create figure
plt.figure(figsize=(15, 8))

# Define data
data = [[2001, 100, 80, 120, 150], [2002, 150, 90, 110, 160], [2003, 80, 110, 130, 120], [2004, 150, 120, 140, 80]]

# Get x-axis values
x_axis = [x[0] for x in data]

# Get y-axis values
y_axis_a = [x[1] for x in data]
y_axis_b = [x[2] for x in data]
y_axis_c = [x[3] for x in data]
y_axis_d = [x[4] for x in data]

# Plotting
ax = plt.subplot()
ax.plot(x_axis, y_axis_a, color="red", label="Production A")
ax.plot(x_axis, y_axis_b, color="green", label="Production B")
ax.plot(x_axis, y_axis_c, color="blue", label="Production C")
ax.plot(x_axis, y_axis_d, color="orange", label="Production D")

# Set title
plt.title('Production of four products in a single factory in the last decade')

# Set x label
plt.xlabel("Year")

# Set y label
plt.ylabel("Units/day")

# Set xticks
plt.xticks(x_axis)

# Set legend
plt.legend(loc="lower right")

# Set Grid
plt.grid(linestyle='-.')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/127.png')

# Clear current image
plt.clf()