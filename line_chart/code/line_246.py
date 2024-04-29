
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2011,2012,2013,2014,2015])
y1 = np.array([10,15,20,30,40])
y2 = np.array([20,25,30,35,40])
y3 = np.array([5,10,15,20,30])

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.plot(x,y1,label="Computer Usage(percentage)")
ax.plot(x,y2,label="Smartphone Usage(percentage)")
ax.plot(x,y3,label="Tablet Usage(percentage)")

ax.set_title('Technology usage trend from 2011 to 2015')
ax.set_xlabel('Year')
ax.set_ylabel('Usage(percentage)')
plt.xticks(x)
plt.legend(bbox_to_anchor=(1.0,1.0))

plt.tight_layout()
plt.savefig('line chart/png/482.png')
plt.clf()