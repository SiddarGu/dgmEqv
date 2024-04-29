import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO

# Transform the data into the required format
data_str = """Renewable Energy Sources,800,1000,5000,200
Energy Efficient Technologies,1200,1500,6000,250
Green Buildings,600,750,4000,150
Water Conservation,1000,1250,7000,300
Waste Management,1400,1750,8000,350
Environmental Education,200,250,1000,50
Transportation Efficiency,1800,2250,9000,400
Sustainable Agriculture,1600,2000,8500,350
Pollution Control,1400,1750,8000,300
Climate Change Adaptation,1900,2400,9500,450"""
df = pd.read_csv(StringIO(data_str), header=None)
line_labels = df[0]
data = df.drop(0, axis=1).astype(float).values
data_labels = ['Energy Consumption (Mega Joules)', 'Carbon Footprint (Metric Tons CO2e)', 'Water Usage (Gallons)', 'Waste Generation (Tons)']

# Create figure and add axes
fig, ax1 = plt.figure(figsize=(24,10)), plt.gca()

# Plotting the data
colors = ['b', 'g', 'r', 'y']
for i in range(data.shape[1]):
    if i == 0:
        ax1.bar(line_labels, data[:, i], color=colors[i], alpha=0.7, label=data_labels[i])
    else:
        ax2 = ax1.twinx()
        ax2.spines["right"].set_position(("axes", 1 + 0.1 * (i-1)))
        if i == 1:
            ax2.scatter(line_labels, data[:, i], color=colors[i], alpha=0.7, label=data_labels[i])
        elif i == 2:
            ax2.plot(line_labels, data[:, i], color=colors[i], alpha=0.7, label=data_labels[i])
        elif i == 3:
            ax2.fill_between(line_labels, 0, data[:, i], color=colors[i], alpha=0.5, label=data_labels[i])
        ax2.set_ylabel(data_labels[i], color=colors[i])
        ax2.legend(loc="upper left", bbox_to_anchor=(0, 0.6 + 0.1 * i))

# Setting common labels and title
ax1.set_xlabel('Category')
ax1.set_title('Environmental Sustainability Indicators: Energy, Emissions, Water, and Waste')
ax1.legend(loc="upper left", bbox_to_anchor=(0, 0.6))

# Rotate x-axis labels for better visibility
plt.setp(ax1.get_xticklabels(), rotation=45)

# Adjust layout
plt.tight_layout()

# Save figure to local disk
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/336_202312311430.png')
plt.clf()
