
import matplotlib.pyplot as plt
import numpy as np

data = {'Renewable Resources':['Solar Energy', 'Wind Energy', 'Hydropower', 'Geothermal Energy', 'Biomass Energy'],
        'Percentage':[20, 30, 25, 15, 10]}
labels = data['Renewable Resources']
sizes = data['Percentage'] 

fig = plt.figure(figsize=(8,8)) 
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 8})
ax.axis('equal')
plt.title('Distribution of Renewable Energy Resources in the USA, 2023')
plt.tight_layout()
plt.xticks([])
plt.legend(loc='upper left')
plt.savefig('pie chart/png/327.png')
plt.clf()