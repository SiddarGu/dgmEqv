
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
y_values = ['Global CO2 Emissions (Gigatonnes)', 'Renewable Energy Sources (% of Total Energy)', 'Average Global Temperature (°C)']
data = np.array([[38.8, 17.5, 11.1], [39.3, 18.2, 11.2], [39.9, 18.9, 11.4], [40.3, 19.6, 11.5], [41, 20.3, 11.7]])
x_values = ['2019', '2020', '2021', '2022', '2023']

# Plot the data with the type of 3D bar chart
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:,i], shade=True, alpha=0.5, color=['b', 'g', 'r', 'c', 'k'][i])

# Set the dimensions of the bars
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=90)
ax.set_yticklabels(y_values, ha='left')
ax.view_init(30, -15)
# Add background grids and titles
ax.set_title('Environmental Sustainability Trends - 2019 to 2023')
ax.grid(True)

# Automatically resize the image by tight_layout() before savefig()
fig.tight_layout()

# Save the image
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/38_202312270030.png')

# Clear the current image state
plt.clf()