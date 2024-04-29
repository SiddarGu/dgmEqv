
import matplotlib.pyplot as plt
import numpy as np

data = [['00:00', 1000, 1200, 900], ['01:00', 1100, 1300, 1000], ['02:00', 1300, 1200, 1100], 
        ['03:00', 1200, 1000, 800], ['04:00', 1500, 1100, 1300], ['05:00', 1300, 900, 1200]]

time = [row[0] for row in data]
tweets = [row[1] for row in data]
fb_posts = [row[2] for row in data]
insta_posts = [row[3] for row in data]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.plot(time, tweets, label='Tweets')
ax.plot(time, fb_posts, label='Facebook Posts')
ax.plot(time, insta_posts, label='Instagram Posts')

ax.set_title('Social Media Activity in the First Five Hours of May 15, 2021')
ax.set_xlabel('Time')
ax.set_ylabel('Number of Posts')
plt.xticks(time, rotation=90)
ax.legend(loc='upper left', bbox_to_anchor=(0, 1))
plt.grid(linestyle='--')

plt.tight_layout()
plt.savefig('line chart/png/188.png')
plt.clf()