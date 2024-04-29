
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

product = ['Automobiles', 'Aerospace', 'Electronics', 'Chemicals', 'Industrial Machinery', 'Metal Products', 'Other']
share = [25, 15, 25, 15, 10, 10, 5]

ax.pie(share, labels=product, autopct='%1.1f%%', startangle=90)
ax.set_title("Distribution of Manufacturing Output in the USA, 2023")
ax.legend(loc="best", bbox_to_anchor=(1,1))

plt.tight_layout()
plt.savefig('pie chart/png/21.png')
plt.clf()