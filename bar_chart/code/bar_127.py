
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

Country = ['USA','UK','Germany','France']
Manufacturing = [1200, 1400, 1100, 1300]
Retail = [1000, 900, 1100, 1200]

ax.bar(Country, Manufacturing, label = 'Manufacturing Output (million)', color = 'b', bottom = Retail)
ax.bar(Country, Retail, label = 'Retail Output (million)', color = 'r')

plt.xticks(Country)
plt.grid(linestyle = '--', alpha = 0.5)
plt.title('Manufacturing and retail output in four countries in 2021')
plt.legend()
plt.tight_layout()
plt.savefig('bar chart/png/491.png')
plt.clf()