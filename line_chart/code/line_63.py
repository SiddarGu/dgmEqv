
import matplotlib.pyplot as plt
import numpy as np

months = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'])
online_purchases = np.array([3000, 3200, 3500, 3700, 4000, 4200, 4500, 4700])
in_store_purchases = np.array([4000, 4200, 4500, 4700, 5000, 5200, 5500, 5700])

fig = plt.figure(figsize=(8,6))
plt.plot(months, online_purchases, label="Online Purchases(million dollars)", color="green", marker="o", linestyle="--")
plt.plot(months, in_store_purchases, label="In-Store Purchases(million dollars)", color="red", marker="o", linestyle="--")
plt.title("Monthly Comparison of Online and In-Store Purchases in 2021")
plt.xlabel("Month")
plt.ylabel("Amount (million dollars)")
plt.xticks(months, rotation=45)
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig("line chart/png/142.png")
plt.clf()