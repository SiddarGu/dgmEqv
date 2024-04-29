
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()

region = ['East Coast','West Coast','Midwest','South']
price = [400,500,300,350]
number = [200,250,150,100]

x = np.arange(len(region))

ax.bar(x,price,label='Average Home Price(thousand $)',width=0.35,bottom=0)
ax.bar(x,number,label='Number of Homes Sold',width=0.35,bottom=price)

ax.set_xticks(x)
ax.set_xticklabels(region)
ax.set_title('Average Home Price and Number of Homes Sold by Region in 2021')

for i,j in zip(x,price):
    ax.annotate(str(j), xy=(i, j), xytext=(0,3), textcoords="offset points", ha='center', va='bottom')

for i,j in zip(x,number):
    ax.annotate(str(j), xy=(i, j+price[i]), xytext=(0,3), textcoords="offset points", ha='center', va='bottom')

ax.legend()
plt.tight_layout()
plt.savefig('bar_58.png')
plt.clf()