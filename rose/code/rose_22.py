
import matplotlib.pyplot as plt
import numpy as np

# transform the given data into three variables
data_labels = ["Visual Arts", "Music", "Theater", "Literature", "Dance", "Film", "Media Arts", "Architecture", "Photography", "Comics"]
data = [890, 850, 500, 400, 360, 320, 290, 220, 190, 100]
line_labels = ["Art Form", "Number of Subscribers"]

# plot the data with the type of rose chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))

# calculate the sector angle
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

# draw sectors corresponding to different categories
for i, d in enumerate(data):
    ax.bar(i * sector_angle, d, width=sector_angle, label=data_labels[i], color=plt.cm.jet_r(i/num_categories))

# set xticks
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))

# set xticklabels
ax.set_xticklabels(data_labels, fontdict={'fontsize': 14}, wrap=True, rotation=90)

# reposition the legend so that it does not cover any part of the chart
ax.legend(data_labels, bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=14)

# set the title of the figure
ax.set_title('Popularity of Arts and Culture Forms in 2021', fontdict={'fontsize': 20})

# set gridlines
ax.grid(True, color='grey', linestyle='--', alpha=0.3)

# automatically resize the image by tight_layout
plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_10.png')

# clear the current image state
plt.clf()