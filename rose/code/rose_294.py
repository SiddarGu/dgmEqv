
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Road', 'Rail', 'Air', 'Sea', 'Pipeline', 'Courier']
line_labels = ['Mode of Transportation', 'Number of Users']
data = [[54, 32, 76, 43, 15, 21]]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

for i in range(num_categories):
    ax.bar(sector_angle * i, data[0][i], width=sector_angle, 
           color=colors[i], edgecolor='black', label=data_labels[i])

ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, wrap=True, rotation=45)
ax.legend(bbox_to_anchor=(1.2,1), loc="upper right")

ax.set_title('Usage of Different Transportation Modes in 2020')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-082906_3.png')
plt.clf()