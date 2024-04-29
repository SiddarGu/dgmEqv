

import matplotlib.pyplot as plt
import numpy as np

data_labels=['Home Prices','Construction Activity','Homeownership Rate','Rental Rates','Foreclosures']
data=[45,17,20,15,3]
line_labels=['Category']

fig=plt.figure(figsize=(10,7))
ax=fig.add_subplot()
ax.pie(data,labels=data_labels,autopct='%1.1f%%',startangle=90,counterclock=False,colors = ['red', 'green', 'blue','yellow','purple'])
circle=plt.Circle(xy=(0,0),radius=0.7,facecolor='white')
ax.add_artist(circle)
ax.set_title('Real Estate and Housing Market Trends - 2023')
plt.tight_layout()
ax.legend(data_labels)

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_43.png')
plt.cla()