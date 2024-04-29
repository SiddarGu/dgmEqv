
import matplotlib.pyplot as plt
plt.figure(figsize=(15,10))
ax = plt.subplot(111)
year=[2015,2016,2017,2018,2019,2020]
movie=[1000,1200,1400,1600,1800,2000]
game=[500,600,700,800,900,1000]
ax.plot(year,movie,label="Movie Revenue(million dollars)")
ax.plot(year,game,label="Game Revenue(million dollars)")
ax.annotate("{}".format(movie[0]),xy=(2015,1000))
ax.annotate("{}".format(movie[1]),xy=(2016,1200))
ax.annotate("{}".format(movie[2]),xy=(2017,1400))
ax.annotate("{}".format(movie[3]),xy=(2018,1600))
ax.annotate("{}".format(movie[4]),xy=(2019,1800))
ax.annotate("{}".format(movie[5]),xy=(2020,2000))
ax.annotate("{}".format(game[0]),xy=(2015,500))
ax.annotate("{}".format(game[1]),xy=(2016,600))
ax.annotate("{}".format(game[2]),xy=(2017,700))
ax.annotate("{}".format(game[3]),xy=(2018,800))
ax.annotate("{}".format(game[4]),xy=(2019,900))
ax.annotate("{}".format(game[5]),xy=(2020,1000))
ax.set_xticks(year)
plt.title("Revenue from movies and video games in the entertainment industry from 2015 to 2020")
ax.legend(loc=2)
plt.tight_layout()
plt.savefig("line chart/png/397.png")
plt.clf()