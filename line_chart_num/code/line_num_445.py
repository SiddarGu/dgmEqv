

import matplotlib.pyplot as plt

x = [2001, 2002, 2003, 2004]
y1 = [2.5, 2.6, 2.8, 2.7]
y2 = [1.2, 1.4, 1.5, 1.6]
y3 = [2.3, 2.2, 2.4, 2.7]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.plot(x, y1, label='Coffee Consumption')
ax.plot(x, y2, label='Tea Consumption')
ax.plot(x, y3, label='Milk Consumption')

for a,b,c in zip(x, y1,y2):
    ax.annotate(str(b), xy=(a,b), xytext=(a-0.3, b+0.2), fontsize=12)
    ax.annotate(str(c), xy=(a,c), xytext=(a-0.3, c+0.2), fontsize=12)

ax.set_xticks(x)
ax.set_title('Beverage Consumption Trend in the United States from 2001 to 2004')
ax.set_xlabel('Year')
ax.set_ylabel('Kg/capita')

plt.legend(loc='best', fontsize=12)
plt.tight_layout()
plt.savefig('line chart/png/78.png')
plt.clf()