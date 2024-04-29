
import matplotlib.pyplot as plt
plt.figure(figsize=(7,5))

country = ["USA","UK","Germany","France"]
sector_a = [1000,900,1100,800]
sector_b = [800,1100,1200,1400]
sector_c = [1200,1300,1400,1500]

ax = plt.subplot()
ax.bar(country, sector_a, bottom=sector_b, label="Sector A")
ax.bar(country, sector_b, bottom=sector_c, label="Sector B")
ax.bar(country, sector_c, label="Sector C")

ax.set_title("Manufacturing output across three sectors in four countries in 2021")
ax.set_xticklabels(country, rotation=45, ha='right', wrap=True)
ax.legend()

plt.tight_layout()
plt.savefig("bar chart/png/260.png")
plt.clf()