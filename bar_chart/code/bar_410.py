
import matplotlib.pyplot as plt

data = {'Country':['USA','Canada','Brazil','Mexico'], 'Crops Produced(billion tons)':[2.4,1.7,3.6,2.2], 'Livestock Produced(billion tons)':[1.2,0.9,1.3,1.1]}

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

ax.bar(data['Country'], data['Crops Produced(billion tons)'], label='Crops', width=0.4, bottom=data['Livestock Produced(billion tons)'])
ax.bar(data['Country'], data['Livestock Produced(billion tons)'], label='Livestock',width=0.4)

ax.set_title('Total Crops and Livestock Produced in Four Countries in 2021', fontsize=14)
ax.set_xticks(data['Country'])
ax.set_xlabel('Country', fontsize=12)
ax.set_ylabel('Produced Quantities (billion tons)', fontsize=12)
ax.legend(loc='upper left')
fig.tight_layout()
plt.savefig('bar chart/png/2.png')
plt.clf()