
import matplotlib.pyplot as plt 
import numpy as np

data_labels = ['Clothing', 'Electronics', 'Groceries', 'Furniture', 'Home Appliances', 'Automotive', 'Sporting Goods', 'Toys', 'Books', 'Jewelry']
data = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
line_labels = ['Category', 'Number']

colors = ['#EE2C2C', '#FBB117', '#FFF222', '#00A08A', '#30C39E', '#89C4F4', '#3D2B1F', '#B08495', '#6B6882', '#6E90BE']

sector_angle = (2 * np.pi) / len(data_labels)

fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection='polar')

for i in range(len(data_labels)):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=colors[i], label=data_labels[i])

ax.set_xticks(np.arange(0, (2 * np.pi), sector_angle))
ax.set_xticklabels(data_labels, fontsize=13, color='black', rotation=90)
ax.set_title('Popularity of Retail and E-commerce Products in 2021', fontsize=20)
ax.legend(bbox_to_anchor=(0.95, 0.6))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_35.png', format='png')
plt.clf()