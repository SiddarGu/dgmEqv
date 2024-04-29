
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Wind Energy','Solar Energy','Hydroelectricity','Natural Gas','Nuclear Power','Coal','Petroleum','Biomass']
line_labels = ['Value']
data = np.array([[90],[80],[60],[50],[40],[30],[20],[10]])

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(111, projection='polar')

for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i))

ax.legend(data_labels, bbox_to_anchor=(1.2,1), fontsize=20)

ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=20, rotation=90)

ax.set_title('Energy Sources and Their Availability in 2021', fontsize=30)

plt.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_21.png')
plt.clf()