
import matplotlib.pyplot as plt
import numpy as np

country=['USA','UK','Germany','France']
offline_sales=[20,15,10,12]
online_sales=[25,30,20,27]

fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot()

ax.bar(country,offline_sales,width=0.3,label='Offline Sales',bottom=online_sales)
ax.bar(country,online_sales,width=0.3,label='Online Sales')

plt.xticks(country,rotation=45,wrap=True)
ax.set_title('Retail sales comparison between offline and online in four countries in 2021')
ax.legend(loc='lower right')
plt.tight_layout()
plt.savefig('bar chart/png/484.png')
plt.clf()