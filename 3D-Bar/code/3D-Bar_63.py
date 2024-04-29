import matplotlib.pyplot as plt
import numpy as np

# Create labeled data
labels = [
    ["New York", "400", "360", "700"],
    ["Los Angeles", "340", "320", "650"],
    ["Chicago", "375", "395", "580"],
    ["Houston", "245", "290", "350"],
    ["Phoenix", "325", "340", "500"]
]

# Convert data into numpy array
data = np.array(labels)

# Extract x_values, y_values and data
x_values = data[:, 0]
y_values = ["New Constructions (Units)", "Sold Properties (Units)", "Median House Price ($000)"]
data = np.float32(data[:, 1:])

# Create 3D bar chart
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Draw bars
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), np.array([i]*len(x_values)), np.zeros(len(x_values)), 
             0.4, 0.8, data[:, i])

# Set titles
plt.title("Comparative Real Estate Market Analysis across major US Cities")

# Set labels and ticks
ax.set_xlabel("Cities")
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_ylabel("Metrics")
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
ax.set_zlabel("Counts")

# Adjust viewing angle for better readability
ax.view_init(elev=20, azim=-35)
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/161_202312302235.png", dpi=300)

# Clear the figure
plt.clf()
