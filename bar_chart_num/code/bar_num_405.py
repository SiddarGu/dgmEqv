
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {'Country':['USA', 'UK', 'Germany', 'France'],
        'Museums':[50, 30, 60, 40],
        'Galleries':[70, 60, 50, 90],
        'Theaters':[80, 40, 70, 60]}

df = pd.DataFrame(data)

x = np.arange(len(df))
width = 0.2

fig = plt.figure()
ax = fig.add_subplot()

ax.bar(x-width, df['Museums'], width=width, label='Museums', color='b')
ax.bar(x, df['Galleries'], width=width, label='Galleries', color='r')
ax.bar(x+width, df['Theaters'], width=width, label='Theaters', color='g')

ax.set_ylabel('Number')
ax.set_title('Number of museums, galleries, and theaters in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(df['Country'])
ax.legend()

for x1, y1 in zip(x, df['Museums']):
    ax.annotate('{}'.format(y1), xy=(x1-width, y1+1), xycoords='data', ha='center', va='bottom')

for x2, y2 in zip(x, df['Galleries']):
    ax.annotate('{}'.format(y2), xy=(x2, y2+1), xycoords='data', ha='center', va='bottom')

for x3, y3 in zip(x, df['Theaters']):
    ax.annotate('{}'.format(y3), xy=(x3+width, y3+1), xycoords='data', ha='center', va='bottom')

fig.tight_layout()
plt.savefig('Bar Chart/png/223.png') 
plt.clf()