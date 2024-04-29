
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Prevention', 'Diagnosis', 'Treatment', 'Rehabilitation']
line_labels = ['Category', 'ratio']
data = np.array([[37,7,30,26]])

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)

colors = ['#FFA07A','#FFD700','#ADD8E6','#90EE90']

ax.pie(data[0], labels=data_labels, colors=colors, startangle=90, counterclock=False)
circle = plt.Circle((0,0), 0.75, color='white')
ax.add_artist(circle)

ax.set_title('Healthcare Strategies - 2023')
ax.legend(data_labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_27.png')
plt.clf()