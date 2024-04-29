
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

data_labels = ['Enrolment', 'Curriculum', 'Technology', 'Faculty', 'Facilities']
line_labels = ['Topic', 'ratio']
data = np.array([[22, 42, 19, 14, 3]])

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)

colors = cm.rainbow(np.linspace(0, 1, len(data_labels)))

ax.pie(data.flatten(), startangle=90, counterclock=False, colors=colors)

# Set ring width
centre_circle = plt.Circle((0, 0), 0.6, fc='white')
ax.add_artist(centre_circle)

ax.axis('equal')
ax.legend(data_labels)
fig.suptitle('Academic Excellence - 2023')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_122.png')
plt.clf()