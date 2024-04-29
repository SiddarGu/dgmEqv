
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

Country = [ 'USA', 'UK', 'Germany', 'France' ]
Museums = [ 100, 110, 90, 120 ]
Galleries = [ 400, 450, 420, 480 ]
Theaters = [ 50, 60, 70, 80 ]

bar_width = 0.3

ax.bar(Country, Museums, width=bar_width, label='Museums')
ax.bar(Country, Galleries, width=bar_width, bottom=Museums, label='Galleries')
ax.bar(Country, Theaters, width=bar_width, bottom=[m+g for m,g in zip(Museums,Galleries)], label='Theaters')

ax.set_title('Number of Cultural Venues in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number of Venues')
ax.legend()
ax.set_xticks(Country)

for i, (m, g, t) in enumerate(zip(Museums, Galleries, Theaters)):
    ax.annotate('{}\n{}\n{}'.format(m, g, t),
                xy=(i, m+g+t/2),
                ha='center',
                va='center',
                wrap=True)

plt.tight_layout()
plt.savefig("Bar Chart/png/150.png")
plt.cla()