
import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4])
y1=np.array([1000,500,4000,200])
y2=np.array([8,7,9,6])

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(1,1,1)

ax.plot(x,y1,color='r',linewidth=3,label='Cost')
ax.plot(x,y2,color='b',linewidth=3,label='Safety Rating')
ax.set_xticks(x)
ax.set_xticklabels(['Train','Bus','Plane','Car'])
ax.set_xlabel('Mode of Transportation',fontsize=14)
ax.set_ylabel('Cost and Safety Rating',fontsize=14)
ax.set_title('Comparison of Safety Ratings and Costs of Different Modes of Transportation')

for x,y1,y2 in zip(x,y1,y2):
    ax.annotate('${}'.format(y1), xy=(x,y1), xytext=(-5,5), textcoords='offset points')
    ax.annotate('$%s'%y2, xy=(x,y2), xytext=(-5,5), textcoords='offset points')

plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/570.png')

plt.clf()