
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
country = ['USA','UK','Germany','France']
theatre_performances = [50,60,55,45]
concerts = [200,220,180,210]
exhibitions = [150,170,130,150]

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)
ax.bar(x-0.2, theatre_performances, width=0.2, color='b', label='Theater Performances')
ax.bar(x, concerts, width=0.2, color='g', label='Concerts')
ax.bar(x+0.2, exhibitions, width=0.2, color='r', label='Exhibitions')
plt.xticks(x,country)
plt.title('Number of theater performances, concerts and exhibitions in four countries in 2021')
plt.legend()

ax.annotate('%d' % theatre_performances[0], xy=(x[0]-0.2, theatre_performances[0]+1))
ax.annotate('%d' % theatre_performances[1], xy=(x[1]-0.2, theatre_performances[1]+1))
ax.annotate('%d' % theatre_performances[2], xy=(x[2]-0.2, theatre_performances[2]+1))
ax.annotate('%d' % theatre_performances[3], xy=(x[3]-0.2, theatre_performances[3]+1))
ax.annotate('%d' % concerts[0], xy=(x[0], concerts[0]+1))
ax.annotate('%d' % concerts[1], xy=(x[1], concerts[1]+1))
ax.annotate('%d' % concerts[2], xy=(x[2], concerts[2]+1))
ax.annotate('%d' % concerts[3], xy=(x[3], concerts[3]+1))
ax.annotate('%d' % exhibitions[0], xy=(x[0]+0.2, exhibitions[0]+1))
ax.annotate('%d' % exhibitions[1], xy=(x[1]+0.2, exhibitions[1]+1))
ax.annotate('%d' % exhibitions[2], xy=(x[2]+0.2, exhibitions[2]+1))
ax.annotate('%d' % exhibitions[3], xy=(x[3]+0.2, exhibitions[3]+1))

plt.tight_layout()
plt.savefig('Bar Chart/png/624.png')
plt.clf()