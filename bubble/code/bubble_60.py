import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# Formatting the data
csv_values = ['Developed Countries,2000,80,40,90', 'Developing Countries,500,65,30,70', 'Low-income Countries,100,55,20,50', 'High-income Countries,1500,75,35,85', 'Middle-income Countries,800,70,25,75']

# Extracting labels and data
data_labels = ['Healthcare Expenditure (Billion $)', 'Life Expectancy (Years)', 'Healthcare Providers (per 1000 people)', 'Healthcare Access (Score)']
line_labels = [f"{label.split(',')[0]} ({label.split(',')[2]})" for label in csv_values]
data = np.array([list(map(int, x.split(',')[1:])) for x in csv_values])

# Normalizing colors
norm = Normalize(data[:, 3].min(), data[:, 3].max())
colors = [get_cmap('viridis')(norm(value)) for value in data[:, 3]]

# Creating figure and subplots
fig, ax = plt.subplots(figsize=(12, 10))

# Plotting data
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], s=data[i, 2]*75, c=colors[i], label=None)
    ax.scatter([], [], s=20, c=colors[i], label=line_labels[i])

# Setting labels 
ax.set_xlabel(data_labels[0], fontsize=14)
ax.set_ylabel(data_labels[1], fontsize=14)

# Adding a title 
plt.title('Healthcare Expenditure and Access by Country Category', fontsize=16)

# Plotting the legend and setting its title
legend = ax.legend(title=data_labels[2], loc="upper left")
legend.get_title().set_fontsize('13')

# Adding colorbar
sm = plt.cm.ScalarMappable(cmap=get_cmap('viridis'), norm=norm)
sm.set_array([])
fig.colorbar(sm, label=data_labels[3])

# Save the image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/382_202312311429.png', dpi=100)
plt.clf()
