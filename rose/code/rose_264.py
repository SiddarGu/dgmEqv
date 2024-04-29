
import matplotlib.pyplot as plt
import numpy as np

# transform data
data_labels = ['Visual Arts', 'Theatre', 'Music', 'Dance', 'Cinema', 'Architecture', 'Literature', 'Folk Arts', 'Literary Arts']
data = [100, 90, 80, 70, 50, 40, 30, 20, 10]
line_labels = ['Arts Category', 'Number of Events']

# create figure
fig = plt.figure(figsize=(10, 10))
plt.title('Cultural Events in 2021 by Art Form')
ax = fig.add_subplot(111, polar=True)

# draw the rose chart
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i))

ax.legend(bbox_to_anchor=(1.0, 1.0))

# position the labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, wrap=True)

# show the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_47.png')
plt.clf()