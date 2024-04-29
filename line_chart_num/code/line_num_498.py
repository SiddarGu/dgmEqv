
import matplotlib.pyplot as plt
import numpy as np

data = [[2010, 80, 20, 30], [2011, 90, 25, 35], [2012, 100, 30, 40], [2013, 110, 35, 45], [2014, 120, 40, 50], [2015, 130, 45, 55]]
x = [i[0] for i in data]
y1 = [i[1] for i in data]
y2 = [i[2] for i in data]
y3 = [i[3] for i in data]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.plot(x, y1, color='#FF0000', linestyle='--', marker='.', label='Number of Users A (million)')
ax.plot(x, y2, color='#0000FF', linestyle='--', marker='.', label='Number of Users B (million)')
ax.plot(x, y3, color='#00FF00', linestyle='--', marker='.', label='Number of Users C (million)')

ax.legend(loc='upper left')
ax.set_title('Growth of users on three major social media platforms from 2010 to 2015')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Users (million)')
ax.grid(True)
ax.set_xticks(x)

for x, y1, y2, y3 in zip(x, y1, y2, y3):
    ax.annotate(str(y1), xy=(x, y1), xytext=(-3, 3), textcoords="offset points", fontsize=10, color='#FF0000')
    ax.annotate(str(y2), xy=(x, y2), xytext=(-3, 3), textcoords="offset points", fontsize=10, color='#0000FF')
    ax.annotate(str(y3), xy=(x, y3), xytext=(-3, 3), textcoords="offset points", fontsize=10, color='#00FF00')

plt.tight_layout()
plt.savefig(r'line chart/png/334.png', dpi=400)
plt.clf()