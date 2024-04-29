
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Research and Development', 'Production', 'Quality Control', 'Safety', 'Environmental Protection']
line_labels = ['Category', 'ratio']

data = np.array([
    [32, 14, 15, 6, 33],
])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()

ax.pie(data.flatten(), labels=data_labels, startangle=90, counterclock=False, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffb3e6'])

plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(plt.Circle((0, 0), 0.7, color='white'))

plt.title('Science and Engineering Progress Report - 2023', fontsize=14)
ax.legend(data_labels)

plt.tight_layout() 
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_48.png')
plt.clf()