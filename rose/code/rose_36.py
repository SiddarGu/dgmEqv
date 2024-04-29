
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Corn', 'Wheat', 'Soybeans', 'Rice', 'Potatoes', 'Tomatoes', 'Apples', 'Bananas', 'Strawberries', 'Carrots']
data = [10, 20, 15, 25, 5, 17, 9, 11, 13, 7]
line_labels = ['Quantity']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

colors = ['yellow', 'orange', 'green', 'blue', 'indigo', 'violet', 'red', 'pink', 'brown', 'grey']

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=colors[i])

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=8, wrap=True, rotation=45)
legend = ax.legend(bbox_to_anchor=(1.1, 1.1), loc='upper left', fontsize='large')

ax.set_title('Food Production Quantities of Selected Crops in 2021')

plt.tight_layout()

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_124.png')

plt.clf()