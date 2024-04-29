
import matplotlib.pyplot as plt 
import numpy as np 

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

Month = ['January','February','March','April','May','June']
ProA = [25,35,30,44,39,42]
ProB = [20,25,23,30,20,30]
ProC = [30,25,20,22,25,27]
ProD = [40,30,35,33,40,35]

ax.plot(Month, ProA, label = 'Production A', color ='red', marker ='o',linestyle='-')
ax.plot(Month, ProB, label = 'Production B', color ='orange', marker ='o',linestyle='-')
ax.plot(Month, ProC, label = 'Production C', color ='green', marker ='o',linestyle='-')
ax.plot(Month, ProD, label = 'Production D', color ='blue', marker ='o',linestyle='-')

plt.title('Monthly Production Output of Four Different Products in 2020')
plt.xlabel('Month')
plt.ylabel('Production(1000 items)')
plt.xticks(Month)
plt.legend(loc='upper left')
ax.grid(True)

for x,y in zip(Month,ProA):
    ax.annotate('(%s, %s)' % (x, y),xy=(x, y), xytext=(-3, 3), 
                textcoords='offset points', ha='right', va='bottom')

for x,y in zip(Month,ProB):
    ax.annotate('(%s, %s)' % (x, y),xy=(x, y), xytext=(-3, 3), 
                textcoords='offset points', ha='right', va='bottom')

for x,y in zip(Month,ProC):
    ax.annotate('(%s, %s)' % (x, y),xy=(x, y), xytext=(-3, 3), 
                textcoords='offset points', ha='right', va='bottom')

for x,y in zip(Month,ProD):
    ax.annotate('(%s, %s)' % (x, y),xy=(x, y), xytext=(-3, 3), 
                textcoords='offset points', ha='right', va='bottom')

plt.tight_layout()
plt.savefig('line chart/png/296.png')
plt.clf()