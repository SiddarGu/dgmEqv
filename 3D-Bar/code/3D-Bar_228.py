
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
y_values = ['Wheat Production (Million Tonnes)', 'Corn Production (Million Tonnes)', 'Rice Production (Million Tonnes)', 'Soybean Production (Million Tonnes)']
x_values = ['North', 'South', 'East', 'West']
data = np.array([[30, 40, 20, 10], [35, 45, 22, 12], [32, 42, 21, 11], [33, 43, 23, 13]])

# Create figure before plotting
fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    ax.bar3d(xs, ys, np.zeros_like(data[:,i]),
            dx=0.3, dy=0.3, dz=data[:,i],
            color=['#f9b1c3', '#f1a59c', '#e99982', '#e19073'], alpha=0.5)
    
# Set different dimensions of the bars to make them distinct
ax.set_xlabel('Regions', fontsize=14, labelpad=15)
ax.set_ylabel('Crop Types', fontsize=14, labelpad=15)
ax.set_zlabel('Production (Million Tonnes)', fontsize=14, labelpad=15)
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=-25)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.view_init(elev=15, azim=20)

# Add background grids
ax.grid(b=True, which='major', axis='both', linestyle='dotted', alpha=0.3)

# Set the title of the figure
ax.set_title('Regional Trends in Food Production - Wheat, Corn, Rice and Soybeans')

# Adjust the image layout
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/7.png')

# Clear the current image state
plt.clf()