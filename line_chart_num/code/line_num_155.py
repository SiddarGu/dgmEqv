
import matplotlib.pyplot as plt
import numpy as np

data = [[2000,2000000,10000,25000], [2005,2200000,12000,30000], [2010,2500000,15000,35000], [2015,3000000,20000,40000], [2020,3300000,22000,45000]]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

ax.plot(data[0][0], data[0][1], label="Home Prices")
ax.plot(data[0][0], data[0][2], label="Rental Prices")
ax.plot(data[0][0], data[0][3], label="Households")

ax.set_title("Changes in Home Prices, Rental Prices, and Number of Households in the US from 2000 to 2020")
ax.set_xlabel("Year")
ax.set_ylabel("Average Price (dollars)")

ax.legend(loc="best")
ax.grid(True)

ax.annotate("Home Prices: $2,000,000", xy=(2000, 2000000))
ax.annotate("Rental Prices: $10,000", xy=(2000, 10000))
ax.annotate("Households: 25,000", xy=(2000, 25000))

ax.annotate("Home Prices: $3,300,000", xy=(2020, 3300000))
ax.annotate("Rental Prices: $22,000", xy=(2020, 22000))
ax.annotate("Households: 45,000", xy=(2020, 45000))

plt.xticks(np.arange(2000, 2021, 5))

fig.tight_layout()
fig.savefig("line chart/png/20.png")
plt.clf()