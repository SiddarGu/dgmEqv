
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Viewership', 'Attendance', 'Subscription', 'Advertising']
line_labels = ['Category']
data = np.array([[38], [27], [15], [20]])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

ax.pie(data[:, 0], labels=data_labels, startangle=45, counterclock=False, colors=['b', 'g', 'r', 'c'])
center_circle = plt.Circle((0, 0), 0.3, color='white')
ax.add_artist(center_circle)
ax.legend(data_labels)
ax.set_title('Sports and Entertainment: Popularity and Performance - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_58.png')
plt.clf()