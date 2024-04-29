
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

age_group = ["18-24","25-34","35-44","45-54"]
movie_sales = [400,450,500,550]
concert_sales = [200,250,300,350]

rects1 = ax.bar(age_group, movie_sales, width=0.3, color='b', label='Movie Ticket Sales')
rects2 = ax.bar(age_group, concert_sales, width=0.3, color='g', label='Concert Ticket Sales', bottom=movie_sales)

plt.xticks(age_group)
ax.set_title('Ticket Sales of Movies and Concerts for Different Age Groups in 2021')
ax.legend()

for rects1, rects2 in zip(rects1, rects2):
    h1 = rects1.get_height()
    h2 = rects2.get_height()
    ax.text(rects1.get_x() + rects1.get_width()/2, h1/2, '%d' % int(h1), ha='center', va='bottom', fontsize=10)
    ax.text(rects2.get_x() + rects2.get_width()/2, h1+h2/2, '%d' % int(h2), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('Bar Chart/png/103.png')
plt.clf()