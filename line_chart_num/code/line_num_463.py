
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017])
median_price = np.array([200000, 210000, 220000, 240000, 260000, 280000, 300000, 320000])
income_per_capita = np.array([50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000])

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111)

ax.plot(x, median_price, color="red", marker="o", label="Median Home Price")
ax.plot(x, income_per_capita, color="blue", marker="o", label="Income per capita")
for i, txt in enumerate(median_price):
    ax.annotate(txt, (x[i], median_price[i]))
for i, txt in enumerate(income_per_capita):
    ax.annotate(txt, (x[i], income_per_capita[i]))

ax.set_xticks(x)
ax.set_title("Home Prices and Income per capita in the US from 2010 to 2017")
ax.set_xlabel("Year")
ax.set_ylabel("Price and Income")
ax.legend(loc="best")

plt.tight_layout()

plt.savefig("line chart/png/521.png")

plt.clf()