
import matplotlib.pyplot as plt
import numpy as np

Country = ["USA", "UK", "Germany", "France"]
Museums = [400, 500, 350, 450]
Theaters = [200, 300, 250, 350]
Galleries = [800, 1000, 900, 1100]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()
width = 0.25
ax.bar(Country, Museums, width, label="Museums")
ax.bar(Country, Theaters, width, bottom=Museums, label="Theaters")
ax.bar(Country, Galleries, width, bottom=[i+j for i,j in zip(Museums, Theaters)], label="Galleries")

ax.set_title("Number of Arts and Culture venues in four countries in 2021")
ax.set_xticks(Country)
ax.set_xlabel("Country")
ax.set_ylabel("Number")
plt.legend(loc="upper right")

for x,y in zip(Country, Museums):
    plt.annotate(y, (x,y+30), ha="center")
for x,y in zip(Country, Theaters):
    plt.annotate(y, (x,sum(Museums)+y+30), ha="center")
for x,y in zip(Country, Galleries):
    plt.annotate(y, (x,sum(Museums)+sum(Theaters)+y+30), ha="center")

plt.tight_layout()
plt.savefig("Bar Chart/png/512.png")
plt.clf()