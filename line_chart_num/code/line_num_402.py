
import matplotlib.pyplot as plt 

year = [2019, 2020, 2021, 2022]
movie_tickets = [800,900,1000,1100]
concert_tickets = [600,700,900,1000]
sports_tickets = [400,500,600,700]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.plot(year, movie_tickets, label='Movie Tickets', marker='o', color='red')
ax.plot(year, concert_tickets, label='Concert Tickets', marker='o', color='blue')
ax.plot(year, sports_tickets, label='Sports Tickets', marker='o', color='green')

ax.set_title('Entertainment and Sports Ticket Sales in the US from 2019 to 2022')
ax.set_xlabel('Year')
ax.set_ylabel('Tickets (million)')

ax.set_xticks(year)
ax.legend()

for a,b,c,d in zip(year, movie_tickets, concert_tickets, sports_tickets):
    ax.annotate('movie={}'.format(b), xy = (a,b), xytext=(a+0.1, b-20) )
    ax.annotate('concert={}'.format(c), xy = (a,c), xytext=(a+0.1, c-20) )
    ax.annotate('sports={}'.format(d), xy = (a,d), xytext=(a+0.1, d-20) )

plt.tight_layout()
plt.savefig('line chart/png/226.png')
plt.clf()