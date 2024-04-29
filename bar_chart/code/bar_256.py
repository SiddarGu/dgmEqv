
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig=plt.figure(figsize=(10,6))

# Set data
states = ["California","New York","Texas","Florida"]
donations = [500,600,400,700]
volunteers = [4500,3500,5000,4000]

# Plot bar chart
ax = fig.add_subplot(111)
ax.bar(np.arange(len(states))-0.2, donations, width=0.4, label="Charitable Donations (million $)")
ax.bar(np.arange(len(states))+0.2, volunteers, width=0.4, label="Number of Volunteers")

# Add legend
plt.legend(loc="upper left", bbox_to_anchor=(1.0, 1.0))

# Add title
plt.title("Charitable donations and volunteer numbers in four states in 2021")

# Add xticks
plt.xticks(np.arange(len(states)), states, rotation=45, wrap=True)

# Resize image
fig.tight_layout()

# Save image
plt.savefig("bar chart/png/367.png")

# Clear current image
plt.clf()