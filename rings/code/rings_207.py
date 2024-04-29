
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_labels = ['Profits','Expenses','Investments','Revenue','Market Share']
line_labels = ['Category']
data = np.array([[54,20,7,16,3]])

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()

ax.pie(data.flatten(), labels=data_labels,counterclock=False,startangle=90)
circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)
ax.set_title('Business Growth Overview - 2023')
ax.legend(data_labels, loc='upper center', bbox_to_anchor=(0.5, -0.1))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_60.png')
plt.clf()