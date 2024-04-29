
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_labels = ['Home Prices','Mortgage Rates','Rental Rates','Home Sales','Foreclosures']
line_labels = ['Category']
data = np.array([[30,12,27,19,12]])

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
colors = ['#FF9F4C','#FF99CA','#FF6C3F','#FF3F35','#A3FF9F']

ax.pie(data[0], colors=colors, startangle=90, counterclock=False)
centre_circle = plt.Circle((0,0),0.6,fc='white')
ax.add_artist(centre_circle)
ax.legend(data_labels, bbox_to_anchor=(1.1, 1.05))
ax.set_title('Real Estate and Housing Market Analysis - 2021')
ax.set_xlabel('Category')
ax.grid()

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_118.png')
plt.clf()