
import matplotlib.pyplot as plt
import pandas as pd

data_labels=['Diagnostics','Treatment','Research','Patient Care','Administration']
data=[33,16,23,27,1]
line_labels=['Category','ratio']

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90,counterclock=False,autopct='%1.1f%%', colors=['red','green','orange','blue','violet'])
inner_circle = plt.Circle((0,0),0.7,color='white')
ax.add_artist(inner_circle)
ax.set_title('Health Care System Efficiency - 2023')
labels = [i.get_text() for i in ax.get_xticklabels()]
ax.legend(data_labels, loc="best", bbox_to_anchor=(1,0.5))
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_35.png')
plt.clf()