
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Fast Food', 'Beverages', 'Bakery', 'Dairy Products', 'Organic Products', 'Frozen Food', 'Seafood']
line_labels = ['Number']
data = [50, 40, 30, 20, 10, 5, 8]
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, polar=True)

for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Dark2(i))

ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, rotation=90)
ax.set_title('Prevalence of Food and Beverage Categories in 2021')
ax.grid(alpha=0.3)
ax.legend(bbox_to_anchor=(1.1,1.1))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-054203_2.png')
plt.clf()