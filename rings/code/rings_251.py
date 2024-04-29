
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_labels = ['Recruitment','Training','Retention','Performance','Satisfaction']
line_labels = ['Category','ratio']
data = np.array([['Recruitment',24],['Training',17],['Retention',30],['Performance',19],['Satisfaction',10]])

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111)
ax.pie(data[:,1], labels=data[:,0], startangle=90, counterclock=False, colors=plt.cm.Set1(np.arange(5)/6))
center_circle = plt.Circle((0,0), 0.6, color='white')
ax.add_artist(center_circle)
ax.legend(data_labels, loc='lower right', bbox_to_anchor=(1.25, 0.1))
ax.set_title('Employee Management in 2021 - An Overview', fontsize=14, fontweight='bold')
plt.xticks(fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_100.png')
plt.clf()