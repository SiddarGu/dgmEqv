
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2001,400,50,5],
                 [2002,500,55,4],
                 [2003,450,60,3],
                 [2004,550,65,2],
                 [2005,500,70,1]])

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1)
ax.plot(data[:,0],data[:,1], color='r', label='Average Home Price(thousand dollars)')
ax.plot(data[:,0],data[:,2], color='b', label='Average Rent Price(thousand dollars)')
ax.plot(data[:,0],data[:,3], color='g', label='Vacancy Rate')
ax.legend(loc='best')
ax.set_title('Average Housing Market Prices and Vacancy Rate in the U.S.')
ax.set_xlabel('Year')
ax.set_ylabel('Price/Rate')
ax.grid(True)
ax.set_xticks(data[:,0])

for i in range(data.shape[0]):
    ax.annotate('{}'.format(data[i,1]),xy=(data[i,0],data[i,1]))
    ax.annotate('{}'.format(data[i,2]),xy=(data[i,0],data[i,2]))
    ax.annotate('{}'.format(data[i,3]),xy=(data[i,0],data[i,3]))

plt.tight_layout()
plt.savefig('line chart/png/293.png')
plt.clf()