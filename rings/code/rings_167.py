
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Artistry', 'Heritage', 'Cultural Sharing', 'Education', 'Participation']
data = [36, 17, 6, 25, 16]
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF'])

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

ax.legend(data_labels, loc="upper left")
ax.grid(True, alpha=0.3)
plt.title('Arts and Culture in the 21st Century')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_140.png')
plt.clf()