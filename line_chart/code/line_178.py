
import matplotlib.pyplot as plt
import numpy as np

data = [[2014,150,15],
        [2015,170,18],
        [2016,190,20],
        [2017,210,22],
        [2018,230,25]]

x = [i[0] for i in data]
house_price = [i[1] for i in data]
rent = [i[2] for i in data]

plt.figure(figsize=(12,8))
ax = plt.subplot()
ax.plot(x, house_price, label='Average House Price (thousands of dollars)', color='red', linestyle='--', marker='s')
ax.plot(x, rent, label='Average Rent (hundreds of dollars)', color='blue', linestyle='-.', marker='o')
ax.legend(loc='best')
plt.xticks(x)
plt.title('Average Home Prices and Rents in the United States from 2014-2018', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.tight_layout()
plt.savefig('line chart/png/242.png')
plt.clf()