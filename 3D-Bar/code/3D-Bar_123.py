import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parse the data
data_string = 'Year,Coal Production (Million Tonnes),Natural Gas Production (Billion Cubic Feet),Oil Production (Million Barrels),Renewable Energy (GWh)\n 2017,3500,3000,2800,3200\n 2018,3400,3150,2900,3300\n 2019,3300,3200,3100,3400\n 2020,3100,3250,3200,3600\n 2021,3000,3300,3400,3800'
lines = data_string.split('\n')

# Prepare the three variables 
titles = lines[0].split(',')[1:]
x_values = [line.split(',')[0] for line in lines[1:]]
y_values = np.arange(len(titles))
data = np.array([list(map(int, line.split(',')[1:])) for line in lines[1:]], dtype=np.float32)

# Set up the figure and axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
width = 0.8

# Plot each column of data
for i in y_values:
  ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
           width, width, data[:, i], shade=True)

# Set x and y ticks and labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(titles)))
ax.set_xticklabels(x_values, rotation='vertical')
ax.set_yticklabels(titles, ha='left')
ax.set_zlabel('Production')

# Set title
plt.title('Energy Production in Different Sectors - 2017 to 2021')

# Adjust viewing angle
ax.view_init(25, -60)

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/258_202312310050.png')

# Clear the current image
plt.clf()
