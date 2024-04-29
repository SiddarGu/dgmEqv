
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

# Set data
year = [2001, 2002, 2003, 2004]
fruits = [200, 250, 300, 400]
vegetables = [300, 450, 400, 500]
grain = [500, 400, 600, 500]
meat = [400, 500, 450, 350]

# Plot line chart
ax.plot(year, fruits, label="Fruits", color="red", lw=2, marker="o")
ax.plot(year, vegetables, label="Vegetables", color="green", lw=2, marker="o")
ax.plot(year, grain, label="Grain", color="blue", lw=2, marker="o")
ax.plot(year, meat, label="Meat", color="magenta", lw=2, marker="o")

# Set xy-axis label
ax.set_xlabel("Year")
ax.set_ylabel("Production")

# Set xy-axis limit
ax.set_xlim(2000, 2005)
ax.set_ylim(0, 600)

# Set xticks
ax.set_xticks(year)

# Set legend
ax.legend(loc="best")

# Set title
ax.set_title("Food Production in the US from 2001 to 2004")

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig("line chart/png/80.png")

# Clear figure
plt.clf()