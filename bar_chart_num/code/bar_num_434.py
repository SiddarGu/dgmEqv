
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
ax=fig.add_subplot()

data=np.array([[50,20,30],[60,25,40],[75,30,45],[90,35,50]])

periods=np.array(['1900-1910','1910-1920','1920-1930','1930-1940'])
disciplines=np.array(['Economics','Psychology','Sociology'])

ax.bar(periods,data[:,0],label=disciplines[0],bottom=data[:,1]+data[:,2])
ax.bar(periods,data[:,1],label=disciplines[1],bottom=data[:,2])
ax.bar(periods,data[:,2],label=disciplines[2])

for x,y,v in zip(periods,data.sum(axis=1),data):
    ax.annotate(str(v[0]),xy=(x,y-v[0]/2))
    ax.annotate(str(v[1]),xy=(x,y-v[0]-v[1]/2))
    ax.annotate(str(v[2]),xy=(x,y-v[0]-v[1]-v[2]/2))

ax.set_xticks(periods)
ax.legend()
ax.set_title('Number of scientific papers published in social sciences and humanities from 1900 to 1940')

fig.tight_layout()
plt.savefig('Bar Chart/png/313.png')
plt.clf()