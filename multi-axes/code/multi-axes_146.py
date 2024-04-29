import matplotlib.pyplot as plt
import numpy as np

# Data transformation
raw_data = '''
Fast Food,57,32,44,18
Casual Dining,45,20,56,23
Fine Dining,40,25,60,15
Coffee & Snack Shops,62,35,46,20
Food Trucks,27,14,52,12
Bakeries,33,19,57,17
Breweries,72,42,42,25
Specialty Foods,53,30,57,22
Organic Products,48,35,58,19
Health Food Stores,39,23,59,21
Supermarkets,96,55,43,28
Convenience Stores,30,16,54,13
Online Grocery Sales,45,24,58,16
Catering Services,52,28,56,24
'''

lines = raw_data.strip().split('\n')
data_labels = ['Revenue (Millions)', 'Cost of Goods Sold (Millions)', 'Gross Margin (%)', 'Market Share (%)']
line_labels = [line.split(',')[0] for line in lines]
data = np.array([list(map(float, line.split(',')[1:])) for line in lines])

# Setup the figure and axes
fig, ax1 = plt.figure(figsize=(15, 10)), plt.gca()

# Colors for each plot
colors = ['blue', 'green', 'red', 'purple']

# Plot the first dataset as bars
bar_width = 0.2
ind = np.arange(len(data))
bar_positions = ind - bar_width * 1.5

for i in range(data.shape[1]):
    if i == 0:
        ax1.bar(bar_positions, data[:, i], bar_width, color=colors[i], alpha=0.7)
        ax1.set_ylabel(data_labels[i], color=colors[i])
        ax1.tick_params(axis='y', labelcolor=colors[i])
        ax1.set_xticks(ind)
        ax1.set_xticklabels(line_labels, rotation=45, ha='right')
    else:
        ax = ax1.twinx()
        ax.spines['right'].set_position(('outward', 60 * (i - 1)))
        if i == 2:
            ax.plot(line_labels, data[:, i], color=colors[i])
        elif i == 1:
            ax.fill_between(line_labels, 0, data[:, i], color=colors[i], alpha=0.5)
        elif i == 3:
            ax.scatter(line_labels, data[:, i], color=colors[i])
        ax.set_ylabel(data_labels[i], color=colors[i])
        ax.tick_params(axis='y', labelcolor=colors[i])

    bar_positions += bar_width

# Set title and layout
plt.title('Gourmet vs. Convenience: Food & Beverage Sector Financial Overview', fontsize=16)
plt.tight_layout()

# Save the plot
save_path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/54_2023122291723.png'
plt.savefig(save_path, dpi=300)

# Clear the current figure state after saving
plt.clf()
