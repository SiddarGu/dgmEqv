
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Regulation','Taxation','Immigration','Social Programs','Defense']
data = np.array([23,29,10,25,13])
line_labels = ['Category','ratio']

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#b30000', '#e34234','#ff6666','#ff9999','#ffcccc'])
centre_circle = plt.Circle((0,0),0.60,fc='white')
ax.add_artist(centre_circle)
ax.axis('equal')
ax.legend(data_labels, loc='lower left', bbox_to_anchor=(-0.1, -0.1, 0.5, 0.5))
ax.set_title("State of Public Policy - 2023")
plt.grid(True)
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_44.png")
plt.clf()