
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Disease Prevention', 'Treatment Quality', 'Patient Care', 'Research', 'Outreach']
data = np.array([35, 20, 15, 10, 20])
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

ax.pie(data, labels=data_labels, startangle=90, counterclock=False, 
       colors=['darkorange', 'gold', 'lightgreen', 'lightskyblue', 'lightcoral'])
centre_circle = plt.Circle((0, 0), 0.60, color="white")
ax.add_artist(centre_circle)
ax.axis('equal')
ax.legend(data_labels, loc='best')
plt.title('Healthcare Overview - 2023', fontsize=18)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_97.png')
plt.clf()