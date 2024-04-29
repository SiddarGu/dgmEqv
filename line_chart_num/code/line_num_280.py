
import matplotlib.pyplot as plt
import numpy as np

data = [[2001,78,3,2],[2002,79,2,1],[2003,80,1,3],[2004,81,2,4]]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()

x = np.array(data)[:,0]
y1 = np.array(data)[:,1]
y2 = np.array(data)[:,2]
y3 = np.array(data)[:,3]

ax.plot(x,y1,label='Employment Rate (%)', color='blue', marker='o')
ax.plot(x,y2,label='Unemployment Rate (%)', color='red', marker='o')
ax.plot(x,y3,label='Inflation Rate (%)', color='green', marker='o')

for i,j in zip(x,y1):
    ax.annotate(str(j),xy=(i,j), rotation=45)
for i,j in zip(x,y2):
    ax.annotate(str(j),xy=(i,j), rotation=45)
for i,j in zip(x,y3):
    ax.annotate(str(j),xy=(i,j), rotation=45)

ax.set_title('Employment and Inflation Rate Changes in the US Economy from 2001-2004', fontsize=20)
ax.legend(loc='best')
ax.set_xticks(x)
plt.tight_layout()
plt.savefig('line chart/png/572.png')
plt.clf()