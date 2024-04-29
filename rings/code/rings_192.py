
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Home Prices','Mortgage Rates','Supply','Demand']
line_labels = ['Category']
data = np.array([[45,20,15,20]])

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.pie(data.flatten(), labels=data_labels, startangle=90, counterclock=False, autopct='%.2f%%', colors=['#ff7f0e','#1f77b4','#2ca02c','#d62728'])

circle = plt.Circle((0,0), 0.6, color='white')
ax.add_artist(circle)

ax.legend(data_labels, loc='best')
plt.title('Real Estate and Housing Market Trends - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_4.png')
plt.cla()