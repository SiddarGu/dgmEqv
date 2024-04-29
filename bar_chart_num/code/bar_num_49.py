
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[400,350], [100,90], [75,70], [50,45]])
index = np.arange(4)

fig, ax = plt.subplots(figsize=(8,6))
ax.bar(index,data[:,0],label='Internet Users(million)',width=0.3,bottom=data[:,1],color='b')
ax.bar(index,data[:,1],label='Smartphone Users(million)',width=0.3,color='r')
ax.set_xticks(index)
ax.set_xticklabels(['USA','UK','Germany','France'])
ax.legend(loc='upper left')
ax.set_title('Number of internet and smartphone users in four countries in 2021')
for a,b in zip(index,data[:,0]):
    ax.annotate(str(b),xy=(a-0.2,b/2+data[a,1]/2))
for a,b in zip(index,data[:,1]):
    ax.annotate(str(b),xy=(a-0.2,b/2))
plt.tight_layout()
plt.savefig('Bar Chart/png/257.png')
plt.clf()