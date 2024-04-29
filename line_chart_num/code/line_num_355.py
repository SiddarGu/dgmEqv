
import matplotlib.pyplot as plt
import numpy as np

data = [['France', 45, 36, 3],
        ['Germany', 50, 38, 4.5],
        ['Spain', 30, 25, 2.5],
        ['Italy', 35, 30, 3.5]]

country, visitors, revenue, profits = [],[],[],[]
for row in data:
    country.append(row[0])
    visitors.append(row[1])
    revenue.append(row[2])
    profits.append(row[3])
    
x = np.arange(len(country))

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot() 
ax.set_title('International tourism performance in 2021')
ax.set_xlabel('Country')
ax.set_xticks(x)
ax.set_xticklabels(country,rotation=45, ha='right', fontsize=14)
ax.set_ylabel('Performance')
ax.plot(x, visitors, label='Visitors (million)', color='#FF5733', linewidth=2)
ax.plot(x, revenue, label='Revenue (billion dollars)', color='#FFC300', linewidth=2)
ax.plot(x, profits, label='Profits (billion dollars)', color='#C70039', linewidth=2)
ax.legend(loc=1)

for a,b in zip(x,visitors):
    ax.annotate('%.2f'%b,xy=(a,b),xytext=(a,b+5))
for a,b in zip(x,revenue):
    ax.annotate('%.2f'%b,xy=(a,b),xytext=(a,b+5))
for a,b in zip(x,profits):
    ax.annotate('%.2f'%b,xy=(a,b),xytext=(a,b+5))

plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/528.png')
plt.clf()