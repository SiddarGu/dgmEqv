
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Solar', 'Wind', 'Hydroelectric', 'Natural Gas', 'Coal', 'Nuclear']
data = [25, 30, 15, 20, 10, 10]
line_labels = ['Energy Source', 'Percentage']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, projection='polar')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories
angles = np.arange(0, (2 * np.pi), sector_angle)
ax.set_thetagrids(angles * 180/np.pi, data_labels)
ax.set_title('Percentage of Energy Sources Used in 2021')
colors = ['blue', 'green', 'yellow', 'orange', 'red', 'pink']
for i in range(num_categories):
    ax.bar(angles[i], data[i], width=sector_angle, color=colors[i], label=data_labels[i])
ax.legend(bbox_to_anchor=(1.2, 1))
fig.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_40.png')
plt.clf()