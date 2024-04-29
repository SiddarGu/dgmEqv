
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
ax = plt.subplot()
ax.bar(x = ["North America", "South America", "Europe", "Asia"], height = [2000, 1800, 2500, 3000], width = 0.3, label = "Vegetables(tons)", color = "green")
ax.bar(x = ["North America", "South America", "Europe", "Asia"], height = [1500, 1600, 2000, 2500], width = -0.3, label = "Fruits(tons)", color = "red")
ax.legend(loc="upper left")
ax.set_title("Total vegetable and fruit production in four regions in 2021")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("bar chart/png/6.png")
plt.clf()