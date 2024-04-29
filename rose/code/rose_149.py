
import matplotlib.pyplot as plt
import numpy as np

# transform the given data into three variables
data_labels = ["Single-Family Home","Multi-Family Home","Condominium","Mixed-Used Property","Vacant Land"]
data = [150,100,50,20,10]
line_labels = ["Property Type","Number"]

# plot the data with the type of rose chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

# assign a different color to each sector
colors = ["r", "g", "b", "y", "m"]
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=colors[i], edgecolor='black', linewidth=1)

# add legend
ax.legend(data_labels, bbox_to_anchor=(1.1, 1.05), fontsize=10)

# set the category labels
angles = np.linspace(0,2*np.pi,num_categories,endpoint=False)
ax.set_xticks(angles)
ax.set_xticklabels(data_labels, fontsize=10)

# title
ax.set_title("Number of Housing Properties in the Real Estate Market")

# adjust the tick labels
tick_labels = ax.get_xticklabels()
for i in range(len(tick_labels)):
    tick_labels[i].set_horizontalalignment('center')

# adjust the margins
plt.tight_layout()

# save figure
fig.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_31.png")

# clear the current image state
plt.clf()