
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(16, 8))

# Set data
x = np.array([25, 30, 35, 40, 45])
y_pressure = np.array([50, 40, 30, 20, 10])
y_volume = np.array([2, 4, 7, 9, 11])

# Plot data
plt.plot(x, y_pressure, label="Pressure(psi)", color="b")
plt.plot(x, y_volume, label="Volume(L)", color="r")

# Set x, y labels
plt.xlabel("Temperature(degrees)")
plt.ylabel("Value")

# Set title
plt.title("Temperature Effect on Pressure and Volume of a Gas at Constant Amount")

# Set legend
plt.legend(loc=2)

# Set x, y ticks
plt.xticks(x)
plt.yticks(np.arange(np.min(y_pressure), np.max(y_volume) + 1))

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig("line chart/png/460.png")

# Clear current image
plt.clf()