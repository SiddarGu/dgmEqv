
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Research','Development','Manufacturing','Design','Testing']
data = [17,20,25,17,21]
line_labels = ['Area','ratio']

plt.figure(figsize=(7,7))
ax = plt.subplot()
ax.pie(data, labels=data_labels,autopct='%1.1f%%',startangle=45,counterclock=False)
circle = plt.Circle((0,0), 0.70, fc='white')
ax.add_artist(circle)
ax.legend(data_labels, loc='best')
plt.title('Science and Engineering Progress - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_54.png')
plt.clf()