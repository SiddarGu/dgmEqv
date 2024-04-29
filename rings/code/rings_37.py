
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Student Success', 'Classroom Resources', 'Teacher Support', 'Student Engagement', 'Administrative Efficiency']
data = [31, 26, 20, 19, 4]
line_labels = ['Area', 'ratio']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)
ax.pie(data, labels=data_labels, autopct='%1.1f%%', startangle=90, counterclock=False)

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax.legend(data_labels, loc='upper left')
ax.set_title('Education Quality Evaluation - 2023')
plt.tight_layout()

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_47.png')
plt.clf()