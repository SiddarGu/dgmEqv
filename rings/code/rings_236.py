
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["User Engagement","Online Presence","User Acquisition","Content Quality","Interaction"]
data = [33,17,21,20,9]
line_labels = ["Category"]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

ax.pie(data, labels=data_labels, autopct='%.2f%%', startangle=90, counterclock=False,colors=['#d62728','#9467bd','#8c564b','#e377c2','#7f7f7f'])
inner_circle = plt.Circle((0,0), 0.7, color='white', fc='white',linewidth=1)
ax.add_artist(inner_circle)
plt.title('Social Media and Web Performance - 2023')
ax.legend(data_labels,loc="upper right", bbox_to_anchor=(1.05,1.0))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_11.png')
plt.clf()