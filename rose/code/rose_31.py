
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Beach","Mountains","Forest","City","Desert","Island","Cruise","Historical Sites"]
data = [545,755,400,900,100,200,150,500]
line_labels = ["Destination","Number of Tourists"]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='polar')

colors = ['#f44336', '#e91e63', '#9c27b0', '#673ab7', '#3f51b5', '#2196f3', '#03a9f4', '#00bcd4']
sector_angle = (2 * np.pi) / len(data_labels)

for i in range(len(data)):
    ax.bar(sector_angle*i, data[i], width=sector_angle, bottom=0.0, color=colors[i], label=data_labels[i])

ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, fontsize=15, ha='center', va='bottom')
ax.set_title('Popularity of Different Tourist Destinations in 2021', fontsize=20)

ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.05), fontsize=15)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_114.png')
plt.clf()