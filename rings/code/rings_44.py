
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Robotics','Artificial Intelligence','Cybersecurity','Data Science','Nanotechnology']
data = [12, 27, 19, 27, 15]
line_labels = ['Domain','ratio']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
explode = [0.1, 0, 0, 0, 0]

ax.pie(data, labels=data_labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors, explode=explode, counterclock=False)
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)
ax.set_title('Science and Engineering Advancement - 2023')
ax.legend(data_labels, fontsize='small', loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_10.png')
plt.clf()