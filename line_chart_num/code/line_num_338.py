

import matplotlib.pyplot as plt 
import numpy as np 

data = [['January',2250,650],
        ['February',2400,700],
        ['March',2700,800],
        ['April',2500,750],
        ['May',2450,850],
        ['June',2650,1000],
        ['July',3000,1100],
        ['August',2800,950]]

month, retail, ecommerce = np.array(data).T

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)
ax.plot(month, retail, marker='o', label='Retail Sales')
ax.plot(month, ecommerce, marker='o', label='E-commerce Sales')

for x, y, label in zip(month, retail, retail):
    plt.annotate(label,
                 (x,y),
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center')

for x, y, label in zip(month, ecommerce, ecommerce):
    plt.annotate(label,
                 (x,y),
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center')

plt.title('Comparison of Retail and E-commerce Sales in the US, 2021')
plt.xlabel('Month')
plt.ylabel('Sales(million USD)')
plt.xticks(month, rotation='vertical') 
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/596.png')
plt.clf()