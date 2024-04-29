

import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Economics','Sociology','Psychology','History','Anthropology','Geography','Political Science','Philosophy','Religion']
data = [120,90,110,80,100,95,60,50,30]
line_labels = ['Number of Students']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i, data_point in enumerate(data): 
    ax.bar(i * sector_angle, data_point, width=sector_angle, label=data_labels[i], color=plt.cm.Set3(i)) 

ax.legend(bbox_to_anchor=(1.05, 1.05))
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10,rotation=45, ha='right', wrap=True)
ax.set_title("Number of Students Enrolled in Social Science and Humanities Courses in 2021")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_72.png')
plt.clf()