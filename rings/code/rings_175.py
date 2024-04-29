
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Electricity Production', 'Renewable Energy', 'Oil Production', 'Gas Production']
line_labels = ['Category', 'Ratio']
data = np.array([[38, 20, 25, 17]]).T

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
ax.pie(data[:,0], labels=data_labels, colors=colors, startangle=90, counterclock=False)
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)
ax.legend(data_labels, loc='upper right')

plt.title('Energy and Utilities Performance - 2023', fontsize=14)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_19.png')
plt.clf()