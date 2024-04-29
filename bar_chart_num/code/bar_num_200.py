
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

country = ['USA', 'UK', 'Germany', 'France']
museums = [150, 180, 140, 170]
theatres = [200, 220, 180, 210]
galleries = [250, 270, 230, 260]

x = [i for i, _ in enumerate(country)]

ax.bar(x, museums, width=0.5, label='Museums', color='#1f77b4')
ax.bar(x, theatres, width=0.5, bottom=museums, label='Theatres', color='#ff7f0e')
ax.bar(x, galleries, width=0.5, bottom=[i+j for i,j in zip(museums, theatres)], label='Galleries', color='#2ca02c')

plt.xlabel('Country')
plt.ylabel('Number of Venues')
plt.title('Number of arts and culture venues in four countries in 2021')
plt.xticks(x, country)
plt.legend(loc='upper right')

for i,j in zip(x,museums):
    ax.annotate(str(j), xy=(i,j+7))

for i,j in zip(x,theatres):
    ax.annotate(str(j), xy=(i,j+7))

for i,j in zip(x,galleries):
    ax.annotate(str(j), xy=(i,j+7))

plt.tight_layout()
plt.savefig('Bar Chart/png/119.png')
plt.clf()