
import matplotlib.pyplot as plt

x = ['Los Angeles','New York','Chicago','Miami']
price = [400000,450000,375000,420000]
rent = [2500,3200,2300,2800]

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()

ax.bar(x, price, width=0.4, bottom=0, color='b', label='Home Price')
ax.bar(x, rent, width=0.4, bottom=0, color='r', label='Rent')

plt.title('Average Home Prices and Rents in four major US Cities in 2021')
ax.set_xticklabels(x, rotation=45, ha='right')
plt.legend(loc='upper left')

plt.tight_layout()
plt.savefig('bar chart/png/349.png')
plt.clf()