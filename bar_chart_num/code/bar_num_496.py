
import matplotlib.pyplot as plt
import numpy as np

data = {'Country':['USA', 'UK', 'Germany', 'France'], 
        'Renewable Energy (%)':[20, 30, 25, 35], 
        'Pollution (million tons)':[25, 15, 10, 5]}

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
width = 0.35

x = np.arange(len(data['Country']))

renewable = ax.bar(x, data['Renewable Energy (%)'], width, color='g')
pollution = ax.bar(x + width, data['Pollution (million tons)'], width,color='r')

ax.set_title('Percentage of Renewable Energy and Pollution in four countries in 2021')
ax.set_xticks(x + width / 2)
ax.set_xticklabels(data['Country'], rotation=90)
ax.legend((renewable[0], pollution[0]), ('Renewable Energy (%)', 'Pollution (million tons)'))

ax.annotate('{}'.format(data['Renewable Energy (%)'][0]), xy=(0, data['Renewable Energy (%)'][0]), xytext=(0, 10), 
            textcoords="offset points", ha='center', va='bottom')
ax.annotate('{}'.format(data['Renewable Energy (%)'][1]), xy=(1, data['Renewable Energy (%)'][1]), xytext=(0, 10), 
            textcoords="offset points", ha='center', va='bottom')
ax.annotate('{}'.format(data['Renewable Energy (%)'][2]), xy=(2, data['Renewable Energy (%)'][2]), xytext=(0, 10), 
            textcoords="offset points", ha='center', va='bottom')
ax.annotate('{}'.format(data['Renewable Energy (%)'][3]), xy=(3, data['Renewable Energy (%)'][3]), xytext=(0, 10), 
            textcoords="offset points", ha='center', va='bottom')

ax.annotate('{}'.format(data['Pollution (million tons)'][0]), xy=(0, data['Pollution (million tons)'][0]), xytext=(0, -10), 
            textcoords="offset points", ha='center', va='top')
ax.annotate('{}'.format(data['Pollution (million tons)'][1]), xy=(1, data['Pollution (million tons)'][1]), xytext=(0, -10), 
            textcoords="offset points", ha='center', va='top')
ax.annotate('{}'.format(data['Pollution (million tons)'][2]), xy=(2, data['Pollution (million tons)'][2]), xytext=(0, -10), 
            textcoords="offset points", ha='center', va='top')
ax.annotate('{}'.format(data['Pollution (million tons)'][3]), xy=(3, data['Pollution (million tons)'][3]), xytext=(0, -10), 
            textcoords="offset points", ha='center', va='top')

plt.tight_layout()
plt.savefig('Bar Chart/png/337.png')
plt.clf()