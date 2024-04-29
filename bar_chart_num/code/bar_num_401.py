
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA','UK','Germany','France']
Online_Shopping = [80, 70, 75, 60]
Offline_Shopping = [20, 30, 25, 40]

fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot()
ax.bar(Country, Online_Shopping, width = 0.6, color='#2F4F4F', bottom=Offline_Shopping, label='Online Shopping')
ax.bar(Country, Offline_Shopping, width = 0.6, color='#696969', label='Offline Shopping')

plt.title('Percentage of Online and Offline Shopping in four countries in 2021')
ax.set_xticks(Country)
ax.set_xticklabels(Country, rotation=45)
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

for x, y1, y2 in zip(Country, Online_Shopping, Offline_Shopping):
    ax.annotate('{}%'.format(y1), xy=(x, y1/2 + y2/2), ha='center')
    ax.annotate('{}%'.format(y2), xy=(x, y2/2), ha='center')

plt.tight_layout()
plt.savefig('Bar Chart/png/289.png')
plt.clf()