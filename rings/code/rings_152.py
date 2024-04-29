
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Social Studies', 'Humanities', 'Arts', 'Language', 'Literature']
data = np.array([25, 35, 15, 17, 8])
line_labels = ['Subject', 'ratio']

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.pie(data, startangle=90, counterclock=False, colors=['red', 'green', 'blue', 'yellow', 'orange'])

ax.add_artist(plt.Circle((0,0), 0.7, color='white'))

ax.legend(data_labels, loc='best')
ax.set_title('Social Sciences and Humanities Analysis - 2021')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_117.png')
plt.clf()