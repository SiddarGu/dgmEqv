
import matplotlib.pyplot as plt

regions = ["North America", "Europe", "Asia", "South America", "Africa", "Oceania"]
population_share = [30, 30, 20, 10, 7, 3]

fig = plt.figure(num=None, figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k')

ax = fig.add_subplot(111)
ax.pie(population_share, labels=regions, autopct='%.2f%%', startangle=90, textprops={'fontsize': 10}, pctdistance=0.7, labeldistance=1.1)

ax.set_title("Global Distribution of Lawyers in 2023", fontsize=13, y=1.08)

plt.tight_layout()
plt.xticks(rotation=45)

plt.savefig("pie chart/png/219.png")
plt.clf()