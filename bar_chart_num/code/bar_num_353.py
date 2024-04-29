
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
ax = plt.subplot()

Country = ['USA','UK','Germany','France']
Railways = [22000,30000,25000,27000]
Roads = [60000,40000,50000,45000]
Airports = [3500,2000,3000,2500]

x = range(len(Country))
ax.bar(x, Railways, bottom = 0, label = 'Railways')
ax.bar(x, Roads, bottom = Railways, label = 'Roads')
ax.bar(x, Airports, bottom = [i+j for i,j in zip(Railways,Roads)], label = 'Airports')

ax.set_xticks(range(len(Country)), minor=False)
ax.set_xticklabels(Country, rotation=45, fontsize = 'large')

plt.title('Length of railways, roads and number of airports in four countries in 2021')
ax.legend()
plt.tight_layout()

for i, v in enumerate(list(zip(Railways,Roads,Airports))):
    ax.text(i, sum(v), str(v), color='black', fontweight='bold',
            ha='center', va='bottom', rotation = 45, wrap = True)

plt.savefig('Bar Chart/png/147.png')
plt.clf()