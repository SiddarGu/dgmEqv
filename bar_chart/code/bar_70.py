
import matplotlib.pyplot as plt
import numpy as np

Month = ['January','February','March','April']
Retail_Sales = [300,350,400,450]
Online_Sales = [400,450,500,550]
Total_Sales = [700,800,900,1000]

x = np.arange(len(Month))

fig, ax = plt.subplots(figsize=(14,7))
ax.bar(x-0.15, Retail_Sales, width=0.3, label='Retail Sales', color='#00A0A0')
ax.bar(x+0.15, Online_Sales, width=0.3, label='Online Sales', color='#FF7D7D')
ax.bar(x, Total_Sales, width=0.3, label='Total Sales', color='#FFD97D')

plt.xticks(x, Month, rotation=45, wrap=True)

plt.legend(loc='best', fontsize=14)
plt.title('Total and online retail sales from January to April 2021', fontsize=20)

plt.tight_layout()
plt.savefig('bar chart/png/468.png')
plt.clf()