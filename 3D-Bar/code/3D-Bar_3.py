
import numpy as np
import matplotlib.pyplot as plt

# Transform data to variables
y_values = ["GDP per Capita (K USD)", "Life Expectancy (Years)", "Unemployment Rate (%)"]
data = np.array([[63, 78.1, 37], [50, 81.9, 77], [45, 81.5, 39], [60, 82.5, 52], [45, 82.0, 42]])
x_values = ["USA", "Canada", "UK", "Australia", "New Zealand"]

# Create figure
fig = plt.figure(figsize=(9, 5))
ax = fig.add_subplot(111, projection='3d')

# Set X, Y coordinates
X = np.arange(len(x_values))
Y = np.arange(len(y_values))
X, Y = np.meshgrid(X, Y)

# Plot 3D bar chart
for i in range(len(y_values)):
    ax.bar3d(X[i], Y[i], np.zeros_like(data[:, i]), 1, 1, data[:, i], alpha=0.5, shade=True, color='lightblue')

# Set X-axis labels
x_range = np.arange(len(x_values))
ax.set_xticks(x_range)
ax.set_xticklabels(x_values, rotation=45)

# Set Y-axis labels
y_range = np.arange(len(y_values))
ax.set_yticks(y_range)
ax.set_yticklabels(y_values)
# Rotate the X-axis labels for better readability
ax.view_init(elev=30, azim=20)
# Set figure title
ax.set_title("Socio-economic Indicators Comparison Across Countries")

# Set size
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/11.png')

# Clear image
plt.clf()