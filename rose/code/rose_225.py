

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data = np.array([[1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]])
data_labels = np.array(['Investment', 'Credit', 'Loans', 'Insurance', 'Banking', 'Taxes', 'Real Estate', 'Stocks', 'Accounting', 'Economics'])
line_labels = np.array([['Category', 'Value']])

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='polar')
colors = ['red','orange','yellow','green','blue','indigo','violet','brown','gray','black']
sector_angle = (2 * np.pi) / len(data_labels)
for i in range(len(data_labels)):
    ax.bar(sector_angle*i, data[0][i], width=sector_angle, color=colors[i], label=data_labels[i])
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10, horizontalalignment='center')
ax.legend(bbox_to_anchor=(1.2, 0.5), labels=data_labels)
plt.title('Financial Investments by Category in 2021')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_45.png', dpi=300)
plt.clf()