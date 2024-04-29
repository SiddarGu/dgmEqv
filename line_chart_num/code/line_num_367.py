
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2011, 2012, 2013, 2014, 2015])
Desktop_Users = np.array([100, 120, 150, 200, 250])
Mobile_Users = np.array([50, 60, 80, 100, 120])
Tablet_Users = np.array([20, 30, 40, 50, 60])

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

ax.plot(x, Desktop_Users, label='Desktop Users(million)', color='green', marker='o', linestyle='--', linewidth=2, markersize=6)
ax.plot(x, Mobile_Users, label='Mobile Users(million)', color='blue', marker='^', linestyle='-', linewidth=2, markersize=6)
ax.plot(x, Tablet_Users, label='Tablet Users(million)', color='red', marker='s', linestyle='-.', linewidth=2, markersize=6)

plt.title('Global Internet Users from 2011 to 2015', fontsize=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Users(million)', fontsize=12)

plt.xticks(x)
plt.legend(loc='best')

for a,b,c in zip(x,Desktop_Users,Mobile_Users):
    ax.annotate(str(b)+','+str(c),xy=(a,b),rotation=45,va="bottom",ha="center",fontsize=10)

for a,b,c in zip(x,Desktop_Users,Tablet_Users):
    ax.annotate(str(b)+','+str(c),xy=(a,b),rotation=45,va="top",ha="center",fontsize=10)

for a,b,c in zip(x,Mobile_Users,Tablet_Users):
    ax.annotate(str(b)+','+str(c),xy=(a,b),rotation=45,va="bottom",ha="center",fontsize=10)

plt.tight_layout()
plt.savefig('line chart/png/467.png')
plt.clf()