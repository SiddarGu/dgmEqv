
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

Country = ['USA','UK','Germany','France']
Internet_Users = np.array([320,180,90,60])
Smartphone_Users = np.array([270,160,80,50])
bar_width = 0.3

ax.bar(Country,Internet_Users,color='red',width=bar_width,label='Internet Users')
ax.bar(Country,Smartphone_Users,bottom=Internet_Users,width=bar_width,color='blue',label='Smartphone Users')

for i,j in enumerate(Internet_Users):
    ax.annotate(str(j),xy=(i-0.15,j+10))
for i,j in enumerate(Smartphone_Users):
    ax.annotate(str(j),xy=(i-0.15,j+Internet_Users[i]+10))

plt.xticks(Country)
plt.xlabel('Country')
plt.ylabel('Number of users (million)')
plt.title('Number of internet and smartphone users in four countries in 2021')
plt.legend()
plt.tight_layout()
plt.savefig('Bar Chart/png/350.png')
plt.clf()