
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

data_labels=['Academic Achievement', 'Student Engagement', 'Teacher Performance', 'School Facilities', 'Extracurriculars']
data=[25, 20, 35, 10, 10]
line_labels=['Category', 'ratio']

fig=plt.figure(figsize=(7,7))
ax=fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False,colors=['#f09df8','#33f0ab','#f0ef33','#ef33f0','#3fef33'])
ax.axis('equal')
centre_circle = Circle((0,0), 0.7, color='white', fc='white',linewidth=0)
ax.add_artist(centre_circle)
ax.legend(data_labels, loc='upper left', bbox_to_anchor=(-0.1, 1))
ax.grid()
plt.title('Education Quality Evaluation - 2023')
plt.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_5.png')
plt.clf()