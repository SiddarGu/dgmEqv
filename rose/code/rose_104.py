
import matplotlib.pyplot as plt
import numpy as np

#transform data
data_labels = ['Primary School', 'Middle School', 'High School', 'College', 'Graduate School', 'Postgraduate School', 'Professional School', 'Doctoral School']
data = [250, 200, 150, 100, 80, 60, 40, 20]
line_labels = ['Educational Level', 'Number of Students']

#plot the data
fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, projection='polar')

#calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

#draw sectors corresponding to different categories
for i in range(0, num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=plt.cm.tab10(i), label=data_labels[i])

#add a legend
ax.legend(data_labels, bbox_to_anchor=(1.2, 0.5))
ax.set_xticks(np.arange(0,2*np.pi,sector_angle))
ax.set_xticklabels(data_labels, rotation=35)
ax.set_title("Number of Students Across Different Educational Levels in 2021", fontsize=20)
plt.grid(linestyle='--')
plt.tight_layout()

#save the image
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_99.png')

#clear the current image state
plt.clf()