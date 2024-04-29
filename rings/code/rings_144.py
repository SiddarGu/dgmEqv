
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_labels = ['Recruiting','Retention','Training & Development','Performance Management','Employee Engagement']
data = [13,25,32,15,15]
line_labels = ['Category','ratio']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

ax.pie(data, labels=data_labels, autopct='%1.1f%%', startangle=45, counterclock=False, colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
inner_circle = plt.Circle((0,0), 0.5, color='white')
ax.add_artist(inner_circle)
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(1.2, 0.8))
ax.set_title('Human Resources and Employee Management - 2023', fontsize=14, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_105.png')
plt.clf()