
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Research and Development','Quality Assurance','Production Efficiency','Waste Reduction','Innovation']
data = [0.25, 0.20, 0.30, 0.10, 0.15]
line_labels = ['Category', 'ratio']

fig, ax = plt.subplots(figsize=(8,8))
wedges, texts, autotexts = ax.pie(data, startangle=90, counterclock=False, autopct='%1.1f%%')
plt.setp(autotexts, size=14, weight="bold")
c = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(c)
ax.legend(data_labels, loc='upper left')
ax.set_title('Science and Engineering Performance - 2023', fontsize=16)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_67.png')
plt.clf()