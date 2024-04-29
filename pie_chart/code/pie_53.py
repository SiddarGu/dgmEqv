
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.figure(figsize=(8,8))
ax = plt.subplot()
labels = 'Energy','Manufacturing','Technology','Aerospace','Automotive','Utilities','Construction'
sizes = [20,15,30,15,10,5,5]
explode = (0.1,0,0,0,0,0,0)
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.set_title('Distribution of Science and Engineering Jobs in the USA, 2023')
ax.axis('equal')
ax.legend(bbox_to_anchor=(1.1, 0.8))
ax.xaxis.set_major_locator(ticker.NullLocator())
ax.yaxis.set_major_locator(ticker.NullLocator())
plt.tight_layout()
plt.savefig('pie chart/png/145.png', bbox_inches='tight')
plt.cla()