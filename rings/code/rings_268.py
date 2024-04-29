
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Capital Expenditure','Tax Expenditure','Financial Assets','Operational Expenditure','Profit']
line_labels = ['Category','ratio']
data = np.array([[45,7,18,25,5]])

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)
ax.pie(data.flatten(), labels=data_labels, startangle=90, counterclock=False)
circle = plt.Circle((0,0),0.6,color='white')
ax.add_artist(circle)
ax.legend(data_labels, loc="best")
ax.set_title('Financial Expenditure Analysis - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_126.png')
plt.clf()