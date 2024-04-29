

import matplotlib.pyplot as plt
import numpy as np

#transform data into three variables
data_labels = ["Sports","Music","Film & Television","Books & Literature","Video Games","Theatre & Arts","Magazines & Newspapers","Radio"]
data = [100,60,80,50,40,20,10,5]
line_labels = ["Category","Number"]

#plot the data
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='polar')

# set the color of each sector
colors = ['coral','gold','skyblue','plum','seagreen','darkorange','crimson','cornflowerblue']

# calculate the sector angle
sector_angle = (2 * np.pi) / len(data_labels)

# draw sectors corresponding to different categories
for i in range(len(data_labels)):
    ax.bar(i*sector_angle, data[i], width=sector_angle, bottom=0.0, color=colors[i], label=data_labels[i])

# set the number of ticks
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))

# set the category labels
ax.set_xticklabels(data_labels)

# rotate the category labels
for tick in ax.get_xticklabels():
    tick.set_rotation(90)

# add the legend
ax.legend(data_labels, bbox_to_anchor=(1.1, 0.5))

# set the title
ax.set_title("Popularity of Media Platforms in the Entertainment Industry in 2021")

# prevent overlapping
plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_95.png')

# clear current image
plt.clf()