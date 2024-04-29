
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data_labels = ['Research & Development', 'Quality Control', 'Manufacturing', 'Innovation', 'Safety']
data = [0.3, 0.25, 0.1, 0.15, 0.2]
line_labels = ['Category']

fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(data, labels=data_labels, autopct='%1.1f%%', startangle=90, counterclock=False)
circle=plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(1.3, 1.12))
plt.title('Science & Engineering Progress - 2023', fontsize=16)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_42.png')
plt.clf()