
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

data = [[400, 220, 150, 210], [550, 370, 280, 320]]
countries = ['USA', 'UK', 'Germany', 'France']
pos = np.arange(len(countries))
ax.set_xticks(pos)
ax.set_xticklabels(countries, rotation=45, wrap=True)

ax.bar(pos - 0.2, data[0], width=0.4, label='Internet Users (million)')
ax.bar(pos + 0.2, data[1], width=0.4, label='Mobile Phone Users (million)')

plt.title('Number of Internet and Mobile Phone Users in Four Countries in 2021')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('bar chart/png/227.png')
plt.clf()