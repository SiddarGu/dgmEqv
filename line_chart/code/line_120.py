
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3,4,5,6])
y1 = np.array([100,90,95,105,110,95,100])
y2 = np.array([80,70,75,85,75,80,85])
y3 = np.array([120,130,125,115,105,110,115])

fig = plt.figure( figsize=(12, 6))
ax = fig.add_subplot(111)
ax.plot(x, y1, '-s', label='Speed A(Mbps)')
ax.plot(x, y2, '-o', label='Speed B(Mbps)')
ax.plot(x, y3, '-^', label='Speed C(Mbps)')
ax.set_xticks(x)
plt.title('Internet connection speed changes in a sample city over 6 hours on March 20, 2021')
plt.xlabel('Time')
plt.ylabel('Speed')
plt.grid(True)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/547.png')
plt.clf()