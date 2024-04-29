
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Preschool","Primary School","Secondary School","Higher Education","Postgraduate"] 
data = [25,50,45,80,30] 
line_labels = ["Level of Education", "Number"] 

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
sector_angle = (2 * np.pi) / len(data)

for i in range(len(data)):
    ax.bar(i*sector_angle, data[i], width=sector_angle, color=plt.cm.Set1(i/len(data)), label=data_labels[i])

ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=14)
ax.set_title('Number of Learners Enrolled in Different Levels of Education', fontsize=18)
ax.legend(bbox_to_anchor=(1.2, 0.5))
plt.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_18.png')
plt.clf()