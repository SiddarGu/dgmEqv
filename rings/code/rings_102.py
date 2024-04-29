
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Online Shopping','Store Visits','Advertising','Customer Retention','Brand Promotion']
line_labels = ['Category', 'ratio']
data = np.array([['Online Shopping','Store Visits','Advertising','Customer Retention','Brand Promotion'],
                 [40, 15, 5, 25, 15]])

fig, ax = plt.subplots(figsize=(9, 9))
ax.pie(data[1], labels=data[0], startangle=90, counterclock=False, 
        colors=['#1f77b4', '#2ca02c', '#d62728', '#9467bd', '#ff7f0e'])
circle = plt.Circle((0, 0), 0.5, color='white')
ax.add_artist(circle)
ax.legend(data_labels, loc='center', bbox_to_anchor=(1.2, .5))
ax.set_title('Retail & E-commerce Market Overview - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_50.png')
plt.clf()