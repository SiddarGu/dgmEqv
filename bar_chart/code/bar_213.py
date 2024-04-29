
import matplotlib.pyplot as plt

country = ['USA','UK','Germany','France']
farmers = [45,30,25,35]
crops = [80,50,40,60]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot() 

ax.bar(country, farmers, label='Farmers')
ax.bar(country, crops, bottom=farmers, label='Crops')

ax.set_title('Number of farmers and crops production in four countries in 2021')
ax.legend(loc='upper left')

plt.xticks(rotation=45, wrap=True)
plt.tight_layout()
plt.savefig('bar chart/png/173.png')
plt.clf()