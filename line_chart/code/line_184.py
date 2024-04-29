
import matplotlib.pyplot as plt
import numpy as np

months = ["January", "February", "March", "April", "May"]
sales_a = [1500, 1900, 1700, 2000, 1800]
sales_b = [1000, 1500, 1400, 1800, 1400]
sales_c = [2000, 1800, 1600, 1700, 1900]
sales_d = [2500, 2100, 2200, 2300, 2500]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.plot(months, sales_a, label="Sales A")
ax.plot(months, sales_b, label="Sales B")
ax.plot(months, sales_c, label="Sales C")
ax.plot(months, sales_d, label="Sales D")
plt.xticks(np.arange(5), months, rotation=30, ha="right")
ax.set_title("Monthly sales of four types of food products in 2021")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.legend(loc="upper left")
plt.tight_layout()
plt.savefig("line chart/png/83.png")
plt.clf()