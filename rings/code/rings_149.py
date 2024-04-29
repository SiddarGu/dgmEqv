
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Education','Arts','Social Sciences','Humanities','Language']
data = [0.25, 0.15, 0.25, 0.25, 0.10]
line_labels = ['Area','ratio']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.set_title("Humanities & Social Sciences - 2023")
ax.pie(data, labels=data_labels, autopct='%1.1f%%', startangle=45, counterclock=False)
ax.legend(data_labels, bbox_to_anchor=(1,0.5), loc="center right", fontsize=12)
circle = plt.Circle((0,0), 0.5, color='white')
ax.add_artist(circle)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_110.png')
plt.clf()