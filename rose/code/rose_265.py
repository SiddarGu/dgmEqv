
import matplotlib.pyplot as plt
import numpy as np

data_labels=['Hotels', 'Restaurants', 'Tourism Agencies', 'Travel Companies', 'Airlines', 'Cruises']
line_labels=['Category', 'Number']
data=np.array([[800, 600, 400, 200, 100, 50]])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i, category in enumerate(data_labels):
    ax.bar(i * sector_angle, data[0][i], width=sector_angle, color=plt.cm.Set1(i/num_categories), label=category)

ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.0)
ax.set_title("Number of Businesses in the Tourism and Hospitality Industry in 2021")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_48.png")
plt.clf()