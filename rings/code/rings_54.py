
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Taxation','Legislation','International Relations','Public Services','Education']
data = np.array([25,5,20,30,20])
line_labels = ['Category','ratio']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#90EE90', '#FFA500', '#FFFF00','#00FF00','#0000FF'])
circle = plt.Circle((0,0), 0.60, color='white')
ax.add_artist(circle)
ax.legend(data_labels, loc='lower right')
ax.set_title('Government and Public Policy Overview - 2023')
ax.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_117.png')
plt.clf()