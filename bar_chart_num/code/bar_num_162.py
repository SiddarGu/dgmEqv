
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()
ax.set_title('Revenue and Expenses of four types of businesses in 2021')
types = ['Restaurant','Retail','Technology','Service']
revenues = [800,1200,1500,900]
expenses = [600,1000,1200,800]
ax.bar(types, revenues, label='Revenue')
ax.bar(types, expenses, label='Expenses', bottom=revenues)
ax.set_xticks(types)
ax.legend(loc='upper left')

for i, j in zip(types,revenues):
    ax.annotate('{}M'.format(j), xy=(i, j/2), horizontalalignment='center',verticalalignment='center')
for i, j in zip(types,expenses):
    ax.annotate('{}M'.format(j), xy=(i, j/2+j), horizontalalignment='center',verticalalignment='center')
plt.tight_layout()
plt.savefig('Bar Chart/png/33.png')
plt.clf()