
import matplotlib.pyplot as plt
import numpy as np

# transform the data
data_labels = ['Adventure Tourists','Business Tourists','Educational Tourists','Family Tourists','Religious Tourists','Tour Group Tourists','Cultural Tourists']
data = [80,40,60,90,20,50,30]
line_labels = ['Type of Tourist','Number']

# create the figure
fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, projection='polar')

# calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# plot the data
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.bwr(i/num_categories))

# add legend, set label and title
ax.legend(bbox_to_anchor=(1,1), labels=data_labels)
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, ha='center')
ax.set_title('Number of Tourists by Type in 2021')

# resize the plot and save it
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_70.png')

# clear current image state
plt.clf()