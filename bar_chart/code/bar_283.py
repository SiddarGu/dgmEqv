
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot()
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston']
home = [500000, 400000, 350000, 300000]
rent = [3000, 3500, 2500, 2000]

ax.bar(cities,home, width=0.5,label='Average Home Price',color='#f8c471')
ax.bar(cities,rent,bottom=home, width=0.5,label='Average Rent Price',color='#f1948a')
ax.set_title('Average Home and Rent Prices in four major US Cities in 2021')
ax.set_xticklabels(cities,rotation=30,ha='right',wrap=True)
ax.set_ylabel('Price')
ax.legend(loc='upper center')
plt.tight_layout()
plt.savefig('bar chart/png/298.png')
plt.clf()