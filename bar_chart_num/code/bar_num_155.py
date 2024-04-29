
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

Country=['USA','UK','Germany','France']
Hotels=[150,200,180,230]
Tourists=[400,450,400,470]

ax.bar(Country,Hotels,bottom=Tourists,width=0.5,label='Hotels')
ax.bar(Country,Tourists,width=0.5,label='Tourists')

plt.xticks(Country)
plt.title('Number of hotels and tourists in four countries in 2021')
plt.legend()
for i,v in enumerate(Hotels):
    ax.text(i-.25,v/2+Tourists[i],str(v),color='blue', fontweight='bold')
for i,v in enumerate(Tourists):
    ax.text(i-.25,v/2,str(v),color='red', fontweight='bold')

fig.tight_layout()
plt.savefig("Bar Chart/png/20.png")
plt.clf()