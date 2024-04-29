
import matplotlib.pyplot as plt
import numpy as np

#Set initial parameters
fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(111)

#Define the data
labels = ['Air','Rail','Road']
distance = [2500,3000,3500]
speed = [800,400,300]
cost = [500,400,350]

#Plot with bar command
ax.bar(labels,distance,bottom=0,label='Distance (miles)',width=0.25)
ax.bar(labels,speed,bottom=distance,label='Speed (mph)',width=0.25)
ax.bar(labels,cost,bottom=[i+j for i,j in zip(distance,speed)],label='Cost',width=0.25)

#Set title and legend
plt.title('Cost, speed and distance of different transportation modes in 2021')
ax.legend(loc='upper left')

#Set the xticks
ax.set_xticks(np.arange(len(labels)))
ax.set_xticklabels(labels)

#Add annotations
for i,j in zip(distance,labels):
    ax.annotate(str(i),xy=(j,i/2))
for i,j in zip(speed,labels):
    ax.annotate(str(i),xy=(j,distance[labels.index(j)]+i/2))
for i,j in zip(cost,labels):
    ax.annotate(str(i),xy=(j,[sum(x) for x in zip(distance,speed)][labels.index(j)]+i/2))

fig.tight_layout()
plt.savefig('Bar Chart/png/426.png')
plt.clf()