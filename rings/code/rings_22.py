

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

data_labels = ['Student Performance', 'Teacher Effectiveness', 'Curriculum Quality', 'Facility Quality', 'Administrative Efficiency']
data = [30, 30, 15, 10, 15]
line_labels = ['Aspect', 'Ratio']

fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(data, startangle=90, counterclock=False,
       labels=data_labels, autopct='%.1f%%',
       colors=cm.rainbow(np.linspace(0, 1, len(data))))

centre_circle = plt.Circle((0, 0), 0.7, color='black', fc='white', linewidth=0)
ax.add_artist(centre_circle)

ax.set_title('Academic Performance Analysis - 2023')
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(0.9, 0.9))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_33.png')
plt.clf()