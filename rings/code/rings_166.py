
import matplotlib.pyplot as plt 
import numpy as np 

data_labels = ['Production Efficiency', 'Quality Control', 'Supply Chain', 'Customer Satisfaction', 'Branding']
data = [19,15,7,32,27]
line_labels = ['Category', 'Ratio']

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot()
ax.pie(data, startangle=90, counterclock=False, colors=['#6A9BFF', '#FF6F6F', '#A0FF68', '#FFF66D', '#B4B4FF'], autopct='%1.1f%%')
circle = plt.Circle((0,0), 0.70, color='white')
ax.add_artist(circle)
ax.axis('equal')
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(1.3, 1))
ax.set_title('Food and Beverage Industry Performance - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_139.png')
plt.clf()