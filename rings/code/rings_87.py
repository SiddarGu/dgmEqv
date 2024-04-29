
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Performance', 'Student Engagement', 'Curriculum Quality', 'Resources Availability', 'Teacher Quality']
data = np.array([30,20,25,15,10])
line_labels = ['Category', 'Ratio']

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, autopct='%1.1f%%', colors=['#19A979','#2E86C1','#F4C724','#D980FA','#C0392B'])
circle = plt.Circle((0,0),0.7, color='white')
ax.add_artist(circle)
ax.set_title('Academic Excellence - 2023')
ax.legend(data_labels, loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, fontsize=9, frameon=False)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_26.png')
plt.clf()