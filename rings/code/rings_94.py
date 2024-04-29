
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Ticket Sales', 'Sponsorship', 'Merchandise', 'Advertisements', 'Media Coverage']
data = np.array([19, 22, 25, 19, 15])
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.set_title('Sports and Entertainment Revenue - 2023')
ax.pie(data, labels=data_labels, autopct='%1.2f%%', radius=1.2, startangle=180, counterclock=False)
inner_circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(inner_circle)
ax.legend(data_labels, bbox_to_anchor=(1.2, 0.8), loc="center left")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_36.png")
plt.clf()