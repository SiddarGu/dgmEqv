
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Raw Ingredients', 'Distribution', 'Storage', 'Product Development',
               'Production', 'Marketing']
line_labels = ['Category', 'ratio']
data = np.array([14, 13, 4, 22, 14, 33])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, wedgeprops={'width': 0.3})
centre_circle = plt.Circle((0, 0), 0.5, color='white')
ax.add_artist(centre_circle)
ax.legend(data_labels)
ax.set_title('Food and Beverage Industry Performance - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_82.png')
plt.clf()