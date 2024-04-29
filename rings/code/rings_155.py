
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Court Cases','Legal Advice','Police Enforcement','Public Policies']
line_labels = ['Category','ratio']
data = [[34, 14, 7, 45]]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(data[0], labels=data_labels,
       startangle=90, counterclock=False,
       colors=['darkorange', 'lightblue', 'grey', 'lightgreen'])
centre_circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(centre_circle)
ax.axis('equal')
ax.set_title("Law and Legal Affairs Impact - 2023")
ax.legend(data_labels, bbox_to_anchor=(1.1, 0.8))
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_12.png")
plt.clf()