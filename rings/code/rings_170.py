
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Adoption","Usage","Security","Impact","Coverage"]
data = np.array([33,18,16,17,16])
line_labels = ["Category"]

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90,counterclock=False,labels=data_labels,colors=['#FF0000','#FFFF00','#00FF00','#00FFFF','#0000FF'])
ax.add_artist(plt.Circle((0, 0), 0.7, color='white'))
ax.set_title("Technology and Internet Trends -2023")
ax.legend(data_labels, loc="lower right")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_144.png")
plt.clf()