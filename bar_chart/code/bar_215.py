
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
ax = plt.subplot()

Country = ['USA', 'UK', 'Germany', 'France']
Museums = [200, 220, 150, 180]
Theaters = [150, 170, 130, 160]
Galleries = [120, 100, 90, 110]

ax.bar(Country, Museums, label='Museums')
ax.bar(Country, Theaters, bottom=Museums, label='Theaters')
ax.bar(Country, Galleries, bottom=[x + y for x, y in zip(Museums, Theaters)], label='Galleries')

ax.set_xlabel('Country')
ax.set_ylabel('Number of venues')
ax.set_title('Number of arts and culture venues in four countries in 2021')
ax.legend(loc='upper right')

plt.xticks(Country, rotation=45, ha='right', wrap=True)
plt.tight_layout()
plt.savefig('bar chart/png/439.png')
plt.clf()