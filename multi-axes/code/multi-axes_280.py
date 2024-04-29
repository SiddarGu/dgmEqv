import matplotlib.pyplot as plt
import numpy as np

# Define data
data_labels = ['Life Expectancy (Years)', 'Healthcare Spending (Billion USD)', 'Adult Obesity Percentage', 'Infant Mortality Rate/1000 Live Births']
line_labels = np.arange(2010, 2020)
raw_data = [
    [78.7, 2.6, 30.4, 6.1],
    [78.7, 2.7, 30.6, 6.0],
    [78.8, 2.7, 30.7, 5.9],
    [78.8, 2.8, 30.9, 5.8],
    [78.9, 3.0, 31.3, 5.7],
    [78.9, 3.2, 31.8, 5.6],
    [78.8, 3.3, 32.2, 5.6],
    [78.6, 3.5, 32.4, 5.7],
    [78.5, 3.6, 32.8, 5.8],
    [78.9, 3.8, 33.1, 5.8]
]
data = np.array(raw_data)

# Create figure
fig, ax1 = plt.subplots(figsize=(20, 10))

# Line chart
ln1 = ax1.plot(line_labels, data[:,0], color='r', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='r')
ax1.tick_params(axis='y', colors='r')
ax1.grid(True)

# Scatter chart
ax2 = ax1.twinx()
ln2 = ax2.scatter(line_labels, data[:,1], color='g', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='g')
ax2.tick_params(axis='y', colors='g')

# Bar chart
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.2))
ln3 = ax3.bar(line_labels, data[:,2], color='b', label=data_labels[2], alpha=0.6)
ax3.set_ylabel(data_labels[2], color='b')
ax3.tick_params(axis='y', colors='b')

# Area chart
ax4 = ax1.twinx()
ax4.spines['right'].set_position(('axes', 1.4))
ln4 = ax4.fill_between(line_labels, data[:,3], color='y', label=data_labels[3], alpha=0.6)
ax4.set_ylabel(data_labels[3], color='y')
ax4.tick_params(axis='y', colors='y')

# Legends and title
lns = ln1 + [ln2] + [ln3] + [ln4]
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc='center left', bbox_to_anchor=(1.15, 0.5))
ax1.set_title('Health and Healthcare in the United States: 2010-2019')

# Save the plot
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/192_202312310150.png")
plt.clf()
