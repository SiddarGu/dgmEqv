
import matplotlib.pyplot as plt
import numpy as np

#create figure
fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot(111)

#plot data
Country=['USA','UK','Germany','France']
CoffeeConsumption=[2500,3200,3000,2700]
TeaConsumption=[3000,2800,2600,2900]
bottom=np.array([0,0,0,0])
ax.bar(Country,CoffeeConsumption,label='Coffee Consumption',bottom=bottom)
bottom+=np.array(CoffeeConsumption)
ax.bar(Country,TeaConsumption,label='Tea Consumption',bottom=bottom)

#display legend
ax.legend(loc='upper left')

#display text
for x,y1,y2 in zip(Country,CoffeeConsumption,TeaConsumption):
    ax.text(x,y1/2+y2/2,str(y1+y2)+'kg',ha='center')

#set title
plt.title('Coffee and tea consumption in four countries in 2021')

#set xticks
plt.xticks(Country)

#tight layout
plt.tight_layout()

#save figure
plt.savefig('Bar Chart/png/453.png')

#clear figure
plt.clf()