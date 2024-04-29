
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot()

region = np.array(['North America','Europe','Asia','South America'])
donors = np.array([500,400,800,300])
amount_donated = np.array([400000,450000,550000,300000])

bar1 = ax.bar(region,donors,bottom=0,label='Donors')
bar2 = ax.bar(region,amount_donated,bottom=donors,label='Amount Donated($)')

plt.title('Donors and Amount Donated to Nonprofit Organizations in Four Regions in 2021')
plt.xlabel('Region')
plt.ylabel('Number of Donors/Amount Donated ($))')
plt.xticks(rotation=45,ha='right')
plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig('bar chart/png/459.png')
plt.clf()