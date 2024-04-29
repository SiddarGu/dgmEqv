
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Renewable Energy','Fossil Fuels','Nuclear Power','Hydroelectricity']
data = np.array([39,21,7,33])
line_labels = ['Category', 'Ratio']

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

ax.pie(data, explode=(0,0,0,0), labels=data_labels, startangle=45, counterclock=False, colors=['#FF0000','#00FF00','#0000FF','#FFFF00'])
plt.Circle((0,0), 0.7, color='white')
ax.add_artist(plt.Circle((0,0), 0.7, color='white'))

ax.legend(data_labels, loc="best")
ax.set_title("Energy Utilization in 2023", fontsize=20)

plt.tight_layout()

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_16.png')
plt.clf()