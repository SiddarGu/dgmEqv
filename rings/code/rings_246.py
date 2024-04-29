
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

data_labels = ['Vaccination','Disease Prevention','Treatment Quality','Disease Management','Health Promotion']
data = [17,32,17,24,10]
line_labels = ['Category','ratio']

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

colors = plt.cm.tab10(np.arange(len(data_labels)))
explode = [0] + [0.1] * 4
ax.pie(data,labels=data_labels,explode=explode,colors=colors,autopct='%1.1f%%',textprops={'fontsize':14},startangle=90,counterclock=False)

centre_circle = plt.Circle((0,0),0.6,fc='white')
ax.add_artist(centre_circle)

ax.legend(data_labels,loc='upper right',bbox_to_anchor=(1,1.03),fontsize=14)

ax.set_title('Healthcare Quality Metrics - 2023', fontsize=18)
ax.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_3.png')
plt.clf()