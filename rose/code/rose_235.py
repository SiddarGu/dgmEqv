
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Criminal Law','Civil Rights','Corporate Law','Family Law','Labor Law','Intellectual Property','Environmental Law','Tax Law','International Law']
data = [300,250,200,150,100,80,60,40,20]
line_labels = ['Number of Cases']

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1, projection='polar')

num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i))
    
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', labels=data_labels)

ax.set_xticks(sector_angle * np.arange(num_categories))
ax.set_xticklabels(data_labels, fontsize=8, ha='center')

ax.set_title('Number of Legal Cases Across Different Categories in 2023', fontsize=11)
ax.set_rlabel_position(45)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_74.png')
plt.clf()