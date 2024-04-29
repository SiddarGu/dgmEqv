
import matplotlib.pyplot as plt

Region = ['North','South','East','West']
Fast_Food = [200,220,180,210]
Coffee = [400,420,380,410]
Beverages = [300,320,280,310]

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot()
ax.bar(Region, Fast_Food, label='Fast Food', bottom=0)
ax.bar(Region, Coffee, label='Coffee', bottom=Fast_Food)
ax.bar(Region, Beverages, label='Beverages', bottom=[sum(x) for x in zip(Fast_Food, Coffee)])
plt.xticks(Region)
plt.legend()
plt.title('Number of food and beverage outlets in four regions in 2021')


plt.tight_layout()
plt.savefig('bar_3.png')
plt.clf()