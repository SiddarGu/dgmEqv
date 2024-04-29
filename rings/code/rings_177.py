
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Research','Development','Innovation','Manufacturing','Testing']
data = [20,30,20,15,15]
line_labels = ['Area','ratio']

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, wedgeprops={'width': 1}, radius=1, startangle=90, counterclock=False, colors=['b','g','r','c','m'])
inner_circle = plt.Circle((0,0), 0.5, color='white')
ax.add_artist(inner_circle)
ax.set_title('Science and Engineering Performance - 2023')
ax.legend(data_labels, loc='lower left', bbox_to_anchor=(-0.3, -0.1))
ax.grid(which='major', linestyle='-', linewidth='0.5', color='gray')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_20.png')
plt.clf()