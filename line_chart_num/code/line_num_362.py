
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
ax = plt.subplot()

month = ["January", "February", "March", "April"]

beverages = [1000, 1200, 800, 1500]
fruits = [800, 900, 1100, 1200]
dairy = [1200, 1100, 1300, 1400]
meat = [1500, 1600, 1200, 800]

ax.plot(month, beverages, label="Beverages")
ax.plot(month, fruits, label="Fruits")
ax.plot(month, dairy, label="Dairy")
ax.plot(month, meat, label="Meat")

plt.xticks(month)
plt.title("Sales of food and beverage products by month in 2021")
plt.xlabel("Month")
plt.ylabel("Sales (million dollars)")
plt.legend(loc="upper left")

for a, b in zip(month, beverages):
    ax.annotate(str(b), xy=(a, b), xytext=(a, b+50))

for a, b in zip(month, fruits):
    ax.annotate(str(b), xy=(a, b), xytext=(a, b+50))

for a, b in zip(month, dairy):
    ax.annotate(str(b), xy=(a, b), xytext=(a, b+50))

for a, b in zip(month, meat):
    ax.annotate(str(b), xy=(a, b), xytext=(a, b+50))

plt.tight_layout()
plt.savefig("line chart/png/300.png")
plt.clf()