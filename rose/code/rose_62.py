
import matplotlib.pyplot as plt 
import numpy as np 

data_labels = ['Sightseeing', 'Shopping', 'Eating Out', 'Outdoor Adventure', 'Cultural Events', 'Nightlife', 'Relaxation']
line_labels = ['Activity', 'Number of Visitors']
data = np.array([[200, 160, 120, 80, 60, 40, 20]])

fig = plt.figure(figsize=(20, 10)) 
ax = fig.add_subplot(111, projection='polar') 

ax.set_title('Number of Visitors to Tourist Destinations in 2021')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

colors = ['#4e73df', '#1cc88a', '#36b9cc', '#f6c23e', '#e74a3b', '#858796', '#ffc107']

for i in range(num_categories):
    ax.bar(i * sector_angle, data[0][i], width=sector_angle, label=data_labels[i], color=colors[i], bottom=0)

ax.legend(data_labels, bbox_to_anchor=(1.2, 0.8))

ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=14, rotation=90)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_24.png', bbox_inches='tight')
plt.clf()