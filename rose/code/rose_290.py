

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Stock', 'Bonds', 'Mutual Funds', 'Real Estate', 'Currency Trading', 'Commodities', 'Insurance', 'Cryptocurrency', 'Savings Accounts', 'Retirement Accounts']
data = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]
line_labels = ['Investment Type', 'Amount']

# Create figure 
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

# Calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot data with rose chart
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color='C' + str(i))
    ax.set_xticks(sector_angle * np.arange(num_categories))
    ax.set_xticklabels(data_labels, wrap=True, fontsize=8)

# Plot legend
ax.legend(data_labels, bbox_to_anchor=(1.2, 1.05))

# Title
ax.set_title('Investment Portfolio Breakdown in 2021')

# Save image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_97.png')

# Clear current image
plt.clf()