
import matplotlib.pyplot as plt
import numpy as np

country = ["USA", "UK", "Germany", "France"]
Revenue = [9000, 8000, 7000, 6000]
Profit = [1200, 1400, 1300, 1500]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(country, Revenue, label="Revenue", bottom=Profit)
ax.bar(country, Profit, label="Profit")
ax.set_title("Revenue and Profit of four countries in 2021")
ax.set_xlabel("Country")
ax.set_ylabel("Amount (million)")
ax.legend(loc="best")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("bar chart/png/62.png")
plt.clf()