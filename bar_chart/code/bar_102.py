
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

region = ["North America", "South America", "Europe", "Asia"]
users = [200, 300, 400, 500]
data_usage = [1000, 1200, 1500, 1800]

ax.bar(region, users, color="b", label="Users")
ax.bar(region, data_usage, bottom=users, color="r", label="Data Usage (GB)")

ax.legend(loc="best")
ax.set_title("Number of users and data usage in four regions in 2021")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("bar chart/png/399.png")
plt.clf()