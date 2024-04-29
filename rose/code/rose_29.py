
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Tax Reform', 'Environmental Policy', 'Social Welfare', 
               'Education', 'National Security', 'Infrastructure', 
               'Foreign Affairs', 'Healthcare']
data = [400, 350, 300, 250, 200, 150, 100, 50]
line_labels = ['Issue', 'Number of Participants']

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

cmap = plt.cm.jet
colors = cmap(np.arange(num_categories)*int(256/num_categories))

for i, data_val in enumerate(data):
    ax.bar(sector_angle*i, data_val, width=sector_angle, color=colors[i], label=data_labels[i])

angles = np.linspace(0, 2*np.pi, num_categories, endpoint=False)
ax.set_thetagrids(angles * 180/np.pi, data_labels, fontsize=10)
ax.set_xticks(angles)
ax.set_title(line_labels[0], y=1.08, fontsize=14)
ax.legend(bbox_to_anchor=(1.2, 0.8))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_111.png')
plt.clf()