
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Investment', 'Taxation', 'Business Administration', 'Economics', 'Accounting', 'Securities', 'Financial Regulation', 'Insurance', 'Banking']
data = [90, 80, 70, 60, 50, 40, 30, 20, 10]
line_labels = ['Category', 'Number']

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=plt.cm.jet(i/num_categories), label=data_labels[i])

ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12, color='black', wrap=True, rotation=45)
ax.set_title('Popular Business and Finance Fields in 2021', fontsize=20, color="black")

ax.legend(bbox_to_anchor=(1.2, 1.05), loc='upper right', fontsize=14)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_97.png')
plt.cla()