

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

products = ["Dairy", "Fruits and Vegetables", "Meat and Fish", "Bakery Products", "Beverages", "Other"]
percentage = [20, 30, 15, 10, 15, 10]

plt.figure(figsize=(10, 10))
ax = plt.subplot()
ax.pie(percentage, labels=products,autopct='%1.1f%%', startangle=90, textprops={'fontsize': 8})
ax.axis('equal')
ax.set_title("Distribution of Food and Beverage Products in the Global Market in 2021", fontsize=15)
plt.tight_layout()
plt.savefig("pie chart/png/362.png")
plt.clf()