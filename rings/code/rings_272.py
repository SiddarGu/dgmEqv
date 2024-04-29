
import matplotlib.pyplot as plt 
import numpy as np

data_labels = ['Greenhouse emission', 'Renewable Energy', 'Pollution Reduction', 'Sustainable Development']
line_labels = ['Category','ratio']
data = np.array([[45,30,12,13]])

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.pie(data[0], startangle=90, counterclock=False,autopct='%1.1f%%',colors = ['#00A8F0','#D8D8D8','#00A8F0','#D8D8D8'])
plt.title("Environmental and Sustainability Report - 2023", fontsize=20)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(1, 0.8))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_130.png')
plt.clf()