
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Prevention', 'Diagnosis', 'Treatment', 'Recovery']
data = [59, 18, 22, 1]
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, autopct='%1.1f%%', startangle=90, counterclock=False)
centre_circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(centre_circle)

plt.title('Healthcare System Overview - 2023')
ax.legend(data_labels, loc='best', bbox_to_anchor=(1, 0.5))
ax.axis('equal')
ax.grid(True)
fig.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_18.png')
plt.clf()