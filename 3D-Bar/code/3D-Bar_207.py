
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: y_values, data, x_values. 
y_values = ["Number of Users (Millions)", "Number of Devices (Millions)", "Number of Transactions (Millions)"]
x_values = ["Smartphones", "Tablets", "Laptops", "Desktops", "Wearables"]
data = np.array([[5, 8, 20], [2, 3, 15], [8, 9, 30], [2, 3, 10], [1, 2, 5]])

# Plot the data with the type of 3D bar chart.
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:, i], alpha=0.7, color=['b','g','r','c','m'], edgecolor='k')

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# Add title
plt.title("Technology and Internet Usage - An Analysis of Global Trends")

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/5_202312270030.png")

# Clear the current image state
plt.clf()