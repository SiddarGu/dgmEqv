
import matplotlib.pyplot as plt

year_list=[2020, 2021, 2022, 2023, 2024]
profit_list=[500, 600, 800, 900, 1000]
revenue_list=[1000, 1200, 1500, 1800, 2000]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()
ax.plot(year_list, profit_list, label="Profit(million dollars)")
ax.plot(year_list, revenue_list, label="Revenue(million dollars)")
ax.set_title("Revenue and Profit of a Company in 2021-2024")
ax.set_xticks(year_list)
ax.legend(loc="best", prop={'size': 10})
plt.tight_layout()
plt.savefig("line chart/png/261.png")
plt.clf()