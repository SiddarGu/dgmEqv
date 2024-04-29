
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
ax = plt.subplot()

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
online_sales = [100, 120, 125, 130, 135, 140, 145]
retail_sales = [150, 140, 145, 150, 155, 160, 165]
total_sales = [250, 260, 270, 280, 290, 300, 310]

ax.plot(month, online_sales, label="Online Shopping Sales")
ax.plot(month, retail_sales, label="Retail Store Sales")
ax.plot(month, total_sales, label="Total Sales")

ax.set_title("Total Retail and E-commerce Sales in 2021")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (billion dollars)")
ax.legend(loc="upper left", bbox_to_anchor=(1,1))

plt.xticks(month, rotation="vertical")
plt.tight_layout()
plt.savefig("line chart/png/131.png")
plt.clf()