
import matplotlib.pyplot as plt
import numpy as np
 
data_labels = ['Crop Yield', 'Livestock Production', 'Food Security', 'Waste Reduction', 'Sustainable Practices']
data = np.array([45, 25, 15, 10, 5])
line_labels = ['Category']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, colors=['#0090d9','#eaa03b','#f24f3b','#e64d3b','#7e543b'])
circle = plt.Circle((0, 0), radius=0.5, fc='white', edgecolor='black')
ax.add_artist(circle)
ax.legend(data_labels, loc='upper center')
plt.title('Agriculture and Food Production Overview - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_127.png')
plt.clf()