
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,5))
ax = plt.subplot(111)

Country = ['USA','UK','Canada','Australia']
Wheat = [1000,1100,850,900]
Rice = [1200,1300,1400,1500]
Corn = [1400,900,1100,1200]

x = np.arange(len(Country))

ax.bar(x-0.2, Wheat, width=0.2, label='Wheat')
ax.bar(x, Rice, width=0.2, label='Rice')
ax.bar(x+0.2, Corn,width=0.2, label='Corn')
ax.set_xticks(x)
ax.set_xticklabels(Country, rotation=30,ha='right', wrap=True)
ax.legend(loc='upper left')
ax.set_title('Food production in four countries in 2021')

plt.tight_layout()
plt.savefig('bar chart/png/183.png')
plt.clf()