
import matplotlib.pyplot as plt

plt.figure(figsize=(10,8))
ax = plt.subplot()
labels = ["Clothing", "Electronics", "Home & Garden", "Grocery", "Beauty & Health", "Sports & Outdoors", "Toys & Games"]
sizes = [25, 20, 20, 15, 10, 5, 5]
explode = [0, 0, 0, 0, 0, 0, 0]
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')
plt.title("Distribution of Online Shopping Categories in the USA, 2023")
plt.tight_layout()
plt.savefig('pie chart/png/386.png', bbox_inches='tight')
plt.xticks(rotation=90)
plt.show()
plt.clf()