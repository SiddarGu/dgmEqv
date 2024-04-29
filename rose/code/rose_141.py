
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Stocks', 'Bonds', 'Mutual Funds', 'Real Estate', 'Forex', 'Options', 'Commodities']
data = [85, 50, 60, 90, 20, 30, 75]
line_labels = ['Investment Type', 'Amount']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Draw sectors corresponding to different categories
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, alpha=0.5, color=plt.cm.Set3(i), label=data_labels[i])

# Set the title
ax.set_title('Investment Allocation in Business and Finance in 2021')

# Set the ticks and labels for each category
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12, wrap=True)

# Reposition the legend so that it does not cover any part of the chart
ax.legend(data_labels, bbox_to_anchor=(1.25, 1.1))

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_16.png')

# Clear the current image state
plt.clf()