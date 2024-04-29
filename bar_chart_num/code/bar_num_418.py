

import matplotlib.pyplot as plt

Region = ["North", "South", "East", "West"]
Home_Price = [200, 250, 300, 350]
Rent = [1200, 1500, 1800, 2100]

fig = plt.figure()
ax = fig.add_subplot()
ax.bar(Region, Home_Price, label="Average Home Price", bottom=0, width=0.3, color="red")
ax.bar(Region, Rent, label="Average Rent", bottom=0, width=0.3, color="green")

ax.set_title("Average Home Price and Rent in Four Regions in 2021")
ax.set_xlabel("Region")
ax.set_ylabel("Price/Rent (thousands)")
ax.legend(loc="upper left")

for i, v in enumerate(Home_Price):
    ax.text(i - 0.1, v + 10, str(v), color="red")
for i, v in enumerate(Rent):
    ax.text(i + 0.2, v + 10, str(v), color="green")

fig.set_figwidth(12)
fig.set_figheight(6)
plt.tight_layout()
plt.xticks(Region)
plt.savefig("Bar Chart/png/218.png")
plt.clf()