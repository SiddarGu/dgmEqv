
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

labels = ["London", "New York", "Tokyo", "Sydney"]
Home_prices = [500000, 600000, 800000, 700000]
Rents = [2000, 2500, 3000, 2200]
width = 0.4

ax.bar(labels, Home_prices, width=width, label="Home Prices", color='red')
ax.bar(labels, Rents, width=width, bottom=Home_prices, label="Rents", color='green')
ax.set_title("Average Home Prices and Rents in four major cities in 2021")
ax.set_xlabel("City")
ax.set_ylabel("Price/Rent")
ax.legend()

plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
plt.tight_layout()
plt.savefig("bar chart/png/466.png")
plt.clf()