
import matplotlib.pyplot as plt
import numpy as np

# Generate data
data = np.array([[2000, 3000,2500,2000,1000],[2001,3500,2800,2200,1200],[2002,4000,3200,2400,1400],[2003,4500,3600,2600,1600]])

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1,1,1)

# Set x and y axis
x = data[:, 0]
y1 = data[:, 1]
y2 = data[:, 2]
y3 = data[:, 3]
y4 = data[:, 4]

# Set xticks
plt.xticks(x, rotation=45)

# Plot data
ax.plot(x, y1, label="Fast Food Revenue(billion dollars)", color="blue", linestyle="--")
ax.plot(x, y2, label="Beverage Revenue(billion dollars)", color="green", linestyle="-.")
ax.plot(x, y3, label="Grocery Revenue(billion dollars)", color="red", linestyle=":")
ax.plot(x, y4, label="Restaurant Revenue(billion dollars)", color="orange")

# Add title and legend
ax.set_title("Revenue growth of food and beverage industry in the US from 2000 to 2003")
legend=ax.legend(loc="upper right", shadow=True, fontsize="small", ncol=2, fancybox=True)

# Set background grid
ax.grid(axis="both", linestyle="-", linewidth="0.5", color="gray")

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig("line chart/png/168.png")

# Clear the current image state
plt.clf()