
import matplotlib.pyplot as plt
labels = ["Fast Food","Grocery Stores","Cafes and Restaurants","Online Delivery Services","Others"]
sizes = [25,30,30,10,5]
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", textprops={'fontsize': 12}, startangle=90, pctdistance=0.8, labeldistance=1.1)
ax.set_title("Distribution of Food and Beverage Industry in the US in 2023")
ax.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/305.png',dpi=300)
plt.gcf().clear()