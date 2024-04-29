
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Creativity', 'Heritage', 'Artistry', 'Education', 'Popularity']
data = np.array([20, 15, 30, 20, 15])
line_labels = ['Category']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

ax.pie(data, labels=data_labels, startangle=90, counterclock=False, 
       colors=['cadetblue', 'lightcoral', 'lightgreen', 'plum', 'sandybrown'])
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

ax.legend(data_labels, loc="upper left")

ax.set_title('Arts and Culture - A Comprehensive Overview - 2023')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_45.png')

plt.clf()