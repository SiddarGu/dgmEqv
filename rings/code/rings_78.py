
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Cultural Participation', 'Creative Industries', 'Arts Education', 'Heritage', 'International Exchange']
data = [34, 24, 14, 18, 10]
line_labels = ['Category', 'Ratio']

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#10A2F5', '#FAC930', '#FD6E35', '#7CBB00', '#FE4C40'])
centre_circle = plt.Circle((0,0),0.5,color='white', fc='white',linewidth=0)
ax.add_artist(centre_circle)
ax.legend(data_labels, loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)
ax.set_title('Arts and Culture Trends - 2023', fontsize=20)
ax.grid(True)
fig.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_147.png')
plt.clf()