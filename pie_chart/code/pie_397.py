
import matplotlib.pyplot as plt
import numpy as np

labels=['Groceries','Electronics','Clothing','Shoes','Toys']
sizes=[25,20,30,15,10]

fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(111)
ax.set_title('Product Distribution in Online Retail Stores, 2023')
ax.pie(sizes,labels=labels,autopct='%1.2f%%',
       textprops={'fontsize': 14,'wrap':True, 'rotation': 60},
       startangle=90)
ax.axis('equal') 
plt.tight_layout()
plt.savefig('pie chart/png/294.png')
plt.clf()