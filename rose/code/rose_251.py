
import matplotlib.pyplot as plt
import numpy as np

# transform data into three variables
data_labels = ["Education", "Social Services", "Public Safety", "Housing and Urban Development", "Transportation", "Energy and Environment", "Economics and Business", "Health and Human Services"]
data = [60, 43, 97, 17, 36, 96, 60, 68]
line_labels = ["Area", "Number"]

# plot the data
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

# create sectors corresponding to different categories
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.get_cmap('tab10')(i)) 

# set up ticks
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10)

# set the title of the figure
ax.set_title("Government and Public Policy Statistics in 2021")

# add legend
ax.legend(data_labels, bbox_to_anchor=(1, 0.6), fontsize=10)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_18.png')

# Clear the current image state
plt.cla()