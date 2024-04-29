
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Renewable Sources', 'Oil and Gas', 'Hydropower', 'Nuclear', 'Coal']
data = [27, 19, 22, 26, 6]
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(14,14))
ax = fig.add_subplot()
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#ff7f0e','#2ca02c','#d62728','#9467bd','#1f77b4'])
circ = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circ)
ax.legend(data_labels, loc='upper right', fontsize=15)
ax.set_title('Energy Sources in the Energy and Utilities Sector - 2023', fontsize=20, wrap=True)
ax.axis('equal')

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_13.png', bbox_inches='tight')
plt.clf()