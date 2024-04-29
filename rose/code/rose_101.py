
import matplotlib.pyplot as plt
import numpy as np

# transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Animal Welfare', 'Environmental Preservation', 'Humanitarian Aid', 'Education', 'Health Care', 'Poverty Relief', 'Homeless Shelters', 'Senior Care', 'Cultural Preservation', 'Disaster Relief']
data = np.array([120, 80, 100, 90, 85, 70, 60, 50, 40, 30])
line_labels = ['Type of Organization', 'Number']

# plot the data with the type of rose chart
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)
sector_angle = (2 * np.pi) / len(data_labels)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'black', 'brown', 'gray']

for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, color=colors[i], label=data_labels[i])
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=12, wrap=True, rotation=90)
ax.legend(bbox_to_anchor=(1.2,1.0), fontsize=12)
ax.set_title('Number of Nonprofit Organizations Serving Different Causes', fontsize=15)

# save the chart
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_94.png')
plt.clf()