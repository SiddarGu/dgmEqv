
import matplotlib.pyplot as plt
import numpy as np

# Transform data into different variables
data_labels = ['Online Shopping', 'In-Store Shopping', 'Delivery Services', 'Mobile Shopping',
               'Payment Services', 'Online Advertising', 'Online Marketplaces', 'E-Commerce Platforms']
data = [400, 350, 300, 250, 200, 150, 100, 50]
line_labels = ['Category','Number of Transactions']

# Set up the figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
fig.suptitle('Number of E-Commerce Transactions in 2020')

# Calculate the sector angle
sector_angle = (2 * np.pi) / len(data_labels)

# Draw the sectors
for i in range(len(data_labels)):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i))
    
# Set the legend position
ax.legend(bbox_to_anchor=(1.2, 1), loc='upper right', ncol=1)

# Set the x-axis labels
ax.set_xticks([sector_angle * i for i in range(len(data_labels))])
ax.set_xticklabels(data_labels, fontsize=10, fontweight='bold', ha='center', va='top')

# Finalize the plot
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-082906_11.png')
plt.clf()