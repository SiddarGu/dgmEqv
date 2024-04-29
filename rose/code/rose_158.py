
import matplotlib.pyplot as plt
import numpy as np

# Transform data into variables
data_labels = ['Economics', 'Sociology', 'Political Science', 'Anthropology', 'History', 'Geography', 'Philosophy', 'Psychology', 'Religion', 'Language Studies']
data = [120, 80, 90, 50, 110, 70, 40, 60, 20, 30]
line_labels = ['Field', 'Number']

# Plot rose chart
fig = plt.figure(figsize = (8, 8))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

colors = ['#003399', '#009933', '#339999', '#cc0033', '#ffff00', '#990000', '#00cccc', '#cccc00', '#330099', '#9900cc']

for i, category in enumerate(data_labels):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=colors[i], label=category)

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, rotation = 0)
ax.legend(bbox_to_anchor = (1.2, 0.5))
ax.set_title('Number of Academic Programs in Social Sciences and Humanities')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_49.png')

plt.clf()