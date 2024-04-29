
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data_labels = ['Knowledge Acquisition','Critical Thinking','Research Skills','Problem Solving','Communication']
data = [[25,15,35,12,13]]
line_labels = ['Area']

fig, ax = plt.subplots(figsize=(10,10))
ax.set_title('Academic Excellence in Education - 2023')
ax.pie(data[0], labels=data_labels, startangle=45,counterclock=False, wedgeprops={'edgecolor': 'k'})
center_circle = plt.Circle((0,0), 0.7, color='white', ec='k', lw=2)
ax.add_artist(center_circle)
ax.legend(data_labels, loc="upper right", bbox_to_anchor=(1, 0., 0.5, 0.5), fontsize=12, 
           bbox_transform=ax.transAxes, borderaxespad=0., frameon=False)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_13.png')
plt.clf()