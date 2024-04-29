
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data_labels = ['Attractions','Accomodation', 'Experience', 'Investment', 'Response Rate']
line_labels = ['Category']
data = np.array([[27,13,31,19,10]])

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Tourism and Hospitality Industry - 2023', fontsize=20)
ax.axis('equal')

ax.pie(data.flatten(), labels=data_labels, startangle=90, counterclock=False)

c = mpatches.Circle((0.0, 0.0), 0.7, color='white')
ax.add_artist(c)
ax.legend(data_labels, loc=[0.8, 0.7], fontsize=14)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_129.png')
plt.clf()