
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Social Media Platforms', 'Digital Advertising', 'E-commerce', 'Web Design', 'Online Security', 'Mobile Applications', 'Cloud Computing', 'Search Engine Optimization']
data = [60, 80, 90, 50, 40, 70, 75, 65]
line_labels = ['Category', 'Number']

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i/num_categories))

ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

ax.legend(bbox_to_anchor=(1, 0.5), loc='center left')
ax.set_title('Popularity of Web Technologies in 2021')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_72.png')
plt.clf()