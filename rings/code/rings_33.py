
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Treatment Quality','Patient Care','Clinical Outcomes','Cost Management']
data = np.array([48,25,13,14])
line_labels = ['Category']

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, autopct='%1.1f%%', startangle=90, counterclock=False, colors=['coral','gold','lightblue','pink'])
circle = plt.Circle((0,0), 0.6, color='white')
ax.add_artist(circle)
ax.set_title('Healthcare Quality Evaluation - 2023')
ax.legend(data_labels,loc='lower right')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_43.png')
plt.clf()