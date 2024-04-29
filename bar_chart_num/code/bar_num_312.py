
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

region = ['North', 'South', 'East', 'West']
Average_Price = [500, 450, 600, 550]
Average_Rental_Price = [800, 750, 850, 900]

ax.bar(region, Average_Price, width=0.3, color='red', bottom=Average_Rental_Price, label='Average_Price')
ax.bar(region, Average_Rental_Price, width=0.3, color='blue', label='Average_Rental_Price')

plt.title('Average real estate and rental prices in four regions in 2021', fontsize=15)
plt.xticks(region)
plt.legend(loc='upper center')

for i in range(len(region)):
    ax.annotate(Average_Price[i], xy=(i, Average_Price[i]), xytext=(i, Average_Price[i]), fontsize=12)
    ax.annotate(Average_Rental_Price[i], xy=(i, Average_Rental_Price[i]), xytext=(i, Average_Rental_Price[i]), fontsize=12)

plt.tight_layout()
plt.savefig('Bar Chart/png/23.png')
plt.clf()