
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Single Family Homes', 'Multi-Family Apartments', 'Townhouses', 'Condominiums', 'Co-ops', 'Mobile Homes']
data = [400, 350, 300, 250, 200, 150]
line_labels = ['Property Type', 'Number of Units']

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

colors = ['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#ffffcc']

for i in range(num_categories):
    ax.bar(i*sector_angle, data[i], width=sector_angle, facecolor=colors[i], edgecolor='black', label=data_labels[i])

ax.set_thetagrids(np.arange(0,360,360/num_categories), labels=data_labels, fontsize=10)
ax.tick_params(labelsize=10)
ax.set_title('Count of Real Estate Properties in 2021', fontsize=20)

ax.legend(bbox_to_anchor=(1, 1), ncol=1, fontsize=15)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_27.png')
plt.clf()