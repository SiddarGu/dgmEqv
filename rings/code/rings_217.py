
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Disease Prevention','Vaccination','Medication','Healthcare Access','Patient Education']
data = np.array([37,20,13,25,5])
line_labels = ['Category','ratio']

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=180, counterclock=False)
ring = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(ring)
ax.legend(data_labels)
ax.set_title('Healthcare Quality Evaluation - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_73.png')
plt.clf()