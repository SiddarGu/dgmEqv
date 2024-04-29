
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data 
y_values = ["Number of Social Network Users (Millions)", "Time Spent on Social Media (Minutes/Day)", "Number of Websites (Millions)"]
data = np.array([[245, 140, 100], [500, 90, 50], [750, 80, 200], [60, 120, 120], [23, 100, 80]]) 
x_values = ["USA", "India", "China", "UK", "Australia"]

# Create figure
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111, projection='3d')

# Plot the data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.5, 0.5, data[:,i], color=plt.cm.viridis(i/len(y_values)), alpha=0.8)

# Set labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# Set title
ax.set_title("Global Social Media and Web Landscape - 2019")

# Set background grids
ax.grid(b=True, which='major', axis='both')
# Rotate the X-axis labels for better readability
ax.view_init(elev=30, azim=-20)

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/7_202312251036.png")

# Clear the current image state
plt.cla()
plt.clf()
plt.close()