

import matplotlib.pyplot as plt
import numpy as np

months = ["January","February","March","April","May","June","July","August"]
number_of_orders = [500,600,700,800,900,1000,1100,1200]
average_order_value = [50,55,60,65,70,75,80,85]

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.plot(months, number_of_orders, label="Number of Orders")
ax.plot(months, average_order_value, label="Average Order Value")
ax.set_title("Online Order Trends in 2020")
ax.set_xlabel("Month")
ax.set_ylabel("Number of orders/Average order value")
ax.legend(loc="upper left")
plt.xticks(np.arange(len(months)), months, rotation=45)
plt.tight_layout()
plt.savefig("line chart/png/492.png")
plt.clf()