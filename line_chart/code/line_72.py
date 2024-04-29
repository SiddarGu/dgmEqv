
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
ax = plt.subplot() 
plt.plot([2001, 2002, 2003, 2004], [1.50, 1.80, 1.50, 1.60], color="red", label="Vegetable Price(dollars/kg)")
plt.plot([2001, 2002, 2003, 2004], [2.00, 2.20, 2.50, 2.20], color="green", label="Fruit Price(dollars/kg)")
plt.plot([2001, 2002, 2003, 2004], [2.50, 3.00, 3.00, 2.80], color="blue", label="Grains Price(dollars/kg)")

plt.title("Price of food items in the food and beverage industry from 2001 to 2004")
plt.xlabel("Year")
plt.ylabel("Price")
plt.xticks([2001, 2002, 2003, 2004])
plt.legend(loc="best")

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.savefig('./line chart/png/468.png')
plt.close()