import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
import numpy as np

# Given data
data_str = """Corn,175,4.20,8000,38,12
Wheat,49,5.35,22000,2,60
Soybeans,52,10.22,11250,18,6
Rice,7500,12.80,4000,0,72
Barley,72,3.80,560,5,15
Sorghum,80,3.67,2500,50,3
Potatoes,45000,0.15,380,0,85
Tomatoes,35000,0.70,500,0,90
Grapes,12800,1.80,3500,0,70
Apples,850,0.55,650,0,80"""

# Transforming data
data_labels = ["Yield Per Acre (Bushels)", "Market Price (Dollars per Bushel)", 
               "Export Volume (Thousands of Tonnes)", "Use in Biofuel Production (%)", 
               "Fresh Consumption Rate (%)"]
line_labels = [line.split(',')[0] for line in data_str.splitlines()]
data = np.array([line.split(',')[1:] for line in data_str.splitlines()], dtype=np.float32)

# Plot types
plot_types = ['bar', 'scatter', 'line', 'area', 'area']

# Create the figure and primary y-axis (ax1)
fig, ax1 = plt.subplots(figsize=(25, 15))
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color='tab:blue')
ax1.bar(line_labels, data[:, 0], color='tab:blue', alpha=0.7, label=data_labels[0])
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.legend(loc='upper left')

# Plot remaining data
axes = [ax1]
colors = ['tab:green', 'tab:red', 'tab:purple', 'tab:orange']
for i in range(1, len(data_labels)):
    ax = ax1.twinx()
    axes.append(ax)
    color = colors[(i-1) % len(colors)]

    if plot_types[i] == 'bar':
        ax.bar(line_labels, data[:, i], color=color, alpha=0.7, label=data_labels[i], width=0.1, position=i)
    elif plot_types[i] == 'scatter':
        ax.scatter(line_labels, data[:, i], color=color, label=data_labels[i])
    elif plot_types[i] == 'line':
        ax.plot(line_labels, data[:, i], color=color, label=data_labels[i])
    elif plot_types[i] == 'area':
        ax.fill_between(line_labels, data[:, i], alpha=0.5, color=color, label=data_labels[i])
    
    ax.set_ylabel(data_labels[i], color=color)
    ax.tick_params(axis='y', labelcolor=color)
    if i > 1:  # Position the spines for secondary y-axes
        spine = ax.spines['right']
        spine.set_position(('outward', 60 * (i-1)))
    
    ax.yaxis.set_major_locator(AutoLocator())
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1 - (0.1 * i)))

# Set the title and layout
plt.title('Insights into Agriculture: Crop Yields, Market Pricing, and Distribution Patterns')
plt.tight_layout()

# Save the image and clear the state
save_path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/55_2023122291723.png'
plt.savefig(save_path)
plt.clf()
