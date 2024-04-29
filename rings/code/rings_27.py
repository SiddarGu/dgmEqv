
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.patches import Circle

data_labels = ['Social Sciences', 'Humanities']
data = np.array([44, 56])
line_labels = ['Topic', 'ratio']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.set_title('Social Sciences and Humanities Ratio - 2023')

pie_wedge_collection = ax.pie(data,startangle=90,counterclock=False,labels=data_labels,autopct='%1.1f%%')
for pie_wedge in pie_wedge_collection[0]:
    pie_wedge.set_edgecolor('white')

c = Circle(xy=(0,0), radius=0.7, edgecolor='white',facecolor='white')
ax.add_artist(c)

ax.legend(data_labels, loc="best")
ax.axis('equal')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_38.png')
plt.clf()