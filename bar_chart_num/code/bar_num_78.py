
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot()

sports = ['Soccer','Basketball','Baseball','Tennis']
tickets_sold = [500,400,300,200]
viewers = [10,12,8,7]

bar_width = 0.5
x = range(len(sports))
ax.bar(x, tickets_sold, width=bar_width, label='Tickets Sold')
ax.bar(x, viewers, width=bar_width, bottom=tickets_sold, label='Viewers(million)')

plt.xticks(x, sports)
plt.legend(loc='upper left')

for i in range(len(x)):
    ax.annotate(str(tickets_sold[i]), xy=(x[i], tickets_sold[i]/2))
    ax.annotate(str(viewers[i]), xy=(x[i], tickets_sold[i]+viewers[i]/2))

plt.title('Number of tickets sold and viewers of four sports in 2021')
plt.tight_layout()
plt.savefig('Bar Chart/png/462.png')

plt.clf()