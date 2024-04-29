
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Donations', 'Fundraising', 'Volunteers', 'Program Management', 'Resource Allocation'] 
data = [45, 21, 14, 20, 0]
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot()
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, 
       colors=['#D91E18','#F7CF5E','#5EA3A3','#B9C6D4','#F2F2F2'])
circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)
ax.legend(data_labels, bbox_to_anchor=(1.1, 0.5))
plt.title('Nonprofit Organization Performance Overview - 2021')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_18.png')
plt.clf()