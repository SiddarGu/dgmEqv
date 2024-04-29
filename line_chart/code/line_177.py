
import matplotlib.pyplot as plt
import numpy as np

Year = [2020, 2021, 2022, 2023, 2024]
Profit = [1000, 1200, 1500, 1800, 2000]
Revenue = [5000, 7000, 9000, 10000, 12000]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()
ax.plot(Year, Profit, color="red", linestyle="-", marker="o", label="Profit (million dollars)")
ax.plot(Year, Revenue, color="blue", linestyle="-", marker="o", label="Revenue (million dollars)")
ax.set_title("Profit and Revenue of a Business from 2020 to 2024")
ax.set_xlabel("Year")
ax.set_ylabel("Amount (million dollars)")
ax.set_xticks(np.arange(2020, 2025, 1))
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize='large',
          fancybox=True, shadow=True, frameon=True)
plt.tight_layout()
plt.savefig("line chart/png/401.png")
plt.clf()