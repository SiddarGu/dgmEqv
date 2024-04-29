
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(14,7))
ax = fig.add_subplot()

Country = ['USA','Canada','Mexico','Brazil']
Vegetables = [600,500,400,800]
Fruits = [800,700,600,900]
Grains = [400,500,600,700]

p1 = ax.bar(Country, Vegetables, label='Vegetables', color='#F8B195')
p2 = ax.bar(Country, Fruits, bottom=Vegetables, label='Fruits', color='#F67280')
p3 = ax.bar(Country, Grains, bottom=[i+j for i,j in zip(Vegetables, Fruits)], label='Grains', color='#C06C84')

plt.ylabel('Production(tons)')
plt.title('Food production of vegetables, fruits and grains in four countries in 2021')
plt.legend(loc='upper left')

plt.xticks(Country)
plt.tight_layout()
plt.savefig('bar_91.png')
plt.clf()