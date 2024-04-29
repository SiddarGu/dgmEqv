import numpy as np
import matplotlib.pyplot as plt

# Define data
data = np.array([[2000, 2100, 2150, 2200, 2250],
                 [1500, 1525, 1550, 1600, 1650],
                 [500, 550, 600, 650, 700]], dtype=np.float32)
x_values = ['2019', '2020', '2021', '2022', '2023']
y_values = ['Undergraduates', 'Graduates', 'PhDs']

# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Create 3D bar plot
for i in range(data.shape[0]):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
             dz=data[i, :], dx=0.4, dy=0.8, zsort='average', color='b', alpha=0.5)

# Rotate x-axis labels for better readability
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=30)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# Set Title
plt.title("Annual Student Enrollment in an Academic Institution from 2019 to 2023")

# Adjust view angle for better readability
ax.view_init(azim=130)

# Adjust labels to avoid overlapping
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/179_202312302235.png')

# Clear the current figure
plt.clf()
