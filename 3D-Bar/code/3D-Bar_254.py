import numpy as np
import matplotlib.pyplot as plt

# Define data
data_str = """Platform,Number of Users (Millions),Time Spent per Day (Minutes),Ad Revenue ($Billion)
Facebook,28,38,85
Instagram,10,30,20
Twitter,33,31,3.5
YouTube,20,40,15
Pinterest,45,14,1.69"""
lines = data_str.split("\n")

# Transform input string into three variables
x_values = [line.split(",")[0] for line in lines[1:]]
data = np.array([line.split(",")[1:] for line in lines[1:]], dtype=np.float32)
y_values = lines[0].split(",")[1:]

# Create a figure
fig = plt.figure(figsize=(10, 8))

# Add a subplot with 3D projection
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.5, 0.5, data[:, i], alpha=0.5)

# Set labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

# Set title
plt.title("Social Media Platforms: User Engagement and Ad Revenue Comparison")

# Change the viewing angle for better visualization
ax.view_init(elev=20., azim=-35)

# Save figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/245_202312310050.png", dpi=300)

# Clear the figure to free memory
plt.clf()
