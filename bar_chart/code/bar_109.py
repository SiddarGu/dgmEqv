
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(6,5))
ax = fig.add_subplot(1,1,1)

data = [[50,350],[60,400],[70,450],[80,500]]
ax.bar(np.arange(len(data)),[i[0] for i in data],label = 'Football Teams',width=0.35,bottom=[i[1] for i in data])
ax.bar(np.arange(len(data))+0.35,[i[1] for i in data],label = 'Cinemas',width=0.35)
ax.set_xticks(np.arange(len(data))+0.35/2)
ax.set_xticklabels(['USA','UK','Germany','France'])
ax.set_xlabel('Country')
ax.set_ylabel('Number')
ax.legend()
ax.set_title('Number of football teams and cinemas in four countries in 2021')
plt.xticks(rotation = 45, va="top", ha="right", wrap=True)
plt.tight_layout()
plt.savefig('bar chart/png/330.png')
plt.clf()