
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8))
ax = plt.subplot()
labels = ['Automotive', 'Electronics', 'Textile','Chemical', 'Food & Beverage', 'Machinery', 'Metals', 'Other']
sizes = [25, 20, 15, 10, 10, 10, 10, 10]
explode = (0.1, 0, 0, 0, 0, 0, 0, 0) 
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.set_title('Market Share of Manufacturing Industries in 2023', fontweight="bold", fontsize=14)
ax.axis('equal')
plt.tight_layout()
plt.savefig("pie chart/png/198.png")
plt.show()
plt.clf()