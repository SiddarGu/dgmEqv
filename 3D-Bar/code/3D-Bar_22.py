
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
y_values = ['Renewable Energy Production (Million KWh)', 'Coal Production (Million KWh)', 'Natural Gas Production (Million KWh)', 'Oil Production (Million KWh)']
x_values = ['2019', '2020', '2021', '2022', '2023']
data = np.array([[2400, 2600, 2700, 3000, 3200],
                 [3000, 2700, 2500, 2600, 2700],
                 [4000, 4500, 4700, 4800, 5000],
                 [2500, 2400, 2300, 2200, 2100]])

# Create figure before plotting
fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    ax.bar3d(xs, ys, [0]*len(x_values), 1, 1, data[i,:], shade=True, alpha=0.5, color=plt.cm.tab20(i))

# Set the dimensions of the bars
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation='vertical')
ax.set_yticklabels(y_values, ha='left', rotation=-15)

# Set title for the figure
ax.set_title("Environmental Sustainability in Energy Production - 2019 to 2023")

# Resize the image before savefig
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/2_202312270030.png')

# Clear the current image state
plt.close()