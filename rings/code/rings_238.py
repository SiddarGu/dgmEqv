
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Profit Margin', 'Expenses', 'Investments', 'Revenue', 'Market Share']
line_labels = ['Category']
data = np.array([[30, 25, 10, 20, 15]])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(data.flatten(), labels=data_labels, autopct='%1.1f%%', startangle=90, counterclock=False)
c = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(c)
ax.legend(data_labels, loc='best', bbox_to_anchor=(0.9, 0.9))
ax.set_title('Business Financial Analysis - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_13.png')
plt.clf()