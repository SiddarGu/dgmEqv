
import matplotlib.pyplot as plt
import numpy as np

Region=['North','South','East','West']
Housing_Prices=[4.5,3.8,3.2,4.0]
Sales_Volume=[2.6,3.2,2.8,2.9]

fig,ax = plt.subplots(figsize=(10,6))
ax.bar(Region, Housing_Prices, width=0.4, label='Housing Prices(million)', bottom=np.array(Sales_Volume), color='royalblue', edgecolor='black')
ax.bar(Region, Sales_Volume, width=0.4, label='Sales Volume(million)', color='darkorange', edgecolor='black')
ax.set_title('Housing Prices and Sales Volume in four regions in 2021')
ax.set_ylabel('million')
ax.legend()
ax.set_xticks(Region)

for i,j in zip(Region,Housing_Prices):
    ax.annotate(str(j), xy=(i, j+0.3), ha='center')
for i,j in zip(Region,Sales_Volume):
    ax.annotate(str(j), xy=(i, j+0.3), ha='center')

fig.tight_layout()
fig.savefig('Bar Chart/png/486.png')
plt.close()