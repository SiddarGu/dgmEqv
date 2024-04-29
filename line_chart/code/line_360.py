
import matplotlib.pyplot as plt
import numpy as np

# Create figure and subplot
fig, ax = plt.subplots(figsize=(16, 9))

# Set x-axis
x = np.array([2017, 2018, 2019, 2020])

# Set y-axis
y1 = np.array([50, 60, 70, 80])
y2 = np.array([20, 25, 30, 35])
y3 = np.array([5, 3, 2, 1])

# Plot the data
ax.plot(x, y1, label="Voter Turnout(%)", marker="o", linewidth=3,
        markersize=12, linestyle="--")
ax.plot(x, y2, label="Tax Rate(%)", marker="^", linewidth=3,
        markersize=12, linestyle="-.")
ax.plot(x, y3, label="Unemployment Rate(%)", marker="s", linewidth=3,
        markersize=12, linestyle=":")

# Set the title and labels
ax.set_title("Impact of Government Policies on Voter Turnout, Tax Rate, and Unemployment Rate in the US from 2017 to 2020")
ax.set_xlabel("Year")
ax.set_ylabel("Percentage (%)")

# Set the position and style of the legend
ax.legend(loc="upper left", fontsize=12, ncol=3, framealpha=0.5)

# Set x-axis ticker
ax.set_xticks(x)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig("line chart/png/144.png", format="png")

# Clear the current image state
plt.clf()