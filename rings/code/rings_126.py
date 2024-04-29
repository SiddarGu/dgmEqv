
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Education Quality', 'Research Quality', 'Student Satisfaction', 'Arts & Culture', 'Social Engagement']
data = np.array([32, 18, 20, 10, 20])
line_labels = ['Category']

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

colors = ['red', 'orange', 'green', 'blue', 'purple']
ax.pie(data, labels=data_labels, colors=colors, shadow=True, startangle=90, counterclock=False, labeldistance=1.1)

circle = plt.Circle((0, 0), 0.7, facecolor='white')
ax.add_artist(circle)

ax.set_title('Humanities and Social Sciences Performance - 2023')
ax.legend(data_labels, bbox_to_anchor=(1, 0.5), loc="center left")

plt.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_78.png')
plt.clf()