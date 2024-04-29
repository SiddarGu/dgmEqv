
import matplotlib.pyplot as plt
import numpy as np

data = np.array([['USA', 100, 97, 104], 
                 ['UK', 102, 95, 103], 
                 ['Germany', 98, 94, 101], 
                 ['France', 101, 96, 105]])

fig, ax = plt.subplots(figsize=(12,8))
x_pos = np.arange(len(data[:,0]))

ax.bar(x_pos-0.2, data[:,1], width=0.2, label='Manufacturing Index', color='b')
ax.bar(x_pos, data[:,2], width=0.2, label='Consumer Index', color='g')
ax.bar(x_pos+0.2, data[:,3], width=0.2, label='Service Index', color='r')

ax.set_xticks(x_pos)
ax.set_xticklabels(data[:,0])
ax.set_title('Manufacturing, Consumer and Service Index in four countries 2021')
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('bar chart/png/195.png')
plt.clf()