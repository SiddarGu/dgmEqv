
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(1, 1, 1)
country = ['US', 'UK', 'France']
movies_released = [200, 150, 100]
musical_albums_released = [100, 80, 60]
books_published = [500, 250, 150]
art_exhibitions = [50, 30, 20]

ax.plot(country, movies_released, label='Movies Released')
ax.plot(country, musical_albums_released, label='Musical Albums Released')
ax.plot(country, books_published, label='Books Published')
ax.plot(country, art_exhibitions, label='Art Exhibitions')

ax.set_title('Cultural Output in the US, UK, and France in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number of Releases')
ax.xaxis.set_major_locator(ticker.FixedLocator(range(len(country))))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(country))
ax.grid(True)
ax.legend(loc='best', ncol=2, fontsize='small', framealpha=0.5, fancybox=True)

plt.tight_layout()
plt.savefig('line chart/png/73.png')
plt.clf()