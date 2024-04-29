
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
y_values = ['Air Quality Index', 'Water Quality Index', 'Carbon Emissions (Million Tonnes)', 'Energy Efficiency (Kilowatt Hours/Million GDP)']
data = np.array([[60,90,500,200],[65,85,400,220],[68,82,380,240],[72,80,360,260],[76,78,340,280]])
x_values = ['2019', '2020', '2021', '2022', '2023']

# Plot the data with the type of 3D bar chart
fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.5, 0.5, data[:,i], alpha=0.8, color=[i/len(y_values), 0.3, 0.4])

# Set the dimensions of the bars
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.view_init(elev=15, azim=135)
ax.set_title('Environmental Sustainability - A Look at Key Indicators from 2019 to 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/33_202312251044.png')
plt.clf()