
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Social Responsibility', 'Economic Stability', 'Political Engagement', 'Public Safety', 'Social Services']
line_labels = ['Category','ratio']
data = np.array([[10,20,30,25,15]])

fig, ax = plt.subplots(figsize=(10,6))
ax.pie(data.flatten(), labels=data_labels, startangle=90, counterclock=False)
circle = plt.Circle((0,0), 0.75, color="white")
ax.add_artist(circle)
ax.set_title('Government and Public Policy Impact - 2023')
ax.legend(data_labels, loc="best")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_82.png')
plt.clf()