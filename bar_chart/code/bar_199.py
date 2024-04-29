
import matplotlib.pyplot as plt
import numpy as np

data=np.array([[120,300,80],[150,400,100],[100,350,90],[140,320,110]])
labels=['New York','Los Angeles','Miami','Las Vegas']

plt.figure(figsize=(10,6))
ax=plt.subplot(111)

bottom=np.zeros(4)
width=0.2

ax.bar(x=np.arange(4)-width,height=data[:,0],width=width,label='Hotels',bottom=bottom,align='edge')
ax.bar(x=np.arange(4),height=data[:,1],width=width,label='Restaurants',bottom=bottom,align='edge')
ax.bar(x=np.arange(4)+width,height=data[:,2],width=width,label='Public Transport',bottom=bottom,align='edge')

ax.set_title('Tourism-related services in four cities in 2021')
ax.set_xticks(np.arange(4))
ax.set_xticklabels(labels,rotation=90,wrap=True)
ax.legend(loc='upper left')

plt.tight_layout()
plt.savefig('bar chart/png/181.png')
plt.clf()