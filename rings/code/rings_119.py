
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

data_labels = np.array(['Usage', 'Security', 'Efficiency', 'Networking', 'Reliability'])
data = np.array([38, 14, 22, 12, 14])
line_labels = np.array(['Category'])

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.pie(data, colors=['red','blue','green','yellow','orange'], startangle=90, counterclock=False, textprops={'fontsize':14})
circle = plt.Circle((0,0), 0.65, color='white')
ax.add_artist(circle)
ax.set_title('Technology and Internet Adoption - 2023', fontsize=20)
ax.legend(data_labels, loc='upper left', bbox_to_anchor=(-0.1, 1.), fontsize=14)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_70.png')
plt.clf()