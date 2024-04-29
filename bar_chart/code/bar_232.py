
import matplotlib.pyplot as plt
import numpy as np

Country = ["USA", "UK", "Germany", "France"]
Online_Retail_Transaction = np.array([3000, 2500, 2000, 2250])
Offline_Retail_Transaction = np.array([2000, 1750, 1500, 1700])


fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
width = 0.35
ax.bar(Country, Online_Retail_Transaction, width, color="b", label="Online Retail Transaction")
ax.bar(Country, Offline_Retail_Transaction, width, bottom=Online_Retail_Transaction, color="g", label="Offline Retail Transaction")
ax.set_title("Comparison of online and offline retail transactions in four countries in 2021")
ax.set_xlabel("Country")
ax.set_ylabel("Retail Transaction (million)")
ax.legend(loc="best", ncol=2, fontsize="large")
ax.set_xticklabels(Country, rotation = 45, ha="right")
plt.tight_layout()
plt.savefig("bar chart/png/430.png")
plt.clf()