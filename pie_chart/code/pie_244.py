
import matplotlib.pyplot as plt
import numpy as np

categories=['Fast Food','Grocery Stores','Restaurants','Online Delivery','Convenience Stores']
percentage=[35,20,20,15,10]
fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(111)
ax.pie(percentage,labels=categories,autopct='%1.1f%%',textprops={'fontsize':10},startangle=90,shadow=True,explode=[0,0,0,0.2,0])
ax.axis('equal')
ax.set_title('Distribution of Food and Beverage Industry in the USA, 2023',fontsize=15)
plt.tight_layout()
plt.xticks(rotation=90,fontsize=10)
plt.savefig('pie chart/png/482.png')
plt.clf()