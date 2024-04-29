
import matplotlib.pyplot as plt

Country = ["USA", "UK", "Germany", "France"]
Retail_sales = [3.5, 2.3, 2.8, 2.2]
E_commerce_sales = [1.2, 1.7, 1.3, 1.5]

fig = plt.figure(figsize=(10,6)) 
ax = fig.add_subplot()
ax.bar(Country, Retail_sales, label="Retail sales")
ax.bar(Country, E_commerce_sales, bottom=Retail_sales, label="E-commerce sales")

ax.set_title("Comparison of retail and e-commerce sales in four countries in 2021")
ax.set_xlabel("Country")
ax.set_ylabel("Sales (billion)") 
ax.legend(loc="upper left")

for i, v in enumerate(Retail_sales):
    ax.text(i, v/2, str(v), ha="center", color="white")
for i, v in enumerate(E_commerce_sales):
    ax.text(i, v/2+Retail_sales[i], str(v), ha="center", color="black")

plt.xticks(Country)

plt.tight_layout()
plt.savefig("Bar Chart/png/489.png")
plt.clf()