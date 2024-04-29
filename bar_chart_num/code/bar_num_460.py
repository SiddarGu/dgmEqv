
import matplotlib.pyplot as plt
import numpy as np

country = ["USA", "UK", "Germany", "France"]
fruits = [200, 300, 180, 230]
vegetables = [450, 500, 400, 470]
grains = [400, 500, 450, 350]

x = np.arange(len(country))

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x, fruits, label="Fruits")
ax.bar(x, vegetables, bottom=fruits, label="Vegetables")
ax.bar(x, grains, bottom=np.array(vegetables)+np.array(fruits), label="Grains")

ax.set_title("Amount of food production in four countries in 2021")
ax.set_xticks(x)
ax.set_xticklabels(country)
ax.legend()

for i, (f, v, g) in enumerate(zip(fruits, vegetables, grains)):
    ax.annotate(str(f), (i-0.1, f/2))
    ax.annotate(str(v), (i-0.1, (f+v)/2))
    ax.annotate(str(g), (i-0.1, (f+v+g)/2))

plt.tight_layout()
plt.savefig('Bar Chart/png/143.png')
plt.clf()