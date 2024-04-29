
import matplotlib.pyplot as plt
import numpy as np

# Get data
y_values = ["Number of Patients Treated (Million)", "Total Expenditure ($Trillion)", "Cost per Patient ($)",]
x_values = ["Primary Care", "Outpatient Services", "Inpatient Services", "Mental Health"]
data = np.array([[2.1, 1.5, 0.7], [3.6, 3.0, 0.8], [1.2, 2.7, 2.2], [0.9, 1.2, 1.3]])

# Plot 3D bar chart
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    xpos = np.arange(len(x_values))
    ypos = [i] * len(x_values)
    zpos = np.zeros(len(x_values))
    
    dx = np.ones(len(x_values))
    dy = np.ones(len(x_values))
    dz = data[:, i]
    
    # Set the dimensions of the bars (width, depth, colors, alpha, etc)
    if i == 0:
        ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#0094FF', alpha=0.5)
    elif i == 1:
        ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#FF7F50', alpha=0.5)
    else:
        ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#9ACD32', alpha=0.5)

# Set plot labels and other details
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=20)
ax.set_yticklabels(y_values)
ax.view_init(30, -90)
plt.title("Healthcare and Health Services - Patient Volume and Expenditure Analysis")

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/25_202312251044.png")

# Clear the current image state
plt.cla()