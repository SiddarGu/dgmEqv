

import matplotlib.pyplot as plt 
import numpy as np 

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)
labels = ['Fast Food','Restaurants','Grocery Stores','Convenience Stores','Cafes']
data = [30,25,20,15,10]
ax.pie(data,labels=labels,autopct='%1.1f%%',startangle=90)
ax.set_title('Distribution of Food and Beverage Industry in the USA, 2023')
ax.text(-1.5,1.5,'Total 100%',fontsize=14)
ax.legend(labels,bbox_to_anchor=(1.2,1.05)) 
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/434.png')
plt.clf()