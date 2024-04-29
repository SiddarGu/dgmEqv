
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

plt.figure(figsize=(10,8))

Country = ['USA','UK','Germany','France']
Sports_Events = [50,45,40,35]
Entertainment_Events = [75,80,85,90]

x = np.arange(len(Country))

ax = plt.subplot()
ax.bar(x-0.2, Sports_Events, width=0.4, bottom=0, color='#add8e6', label='Sports Events')
ax.bar(x+0.2, Entertainment_Events, width=0.4, bottom=0, color='#f08080', label='Entertainment Events')

ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.set_ylabel('Number of Events')
ax.set_title(' Number of Sports and Entertainment Events in Four Countries in 2021')
ax.legend(loc='best')

for i, v in enumerate(Sports_Events):
    ax.text(x[i] - 0.2, v + 0.5, str(v))
for i, v in enumerate(Entertainment_Events):
    ax.text(x[i] + 0.2, v + 0.5, str(v))

plt.tight_layout()
plt.savefig('Bar Chart/png/83.png')
plt.clf()