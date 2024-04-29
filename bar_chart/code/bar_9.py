
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Laws = [200, 250, 280, 270]
Provisions = [350, 400, 420, 390]

fig, ax = plt.subplots(figsize=(8,6))
ax.bar(Country, Laws, label='Laws', bottom=Provisions)
ax.bar(Country, Provisions, label='Provisions', bottom=0)
ax.set_title('Number of Laws and Provisions in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Amount')
ax.legend(loc='upper right')
plt.xticks(Country)
plt.tight_layout()
plt.savefig('bar chart/png/222.png')
plt.clf()