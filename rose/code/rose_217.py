
import matplotlib.pyplot as plt
import numpy as np

# Transform data into three variables
data_labels = ['Life Insurance', 'Banking', 'Mutual Funds', 'Real Estate', 'Stocks', 'Bonds', 'Credit Cards', 'Financial Planning']
data = [250, 200, 150, 100, 80, 60, 40, 20]
line_labels = ['Financial Product', 'Number of Customers']

# Plot data with type of rose chart
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

sector_angle = (2 * np.pi) / len(data_labels)
color_list = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'black']

for i in range(len(data_labels)):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=color_list[i], label=data_labels[i])

ax.set_title("Popularity of Financial Products in 2021")

# Position the legend outside of the chart area
ax.legend(bbox_to_anchor=(1.1, 1.1), labels=data_labels)

# Set the category labels at the center of each sector
ax.set_xticks(sector_angle * np.arange(len(data_labels)))
ax.set_xticklabels(data_labels)

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_29.png')

# Clear the current image state
plt.clf()