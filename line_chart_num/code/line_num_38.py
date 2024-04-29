

import matplotlib.pyplot as plt
import numpy as np

# Generate data
data = [[2011,100,800,0,200],
        [2012,150,1000,10,300],
        [2013,200,1200,30,400],
        [2014,250,1400,50,500],
        [2015,300,1600,70,600],
        [2016,350,1800,90,700],
        [2017,400,2000,110,800],
        [2018,450,2200,130,900]]

data = np.array(data)
year = data[:, 0]
twitter_users = data[:, 1]
facebook_users = data[:, 2]
instagram_users = data[:, 3]
youtube_users = data[:, 4]

# Plot figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.plot(year, twitter_users, label='Twitter', marker='.')
ax.plot(year, facebook_users, label='Facebook', marker='.')
ax.plot(year, instagram_users, label='Instagram', marker='.')
ax.plot(year, youtube_users, label='YouTube', marker='.')
plt.xticks(year, rotation=45)
plt.title("Global Social Media user growth from 2011 to 2018")
plt.xlabel("Year")
plt.ylabel("User (million)")
ax.legend(loc='upper left')

for a, b in zip(year, twitter_users): 
    ax.annotate('{}'.format(b), xy=(a, b), xytext=(a-0.2, b+3))
for a, b in zip(year, facebook_users): 
    ax.annotate('{}'.format(b), xy=(a, b), xytext=(a-0.2, b+20))
for a, b in zip(year, instagram_users): 
    ax.annotate('{}'.format(b), xy=(a, b), xytext=(a-0.2, b+3))
for a, b in zip(year, youtube_users): 
    ax.annotate('{}'.format(b), xy=(a, b), xytext=(a-0.2, b+3))

plt.tight_layout()
plt.savefig('line chart/png/315.png')
plt.clf()