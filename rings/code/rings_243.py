
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_labels = ['Creativity','Artistic Expression','Cultural Engagement','Historical Preservation','Appreciation']
data = [15, 20, 25, 20, 20]
line_labels = ['Element','ratio']

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()

ax.pie(data, labels=data_labels,autopct='%1.1f%%', startangle=90, counterclock=False, colors=['#FFC0CB','#F08080','#CD5C5C','#FFA07A','#DC143C'])
centre_circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(centre_circle)

ax.set_title('Analysis of Arts and Culture Participation - 2023', fontsize=20)
ax.set_aspect('equal')
ax.legend(data_labels, loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

plt.grid(True)
plt.tight_layout()

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_22.png', bbox_inches='tight')
plt.clf()