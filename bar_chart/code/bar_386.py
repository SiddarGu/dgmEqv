
import matplotlib.pyplot as plt

x_labels = ["USA", "UK", "Germany", "France"]
y_museums = [100, 120, 110, 130]
y_theatres = [90, 110, 100, 120]
y_galleries = [80, 100, 90, 110]

plt.figure(figsize=(8,5))
ax = plt.subplot()

ax.bar(x_labels, y_museums, width=0.2, label="Museums")
ax.bar(x_labels, y_theatres, bottom=y_museums, width=0.2, label="Theatres")
ax.bar(x_labels, y_galleries, bottom=[i+j for i,j in zip(y_museums, y_theatres)], width=0.2, label="Galleries")

ax.set_title("Number of museums, theatres, and galleries in four countries in 2021")
ax.set_xticklabels(x_labels, rotation=0, wrap=True)
ax.legend(loc="upper right")

plt.tight_layout()
plt.savefig("bar chart/png/456.png")
plt.clf()