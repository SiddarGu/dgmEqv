
import matplotlib.pyplot as plt 
import numpy as np

# Set up the data
month = ["January", "February", "March", "April", "May"]
product_A = [200, 300, 400, 500, 400]
product_B = [400, 500, 500, 600, 500]
product_C = [600, 700, 800, 900, 700]
product_D = [800, 900, 1000, 1100, 1000]

# Set up figure
plt.figure(figsize=(10, 6))
ax = plt.subplot()

# Plot data
ax.plot(month, product_A, label="Product A")
ax.plot(month, product_B, label="Product B")
ax.plot(month, product_C, label="Product C")
ax.plot(month, product_D, label="Product D")

# Set up the grid
ax.grid(axis="y", color="lightgrey")

# Set up the x-axis ticks
plt.xticks(np.arange(5), month, rotation=45)

# Add legend
ax.legend(loc="upper right")

# Add title
ax.set_title("Production output of four products in 2020")

# Resize image
plt.tight_layout()

# Save image
plt.savefig("line chart/png/313.png")

# Clear current image
plt.clf()