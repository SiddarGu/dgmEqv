import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Provided data in a format that could be directly copied into a Python script
data = np.array([
    [1030, 14.2, 1.75, 3.2],
    [750, 13.8, 2.10, 2.8],
    [4000, 35.9, 0.95, 5.4],
    [2200, 22.0, 1.50, 3.0],
    [1830, 15.4, 1.78, 4.1],
    [1670, 18.5, 2.30, 4.0],
    [1450, 10.1, 1.25, 2.0],
    [1900, 20.4, 2.40, 4.5],
    [680, 16.3, 4.10, 6.2],
    [2500, 28.7, 2.85, 3.6],
    [3100, 25.3, 1.20, 3.8]
])

data_labels = ["Monthly Production (Metric Tons)", "Revenue (Million USD)", "Average Product Price (USD)", "Year-Over-Year Growth (%)"]
line_labels = ["Snacks", "Confections", "Beverages", "Dairy Products", "Bakery Goods", "Frozen Foods", "Canned Foods", "Ready-to-Eat Meals", "Health Foods", "Alcoholic Beverages", "Non-Alcoholic Beverages"]

# Plot types corresponding to each data column
plot_types = ['line', 'bar', 'line', 'scatter']

# Create figure and initial subplot
plt.figure(figsize=(21, 10))
ax1 = plt.subplot(111)
color = 'tab:blue'
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color=color)
ax1.plot(line_labels, data[:,0], color=color, label=data_labels[0])
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(loc='upper left')
ax1.yaxis.set_major_locator(AutoLocator())

# Variable to track offset for bar separation
bar_width = 0.2
bar_positions = np.arange(len(line_labels))
bar_idx = 0

# Additional axes
axes = [ax1]

for i in range(1, len(data_labels)):
    ax = axes[0].twinx()
    axes.append(ax)
    color = f'tab:{["orange", "green", "red"][i-1]}'
    if plot_types[i] == 'line':
        ax.set_ylabel(data_labels[i], color=color)
        ax.plot(line_labels, data[:, i], color=color, label=data_labels[i])
        ax.tick_params(axis='y', labelcolor=color)
    elif plot_types[i] == 'bar':
        ax.set_ylabel(data_labels[i], color=color)
        ax.bar(bar_positions + bar_idx * bar_width, data[:, i], bar_width, label=data_labels[i], alpha=0.7, color=color)
        bar_idx += 1
    elif plot_types[i] == 'scatter':
        ax.set_ylabel(data_labels[i], color=color)
        ax.scatter(line_labels, data[:, i], color=color, label=data_labels[i], zorder=5)
        ax.tick_params(axis='y', labelcolor=color)
    ax.legend(loc='upper right' if i % 2 == 0 else 'center right', bbox_to_anchor=(1.1+0.05*i, 0.5))
    ax.yaxis.set_major_locator(AutoLocator())

    # Seperate different y-axes
    if i > 1:
        spine = ax.spines['right']
        spine.set_position(('outward', 70 * (i - 1)))

# Set plot title
plt.title('Food and Beverage Industry Production and Growth Insight')

# Automatically resize layout
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/56_2023122291723.png')

# Clear the current figure
plt.clf()
