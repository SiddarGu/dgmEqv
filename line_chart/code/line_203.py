

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

x = [2013, 2014, 2015, 2016, 2017, 2018]
y1 = [1000, 1500, 2000, 2500, 3000, 4000]
y2 = [500, 800, 1200, 1600, 2000, 2500]
y3 = [100, 200, 400, 800, 1200, 1600]

ax.plot(x, y1, label='Facebook Users')
ax.plot(x, y2, label='Twitter Users')
ax.plot(x, y3, label='Instagram Users')

plt.xticks(x)
plt.title('Growth of Social Media Users from 2013 to 2018')
plt.xlabel('Year')
plt.ylabel('Number of Users')
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)
plt.tight_layout()
plt.savefig('line chart/png/113.png')
plt.clf()