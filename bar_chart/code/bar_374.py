
import matplotlib.pyplot as plt 
import numpy as np 

data = [[2019,40,30,35],
        [2020,42,31,38],
        [2021,44,32,40]]

x = np.arange(len(data))

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)
ax.bar(x-0.2, [i[1] for i in data], width=0.2, label='Philosophy(%)', color='b')
ax.bar(x, [i[2] for i in data], width=0.2, label='Psychology(%)', color='r')
ax.bar(x+0.2, [i[3] for i in data], width=0.2, label='Sociology(%)', color='y')

ax.set_xticks(x)
ax.set_xticklabels([i[0] for i in data], rotation=0, wrap=True)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_title('Percentage of Social Sciences and Humanities in three fields from 2019 to 2021')
plt.tight_layout()
plt.savefig('bar chart/png/133.png')
plt.clf()