
import matplotlib.pyplot as plt
import numpy as np

# transform the given data into three variables
data_labels = ['Live Sports', 'Movies', 'Video Games', 'Music', 'Social Media', 'Television', 'Theatrical Performances', 'Books']
data = [130, 90, 80, 70, 50, 45, 30, 20]
line_labels = ['Category', 'Number']

# plot the data with the type of rose chart
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# create figure before plotting
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

# adjust the axes
ax.set_theta_direction(-1)
ax.set_theta_zero_location("N")

# plot the data
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

# add legend
ax.legend(bbox_to_anchor=(1.1, 0.8), labels=data_labels)

# set xticks
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
# set xticklabels
ax.set_xticklabels(data_labels, fontsize=10, fontdict={'fontweight':'bold'}, rotation=45, ha='right')

# add background gridlines
ax.grid(color='lightgray', linestyle='-', linewidth=1, alpha=0.5)

# add title
ax.set_title("Popularity of Entertainment and Sports Categories in 2021", fontsize=15, fontdict={'fontweight':'bold'})

# resize
fig.tight_layout()

# save the image
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_126.png')

# clear the current image state
plt.clf()