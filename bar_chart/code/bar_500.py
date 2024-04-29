
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
restaurants = [200,220,180,210]
grocery = [400,420,400,430]
cafes = [150,170,130,160]

fig,ax = plt.subplots(figsize=(7,6))
ax.bar(x-0.2,restaurants,color='b',width=0.2,label='Restaurants')
ax.bar(x,grocery,color='r',width=0.2,label='Grocery Store')
ax.bar(x+0.2,cafes,color='g',width=0.2,label='Cafes')

plt.xticks(x,['North','South','East','West'],rotation=45,fontsize=10)
plt.legend(loc='best',fontsize=10)
plt.title('Number of food and beverage establishments in four regions in 2021',fontsize=12)
plt.tight_layout()
plt.savefig('bar chart/png/76.png')
plt.clf()