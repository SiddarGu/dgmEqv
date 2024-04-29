
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot()

x = np.arange(5)
ax.plot(x, [100,90,85,75,70], label='Classical Music', marker='o')
ax.plot(x, [90,80,75,65,55], label='Rock Music', marker='o')
ax.plot(x, [80,75,60,50,45], label='Country Music', marker='o')

ax.set_xticks(x)
ax.set_xticklabels(('2001', '2002', '2003', '2004', '2005'))
ax.set_title('Music Albums Sales in the US from 2001 to 2005')
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/315.png')
plt.clf()