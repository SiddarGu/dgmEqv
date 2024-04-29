
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Investment Banking', 'Corporate Finance', 'Financial Analysis', 'Financial Planning', 'Risk Management', 'Mergers and Acquisitions', 'Equity Research', 'Venture Capital']
data = [25, 20, 15, 10, 5, 3, 2, 1]
line_labels = ['Category', 'Number']

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True, projection='polar')

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

ax.legend(bbox_to_anchor=(1.15, 1.05))
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=14, rotation='vertical')
ax.set_title('Number of Professionals in Different Financial Domains', fontsize=18)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_58.png')
plt.clf()