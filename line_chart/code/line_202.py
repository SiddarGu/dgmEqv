
import matplotlib.pyplot as plt
import numpy as np

# set data
quarter = np.array(["Q1 2021","Q2 2021","Q3 2021","Q4 2021"])
retail_store_sales = np.array([200,220,270,340])
online_sales = np.array([500,480,460,430])

# create figure
fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot()

# plot line chart
ax.plot(quarter, retail_store_sales, label="Retail Store Sales", linewidth=3)
ax.plot(quarter, online_sales, label="Online Sales", linewidth=3)

# set x,y labels
ax.set_xlabel("Quarter", fontsize=14)
ax.set_ylabel("Sales", fontsize=14)

# set title
ax.set_title("Comparison of Retail Store Sales and Online Sales During 2021", fontsize=16)

# set x ticks
ax.set_xticks(quarter)

# set legend
ax.legend(loc="upper left")

# automatically resize the image
plt.tight_layout()

# save figure
plt.savefig("line chart/png/179.png")

# clear the current image state
plt.clf()