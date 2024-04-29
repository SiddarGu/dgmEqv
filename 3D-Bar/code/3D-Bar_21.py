
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
y_values = ['Consumption (Million Tonnes)', 'Average Price ($/Tonne)', 'Number of Suppliers']
data = np.array([[100, 500, 300], [150, 400, 250], [200, 350, 450], [250, 300, 600], [50, 550, 200]])
x_values = ['Dairy', 'Fruits', 'Vegetables', 'Grains', 'Oils']

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot data
for i in range(len(y_values)):
    X = np.arange(len(x_values))
    Y = [i] * len(x_values)
    Z = data[:, i]
    ax.bar3d(X, Y, np.zeros_like(Z), 1, 1, Z, shade=True, alpha=0.3 * (i + 1))

# Set the title of the figure
ax.set_title('Food and Beverage Industry Consumption and Prices - Overview')

# Set the dimensions of the bars
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))

# Label x-axis
ax.set_xticklabels(x_values, rotation=45)

# Label y-axis
ax.set_yticklabels(y_values)

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/3.png')

# Clear the image state
plt.clf()