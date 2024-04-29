
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Cultural Context','Human Interaction','Social Development','Philosophy','Language']
line_labels = ['Topic']
data = np.array([[25,15,30,15,15]])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(data.flatten(), labels=data_labels, autopct='%1.1f%%', startangle=90, counterclock=False)
circle = plt.Circle(xy=(0, 0), radius=0.7, facecolor='white')
ax.add_artist(circle)
ax.set_title('Analyzing Social Sciences and Humanities - 2023')
ax.legend(data_labels,bbox_to_anchor=(1, 0.5), loc="center right", fontsize=10)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_31.png')
plt.clf()