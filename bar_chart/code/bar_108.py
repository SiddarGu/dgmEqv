
import matplotlib.pyplot as plt 
import numpy as np

data = np.array([[20000, 50000],
                 [25000, 45000],
                 [18000, 40000],
                 [23000, 47000]])

labels = ['USA', 'UK', 'Germany', 'France']

sport_fans = data[:, 0]
tv_viewers = data[:, 1]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.bar(labels, sport_fans, bottom=0, label='Sports Fans', width=0.4)
ax.bar(labels, tv_viewers, bottom=sport_fans, label='TV Viewers', width=0.4)

ax.set_title('Number of Sports Fans and TV Viewers in Four Countries in 2021')
ax.set_ylabel('Number of People')
ax.legend(loc='upper left')
ax.grid(True, linestyle='--', color='grey', linewidth=1)
plt.xticks(rotation=45) 
plt.tight_layout() 
plt.savefig('bar chart/png/396.png')
plt.clf()