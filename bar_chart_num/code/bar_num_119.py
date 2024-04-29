
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)

Region = ["North America", "Europe", "Asia", "South America"]
Donations = [50, 70, 30, 40]
Volunteers = [100, 120, 90, 80]

p1 = ax.bar(Region, Donations, width=0.4, label="Donations(million)")
p2 = ax.bar(Region, Volunteers, width=0.4, label="Volunteers", bottom=Donations)

plt.title("Monetary and volunteer donations to charity organizations in four regions in 2021")
ax.set_xticklabels(Region, rotation=0)
ax.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130])
ax.legend(loc="upper right")

for i in range(len(Region)):
    ax.annotate(str(Donations[i]), xy=(p1[i].get_x() + 0.2, p1[i].get_height() / 2), xytext=(0, 3), 
            textcoords="offset points", ha="center", va="center", rotation=90)
    ax.annotate(str(Volunteers[i]), xy=(p2[i].get_x() + 0.2, p2[i].get_height() / 2 + p1[i].get_height()), xytext=(0, 3), 
            textcoords="offset points", ha="center", va="center", rotation=90)

plt.tight_layout()
plt.savefig("Bar Chart/png/275.png")
plt.clf()