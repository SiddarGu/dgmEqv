
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Music', 'Visual Arts', 'Dance', 'Theatre', 'Literature']
data = np.array([17, 26, 13, 22, 22])
line_labels = ['Category', 'Ratio']

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, colors=['b', 'g', 'r', 'c', 'm'])
circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)
ax.legend(data_labels, loc='lower left', bbox_to_anchor=(0.6, 0.05, 0.5, 0.5))
plt.title('Arts and Culture - 2023')
plt.tight_layout()
plt.savefig(r'/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_35.png')
plt.clf()