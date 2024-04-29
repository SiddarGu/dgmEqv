
import matplotlib.pyplot as plt
import numpy as np

# transform data into three variables
data_labels = ["Music","Dance","Visual Arts","Theater","Literature","Film"]
data = [100,80,60,40,20,10]
line_labels = ["Category","Number"]

# create figure and plot
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# calculate sector angle
sector_angle = (2 * np.pi) / len(data_labels)

# draw sector
for i in range(len(data_labels)):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=plt.cm.Set1(i), edgecolor='k')

# set ticks and labels
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels)

# reposition legend
ax.legend(data_labels, bbox_to_anchor=(1.3,0.5))

# set title
plt.title("Popularity of Arts and Culture Disciplines in 2021")

# resize image
plt.tight_layout()

# save figure
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_13.png")

# clear current image state
plt.clf()