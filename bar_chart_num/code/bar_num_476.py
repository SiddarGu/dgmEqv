
import matplotlib.pyplot as plt
import numpy as np

data = [['Facebook', 2.80, 12.50], ['Twitter', 0.86, 2.50], ['Instagram', 1.00, 3.00], ['YouTube', 2.00, 4.00]]

x = np.arange(len(data))

fig, ax = plt.subplots()
fig.set_size_inches(10, 6)
ax.bar(x, [i[1] for i in data], label='Users (million)', color='#FF9F80')
ax.bar(x, [i[2] for i in data], bottom=[i[1] for i in data], label='Sessions', color='#FF5F6D')
ax.set_xticks(x)
ax.set_xticklabels([i[0] for i in data])
ax.legend()
ax.set_title('Number of users and sessions on four social media platforms in 2021')

for i in x:
    plt.annotate(data[i][1], 
                 xy=(i, data[i][1]/2), 
                 xytext=(0, 10), 
                 textcoords="offset points", 
                 ha='center')
    plt.annotate(data[i][2], 
                 xy=(i, data[i][1]+data[i][2]/2), 
                 xytext=(0, 10), 
                 textcoords="offset points", 
                 ha='center')

plt.tight_layout()
plt.savefig('Bar Chart/png/135.png')
plt.cla()