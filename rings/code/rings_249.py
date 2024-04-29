
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

data_labels = ['Academic Performance','Student Retention','Faculty Quality','Facilities','Curriculum']
data = np.array([30,23,31,11,5])
line_labels = ['2023']

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
ax.add_artist(plt.Circle((0,0), 0.7, color='white'))
ax.set_title('Education and Academics Overview - 2023')
ax.legend(data_labels, loc='upper left')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_9.png')
plt.clf()