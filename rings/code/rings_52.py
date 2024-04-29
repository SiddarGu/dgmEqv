
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Software Development', 'Cyber Security', 'Networking', 'Database Design', 'Web Development']
data = np.array([25, 15, 20, 10, 30])
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False)
inner_circle = plt.Circle((0, 0), 0.5, color='white')
ax.add_artist(inner_circle)
ax.set_title('Technology and Internet Usage in 2023')
ax.legend(data_labels, loc="best", bbox_to_anchor=(1,0.5))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_113.png')
plt.cla()