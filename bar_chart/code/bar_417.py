
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Manufactured_goods = [1500, 1000, 1350, 1200]
Exported_goods = [800, 600, 700, 500]

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot()

width = 0.4
x_pos = np.arange(len(Country))
ax.bar(x_pos - width/2, Manufactured_goods, width, label='Manufactured Goods')
ax.bar(x_pos + width/2, Exported_goods, width, label='Exported Goods')

ax.set_title('Manufactured and exported goods in four countries in 2021')
ax.set_xticks(x_pos)
ax.set_xticklabels(Country, rotation=45, wrap=True)
ax.legend(loc='upper left')
plt.tight_layout()

plt.savefig('bar chart/png/215.png')
plt.clf()