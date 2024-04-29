
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(7,7))
ax=fig.add_subplot(111)
labels=['Amazon','Walmart','eBay','Alibaba','Apple','Others']
sizes=[40,20,15,10,5,10]
explode = (0.1, 0, 0, 0, 0, 0)
ax.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%', shadow=True, startangle=90,textprops={'fontsize':14,'wrap':True,'rotation':90})
ax.axis('equal')
ax.set_title('Market Share for Online Retailers in the USA, 2023',fontsize=15)
plt.xticks(fontsize=14)
plt.tight_layout()
plt.savefig('pie chart/png/500.png')
plt.clf()