
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Education','Cultural Understanding','Social Interaction','Economics','Politics']
data = [25,7,21,19,28]
line_labels = ['Category','Ratio']

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1,1,1)
cmap = plt.get_cmap('tab20')
colors = cmap(np.arange(len(data_labels)))
ax.pie(data, labels=data_labels, colors=colors, startangle=90,counterclock=False)
inner_circle = plt.Circle((0,0),0.70,fc='white')
ax.add_artist(inner_circle)
ax.set_title("Social Sciences and Humanities Overview - 2023", fontsize=18)
ax.legend(data_labels, title=line_labels[1], loc="upper right")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_2.png')
plt.clf()