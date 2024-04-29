
import matplotlib.pyplot as plt
import numpy as np

data_labels = np.array(['Production Efficiency', 'Consumer Satisfaction', 'Ingredient Quality', 'Distribution Network', 'Marketing Strategies'])
data = np.array([25,20,11,30,14])
line_labels = np.array(['Category', 'ratio'])

fig, ax = plt.subplots(figsize=(8,8))
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, autopct='%1.1f%%')
plt.title('Food and Beverage Performance - 2023')

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax.axis('equal')  
plt.tight_layout()

ax.legend(data_labels, loc="upper left", bbox_to_anchor=(1,1))
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_25.png', bbox_inches="tight") 

plt.clf()