
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)

data = np.array([[500000,3000],[450000,2500],[400000,2000],[350000,1500]])
house_price = ax.bar(x,data[:,0],width=0.4,label='House Prices')
rent = ax.bar(x+0.4,data[:,1],width=0.4,label='Rent')

ax.set_xticks(x+0.2)
ax.set_xticklabels(('North','South','East','West'))
ax.set_title('Average house prices and rents in four regions in 2021')
ax.legend()

for house, rent in zip(house_price, rent):
    ax.annotate('$'+str(house.get_height()),
                xy=(house.get_x() + house.get_width() / 2, house.get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('$'+str(rent.get_height()),
                xy=(rent.get_x() + rent.get_width() / 2, rent.get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

fig.tight_layout()
plt.savefig('Bar Chart/png/556.png')
plt.clf()