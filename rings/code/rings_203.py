
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Network Security', 'Data Analysis', 'Cloud Computing', 'Artificial Intelligence', 'User Experience']
line_labels = ['Category', 'ratio']
data = np.array([[13, 25, 17, 27, 18]])

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title('Technology and the Internet - 2023')

ax.pie(data[0], labels=data_labels, startangle=90, counterclock=False,autopct='%.1f%%')
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax.legend(data_labels, loc="best")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_56.png')
plt.clf()