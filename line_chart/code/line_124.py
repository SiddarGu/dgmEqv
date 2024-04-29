
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
ax = plt.subplot()

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
online_sales = [30, 35, 40, 45, 50, 55, 60]
store_sales = [40, 45, 50, 55, 60, 65, 70]

ax.plot(months, online_sales, label="Online Sales")
ax.plot(months, store_sales, label="Store Sales")

ax.set_title("Comparison of Online Sales and Store Sales in the Retail Industry from January to July 2021")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (in thousands)")
ax.set_xticks(months)
ax.legend(loc="upper left", bbox_to_anchor=(1,1), fontsize='small')

plt.tight_layout()
plt.savefig(r'line chart/png/100.png')
plt.clf()