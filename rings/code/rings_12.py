
import matplotlib.pyplot as plt
import numpy as np
data_labels = ['Network Security', 'Data Storage', 'Cloud Computing', 'Artificial Intelligence', 'Internet of Things']
data = np.array([15, 25, 10, 30, 20])
line_labels = ['Category', 'Ratio']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, autopct='%1.1f%%', startangle=90, counterclock=False, colors=['#e0e0e0', '#c9e5ef', '#b9d9f2', '#aacdf5', '#9ac2f8'])

white_circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(white_circle)
ax.set_title('Technological Innovation in the Digital Age - 2023')
ax.legend(data_labels, loc='best', bbox_to_anchor=(1, 0., 0.5, 0.5))
plt.grid()
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_19.png')
plt.clf()