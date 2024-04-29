
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Crop Production', 'Livestock Management', 'Irrigation', 'Food Processing', 'Supply Chain']
data = np.array([20, 30, 5, 25, 20])
line_labels = ['Category', 'ratio']

fig, ax = plt.subplots(figsize=(6,6))

ax.pie(data, radius=1, startangle=90, counterclock=False, labels=data_labels, autopct='%1.1f%%', pctdistance=0.8)

centre_circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(centre_circle)
ax.legend(data_labels, loc='upper left')

plt.title("Food Production and Agriculture Overview - 2023")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_33.png')
plt.clf()