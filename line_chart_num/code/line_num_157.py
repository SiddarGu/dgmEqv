
import matplotlib.pyplot as plt
import numpy as np

x = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
views = [200, 220, 250, 280, 310, 340, 370]
likes = [50, 55, 60, 65, 70, 75, 80]
shares = [10, 12, 15, 20, 25, 30, 35]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

ax.plot(x, views, marker='o', label='Views')
ax.plot(x, likes, marker='^', label='Likes')
ax.plot(x, shares, marker='*', label='Shares')

ax.set_xticks(x)
ax.set_ylim(0, 400)
ax.set_title('Social Media Engagement of Artworks in 2021')
ax.legend(loc='best')

for i, v in enumerate(views):
    ax.text(i, v + 5, str(v), ha='center', fontsize=10)
for i, l in enumerate(likes):
    ax.text(i, l + 5, str(l), ha='center', fontsize=10)
for i, s in enumerate(shares):
    ax.text(i, s + 5, str(s), ha='center', fontsize=10)

plt.tight_layout()
plt.savefig('line chart/png/53.png')
plt.clf()