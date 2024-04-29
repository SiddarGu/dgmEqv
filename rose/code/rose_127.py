

import matplotlib.pyplot as plt
import numpy as np

data = [['Category', 'Number'], 
        ['History', 50], 
        ['Economics', 45], 
        ['Sociology', 40], 
        ['Politics', 35], 
        ['Philosophy', 30], 
        ['Anthropology', 25], 
        ['Psychology', 20], 
        ['Literature', 15], 
        ['Religion', 10], 
        ['Art', 5]]

data_labels = [row[0] for row in data[1:]] 
line_labels = [row[0] for row in data[1:]] 
data = [row[1] for row in data[1:]] 

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

fig = plt.figure()
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

ax = fig.add_subplot(111, polar=True)
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

start_angle = 0
for i in range(num_categories):
    ax.bar(start_angle, data[i], width=sector_angle, color=colors[i], label=data_labels[i])
    start_angle += sector_angle

ax.legend(bbox_to_anchor=(1.2, 0.7), loc='center left')
ax.set_title('Number of Students Majoring in Social Sciences and Humanities Fields in 2021')
ax.set_xticks(np.arange(0, 2*np.pi, sector_angle))
ax.set_xticklabels(data_labels, rotation=90, wrap=True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_134.png')
plt.clf()