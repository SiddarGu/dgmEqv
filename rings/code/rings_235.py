
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_labels = ['Financial Planning','Risk Management','Budgeting','Tax Planning','Credit Management']
data = [18,16,33,13,20]
line_labels = ['Category','ratio']

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, radius=1, colors=['r','g','b','c','m'])
circle = plt.Circle((0,0), 0.75, color='white')
ax.add_artist(circle)
ax.set_title('Financial Planning Overview - 2023', fontsize=14)
ax.legend(data_labels, loc="center left", bbox_to_anchor=(1.2, 0, 0.5, 1))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_10.png')
plt.clf()