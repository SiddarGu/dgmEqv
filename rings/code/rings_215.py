
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

data_labels = ['Quality of Service','Amenities','Location','Customer Satisfaction','Cleanliness']
data = np.array([38,18,34,7,3])
line_labels = ['Category','ratio']

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot()
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#17B8BE','#FAAB1A','#8B1FA9','#F35D20','#F8E71C'])
circle = Circle(xy=(0, 0), radius=0.6, facecolor='white')
ax.add_artist(circle)
ax.legend(data_labels, loc="lower right")
plt.title('Tourism and Hospitality Performance - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_70.png')
plt.close()