
import matplotlib.pyplot as plt

labels = ['New York City', 'Los Angeles', 'Chicago', 'Houston']
median_home_price = [800000, 750000, 600000, 450000]
average_rent = [3000, 2800, 2500, 2300]

fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot()
ax.bar(labels, median_home_price, width=0.4,bottom=average_rent, label="Median Home Price")
ax.bar(labels, average_rent, width=0.4, label="Average Rent")
ax.set_title("Median Home Price and Average Rent in four major cities in 2021")
ax.set_xticklabels(labels, rotation=45, wrap=True)
ax.legend()
plt.tight_layout()
plt.savefig("bar chart/png/273.png")
plt.clf()