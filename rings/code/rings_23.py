
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Music and Dance', 'Theatre and Drama', 'Art and Design', 'Literature', 'Performing Arts']
data = [20, 25, 15, 20, 20]
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['red', 'green', 'blue', 'orange', 'purple'])
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)
ax.legend(data_labels)
plt.title('Arts and Culture Appreciation - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_34.png')
plt.clf()