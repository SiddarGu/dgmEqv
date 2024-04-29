
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data_labels=["Visual Arts","Music","Theatre","Literature","Dance"]
data=[15,10,25,20,30]
line_labels=["Category","ratio"]

plt.figure(figsize=(10,8))
ax = plt.subplot()
ax.axis('equal')

ax.pie(data, startangle=90,counterclock=False, labels=data_labels, autopct='%1.1f%%')

centre_circle = plt.Circle((0,0),0.7,color='white', fc='white',linewidth=0)
ax.add_artist(centre_circle)

ax.set_title("Cultural Participation - 2023", fontdict={'fontsize':20})

ax.legend(data_labels, bbox_to_anchor=(1.1, 0), loc="lower right", bbox_transform=ax.transAxes)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_13.png')
plt.clf()