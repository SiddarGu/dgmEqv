
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data_labels = ['Academic Performance','Student Engagement','Teacher Performance','School Administration']
data = [39,24,19,18]
line_labels = np.array(data_labels)

fig, ax = plt.subplots(figsize=(10,10))

ax.pie(data, startangle=90, counterclock=False, colors=['g', 'b', 'r', 'y'],autopct='%1.1f%%')

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax.axis('equal')  
ax.set_title('Education Quality Measurement - 2023')
ax.legend(line_labels, loc="best", bbox_to_anchor=(1.0, 0.5), fontsize=12, labelspacing=1, frameon=False)
ax.set_aspect('equal')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_30.png')
plt.clf()