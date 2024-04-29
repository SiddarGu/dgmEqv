
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_labels = ['Home Affordability','Property Quality','Mortgage Rates','Market Activity','Rental Market']
data = np.array([30, 23, 12, 25, 10])
line_labels = ['Category', 'Ratio']

fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(1,1,1)
ax.pie(data,labels=data_labels,autopct='%1.1f%%',startangle=90,counterclock=False)
circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)
ax.legend(data_labels,loc="best")
plt.title('Real Estate and Housing Market Overview - 2023')
ax.axis('equal')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_89.png')
plt.clf()