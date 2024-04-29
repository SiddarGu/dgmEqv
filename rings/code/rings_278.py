
import matplotlib.pyplot as plt
import numpy as np

data_labels = [str(i).strip() for i in 'Traveler Satisfaction, Hospitality Services, Tourist Attraction, Tour Guide Quality, Security and Safety'.split(',')]
data = [float(i.strip('%'))/100 for i in '21%, 33%, 18%, 15%, 13%'.split(',')]
line_labels = [str(i).strip() for i in 'Category, ratio'.split(',')]

fig, ax = plt.subplots(figsize=(10,8))
ax.pie(data, startangle=90, counterclock=False, labels=data_labels, 
       wedgeprops=dict(width=0.3, edgecolor='white'))

center_circle = plt.Circle((0,0), 0.70, fc='white')
ax.add_artist(center_circle)

ax.axis('equal')
ax.set(title='Tourism and Hospitality Performance - 2023')
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(1, 0.9))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_139.png')
plt.clf()