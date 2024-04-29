
import matplotlib.pyplot as plt
import matplotlib.cm as cm

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot()

home_types = ["Single-family Homes", "Condominiums", "Townhouses", "Multi-family Homes"]
percents = [50, 25, 15, 10]

plt.pie(percents, labels=home_types, autopct='%1.1f%%', textprops={'fontsize': 14}, startangle=-90, 
        shadow=True, explode=[0.05, 0, 0, 0], colors=cm.Dark2(range(4)))
ax.axis('equal')
plt.title("Breakdown of Home Types in the USA Housing Market in 2021")
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/368.png')
plt.clf()