
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

data_labels = ['Road','Air','Water','Rail','Other']
line_labels = ['Mode','ratio']
data = [[30,15,25,20,10]]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
cmap = cm.get_cmap('Set1')

pie_wedge_collection = ax.pie(data[0],labels=data_labels, colors=cmap(np.arange(len(data_labels))),startangle=90,counterclock=False)

center_circle = plt.Circle((0,0),0.7,color='white')
ax.add_artist(center_circle)
ax.axis('equal')
ax.legend(data_labels,loc='upper left')
ax.set_title('Transportation & Logistics in 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_119.png')
plt.clf()