
import matplotlib.pyplot as plt

x=[2001,2002,2003,2004,2005]
y1=[2000,2200,2500,3000,3500]
y2=[1000,1100,1500,2000,2500]

fig=plt.figure(figsize=(10,8))
ax=fig.add_subplot()

ax.plot(x,y1,label='Number of Scientific Papers Published',color='green',marker='o',markersize=10)
ax.plot(x,y2,label='Number of Patents Granted',color='red',marker='o',markersize=10)

plt.xticks(x)
plt.title('Trends of Scientific Publications and Patents Grants from 2001 to 2005')
plt.xlabel('Years')
plt.ylabel('Number of Publications/Grants')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/256.png')

plt.clf()