
import matplotlib.pyplot as plt 
import numpy as np 

data_labels = ["Visual Arts","Music","Theatre","Literature","Film"] 
data = [31,17,20,14,18] 
line_labels = [0,1,2,3,4] 
inner_radius = 0.4

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.set_title("Arts and Culture Performance - 2023")

ax.pie(data, labels=data_labels, startangle=90, counterclock=False, radius=1.2, labeldistance=1.05, rotatelabels=True, autopct='%1.1f%%', pctdistance=0.7, wedgeprops=dict(width=inner_radius, edgecolor='w'))

ax.add_artist(plt.Circle((0,0), inner_radius, color='white', fill=True, linewidth=1.25))

ax.legend(data_labels, loc="upper left", bbox_to_anchor=(-0.1, 1))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_141.png')
plt.clf()