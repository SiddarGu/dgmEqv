
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))

data = {'Country': ['USA', 'UK', 'Germany', 'France'],
        'GDP(Billion)': [21.44, 2.83, 4.03, 2.80],
        'GDP Growth Rate': [4.2, 6.1, 3.2, 5.6],
        'Unemployment Rate': [6.2, 4.5, 5.2, 8.6],}

x = np.arange(len(data['Country']))
GDP = data['GDP(Billion)']
GrowthRate = data['GDP Growth Rate']
unemployment = data['Unemployment Rate']

ax = plt.subplot(111)
ax.bar(x-0.2, GDP, width=0.2, color='b', align='center', label='GDP')
ax.bar(x, GrowthRate, width=0.2, color='g', align='center', label='Growth Rate')
ax.bar(x+0.2, unemployment, width=0.2, color='r', align='center', label='Unemployment Rate')

plt.xticks(x, data['Country'])
plt.legend(loc='upper left')
plt.title("GDP and Unemployment rate of four countries in 2021")
plt.grid(True, linestyle='--', linewidth=1)
plt.tight_layout()
plt.savefig('bar chart/png/508.png')
plt.clf()