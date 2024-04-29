
import matplotlib.pyplot as plt 
country = ['USA','UK','Germany','France']
hotels = [800,900,700,500]
travelers = [3000,2500,2800,2900]

plt.figure(figsize=(10,7))
ax = plt.subplot()
ax.bar(country, hotels, color='#2196f3', label='Hotels')
ax.bar(country, travelers, bottom=hotels, color='#ffc107', label='Travelers')
ax.set_title('Number of Hotels and Travelers in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number')
ax.legend(loc='upper left')
plt.xticks(country,rotation=45)
for i, (hotel, traveler) in enumerate(zip(hotels, travelers)):
    ax.annotate('{}\n{}'.format(hotel, traveler), xy=(i, hotel + traveler/2), ha='center', va='center')
plt.tight_layout()
plt.savefig('Bar Chart/png/256.png')
plt.clf()