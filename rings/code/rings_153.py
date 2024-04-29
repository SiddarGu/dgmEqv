
import matplotlib.pyplot as plt
import numpy as np

data_labels=['Litigation','Compliance','Contract Management','Regulatory Operations','Professional Services']
data=[29,15,11,24,21]
line_labels=['Category','ratio']

fig, ax = plt.subplots(figsize=(10,10))

wedges, texts, autotexts= ax.pie(data, startangle=90, counterclock=False,labels=data_labels,autopct='%1.1f%%')

ax.axis('equal')
ax.set_title('Legal Affairs Overview - 2023')

centre_circle = plt.Circle((0,0),0.50,fc='white')
ax.add_artist(centre_circle)

ax.legend(data_labels, loc="upper left", bbox_to_anchor=(1,0.5))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_118.png')
plt.clf()