
import numpy as np
import matplotlib.pyplot as plt

data = [
    ('USA', 350, 300),
    ('UK', 100, 90),
    ('Germany', 85, 75),
    ('France', 75, 65)
]

Country,Internet_Users,Smartphone_Users = zip(*data)

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

p1 = ax.bar(Country, Internet_Users, label='Internet Users(million)')
p2 = ax.bar(Country, Smartphone_Users, bottom=Internet_Users, label='Smartphone Users(million)')

ax.set_title('Number of Internet and Smartphone Users in four countries in 2021')
ax.set_xticks(Country)
ax.set_ylabel('People (million)')
ax.set_xlabel('Country')
ax.legend()

for i,j in enumerate(Internet_Users):
    ax.annotate(str(j),xy=(i,j+2))

for i,j in enumerate(Smartphone_Users):
    ax.annotate(str(j),xy=(i,j+Internet_Users[i]+2))

plt.tight_layout()
plt.savefig('Bar Chart/png/475.png')
plt.clf()