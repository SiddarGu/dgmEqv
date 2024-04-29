
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,5))

data = [[200,150],[100,70],[90,80],[80,70]]
Country = ['USA','UK','Germany','France']

x = np.arange(len(Country))

Internet_User = [i[0] for i in data]
Smartphone_User = [i[1] for i in data]

width = 0.35

ax = plt.bar(x-width/2, Internet_User, width, label = 'Internet User(million)')
ax1 = plt.bar(x+width/2, Smartphone_User, width, label = 'Smartphone User(million)')

plt.xlabel('Country')
plt.ylabel('Users(million)')
plt.xticks(x,Country)
plt.title('Number of internet and smartphone users in four countries in 2021')
plt.legend()

for i,j in zip(ax,ax1):
    h1 = i.get_height()
    h2 = j.get_height()
    plt.text(i.get_x() + i.get_width()/2., h1/2, '%d' % h1, ha="center", va="bottom", fontsize=10, color="black")
    plt.text(j.get_x() + j.get_width()/2., h2/2, '%d' % h2, ha="center", va="bottom", fontsize=10, color="black")

plt.tight_layout()
plt.savefig('Bar Chart/png/314.png')
plt.clf()