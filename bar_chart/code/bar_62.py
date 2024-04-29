
import matplotlib.pyplot as plt
import numpy as np

# Define data
regions = ["East","West","North","South"]
electricity = [1000, 1200, 1400, 950]
gas = [200, 220, 240, 260]
oil = [50, 60, 70, 80]

# Create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

# Plot data
ax.bar(regions, electricity, label="Electricity", color="b")
ax.bar(regions, gas, bottom=electricity, label="Gas", color="g")
ax.bar(regions, oil, bottom=np.array(electricity)+np.array(gas), label="Oil", color="r")

# Set title and labels
ax.set_title("Energy consumption in four regions in 2021")
ax.set_xlabel("Region")
ax.set_ylabel("Consumption")

# Show legend
plt.legend(loc="upper right")

# Set x-axis ticks
plt.xticks(regions)

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig("bar chart/png/87.png")

# Clear current image
plt.clf()