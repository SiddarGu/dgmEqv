
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data_labels = ['Crop Yields','Livestock Breeding','Quality Assurance','Food Storage','Water Management']
data = np.array([39,17,13,11,20])
line_labels = ['Category','ratio']

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.set_title('Agriculture and Food Production - 2023')
ax.pie(data, startangle=90, counterclock=False, labels=data_labels, autopct='%1.1f%%', pctdistance=1.1, labeldistance=1.2)
plt.Circle((0,0), 0.72, color='white')
ax.add_artist(plt.Circle((0,0), 0.72, color='white'))
ax.legend(data_labels, loc='center')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_54.png')
plt.clf()