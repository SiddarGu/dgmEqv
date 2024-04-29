
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Education', 'Environment', 'Transportation', 'Social Services', 'Immigration', 'Fiscal and Monetary', 'Health and Safety', 'Defense', 'Energy']
data = [25, 22, 64, 12, 30, 87, 45, 55, 81]
line_labels = ['Policy Area', 'Number']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], edgecolor='k', color=plt.cm.jet(i/num_categories))

ax.legend(bbox_to_anchor=(1.15, 1), labels=data_labels)
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, rotation=45, wrap=True)
ax.set_title('Government and Public Policy Outcomes in 2021')
fig.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-082906_14.png')
plt.close()