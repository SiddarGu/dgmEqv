
import matplotlib.pyplot as plt
import numpy as np

Month = ["January", "February", "March", "April", "May", "June", "July", "August"]
E_commerce = [1000, 1100, 1200, 1300, 1100, 1200, 1400, 1300]
Retail_Store = [1200, 1300, 1400, 1600, 1500, 1400, 1600, 1200]

plt.figure(figsize=(8,4))
ax = plt.subplot()
ax.plot(Month, E_commerce, label="E-commerce", linestyle="dashed")
ax.plot(Month, Retail_Store, label="Retail Store")

for x, y in zip(Month, E_commerce):
    ax.annotate(str(y), xy=(x, y), xytext=(0, 5), textcoords="offset points", fontsize=8)
for x, y in zip(Month, Retail_Store):
    ax.annotate(str(y), xy=(x, y), xytext=(0, 5), textcoords="offset points", fontsize=8)

ax.set_title("Comparison of sales between e-commerce and retail stores in 2020")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (billion dollars)")
ax.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.xticks(Month)
plt.tight_layout()
plt.savefig("line chart/png/109.png")
plt.clf()