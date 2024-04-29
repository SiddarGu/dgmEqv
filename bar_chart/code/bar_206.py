
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
ax = plt.subplot()

Regions = ["North America", "South America", "Europe", "Asia"]
Hotels = [300, 400, 200, 350]
Restaurants = [200, 300, 500, 400]
Tourists = [500, 450, 350, 400]

ax.bar(Regions, Hotels, label="Hotels", width=0.2, bottom=0)
ax.bar(Regions, Restaurants, label="Restaurants", width=0.2, bottom=Hotels)
ax.bar(Regions, Tourists, label="Tourists", width=0.2, bottom=[x + y for x, y in zip(Hotels, Restaurants)])

ax.set_title("Number of Hotels, Restaurants and Tourists in four regions in 2021")
ax.set_xticklabels(Regions, rotation=45, ha="right", wrap=True)
ax.legend()

plt.tight_layout()
plt.savefig('bar chart/png/113.png')

plt.clf()