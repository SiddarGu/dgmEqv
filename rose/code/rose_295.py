
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Renewable Energy','Biodiesel','Carbon Offsetting','Eco-friendly Products','Organic Farming','Eco-tourism','Greenhouse Gas Reduction']
data = [53,24,19,76,47,93,62]
line_labels = ['Environment and Sustainability']

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, polar=True)

ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

ax.set_title('Number of Practices for Environmental Sustainability in 2021', fontsize=15)

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=(i / num_categories, (num_categories - i) / num_categories, 0.5))

ax.set_xticks(np.linspace(sector_angle/2, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10, wrap=True, rotation=45)

ax.legend(bbox_to_anchor=(1.08, 0.9), fontsize=10)

ax.grid(alpha=0.5)
plt.tight_layout()
plt.savefig(r'/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-082906_4.png')

plt.clf()