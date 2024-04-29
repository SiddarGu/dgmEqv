
import matplotlib.pyplot as plt
import numpy as np

data = [['Drama',150,3000],['Music',200,4000],['Dance',100,2500],['Opera',90,2000]]
x = np.arange(len(data))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()
ax.bar(x - 0.2, [i[1] for i in data], width=0.2, color='b', label='Performance')
ax.bar(x, [i[2] for i in data], width=0.2, color='r', label='Attendees')
ax.set_xticks(x) 
ax.set_xticklabels([i[0] for i in data], fontsize=12)
ax.set_title('Number of Performances and Attendees in Arts and Culture in 2021')
ax.legend(loc='upper left')
for i in range(len(data)):
    ax.annotate(data[i][1], xy=(x[i] - 0.2, data[i][1] + 50), fontsize=12)
    ax.annotate(data[i][2], xy=(x[i], data[i][2] + 50), fontsize=12)
fig.tight_layout()
plt.savefig('Bar Chart/png/546.png')
plt.clf()