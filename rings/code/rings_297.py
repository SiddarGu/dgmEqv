
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Court Cases','Litigation','Compliance','Regulatory Affairs','Legal Advice']
data = [27,9,15,19,30]
line_labels = ['Category', 'Ratio']

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, autopct='%.2f%%')
circle = plt.Circle(xy=(0,0), radius=0.5, fc='white', ec='black', lw=2)
ax.add_artist(circle)
ax.legend(data_labels, loc='upper center')
plt.title("Legal Affairs Overview - 2023")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_31.png')
plt.clf()