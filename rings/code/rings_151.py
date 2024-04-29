
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Taxation','Public Education','Social Security','Infrastructure','Employment']
data = [17,20,37,18,8]
line_labels= ['Category','ratio']

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

explode = np.zeros(len(data))
explode[0] = 0.1
colors = ['#c0392b', '#16a085', '#27ae60', '#2980b9', '#8e44ad']
ax.pie(data, labels=data_labels, explode=explode, autopct='%.2f%%', startangle=90, radius=1, counterclock=False, wedgeprops={'linewidth':1.5, 'edgecolor':'white'}, colors=colors)
inner_circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(inner_circle)
ax.axis('equal')
ax.set_title('Government and Public Policy Overview - 2023', fontsize=20)
ax.legend(data_labels, loc='upper left', bbox_to_anchor=(-0.1, 1))
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_116.png')
plt.clf()