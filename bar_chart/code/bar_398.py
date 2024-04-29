
import matplotlib.pyplot as plt
import numpy as np

data = [['USA',4500,2500],['UK',4000,3000],['Germany',3500,3500],['France',3000,4000]]

countries, retail, ecommerce = [],[],[]
for row in data:
    countries.append(row[0])
    retail.append(row[1])
    ecommerce.append(row[2])

x = np.arange(len(countries))
width = 0.35

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1,1,1)
ax.bar(x - width/2, retail, width, label='Retail Sales', color='#f75b5b')
ax.bar(x + width/2, ecommerce, width, label='E-commerce Sales', color='#70d5f2')

ax.set_ylabel('Sales(million)')
ax.set_title('Comparison of Retail and E-commerce sales in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(countries, rotation=45, ha='right', wrap=True)
ax.legend()

fig.tight_layout()
plt.savefig('bar chart/png/448.png')
plt.clf()