
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot()

Country = ["USA","UK","Germany","France"]
Museums = [50,60,80,70]
Galleries = [100,110,120,130]
Theaters = [150,160,140,170]

ax.bar(Country, Museums, label="Museums", color="C0")
ax.bar(Country, Galleries, bottom=Museums, label="Galleries", color="C1")
ax.bar(Country, Theaters, bottom=[m+g for m,g in zip(Museums, Galleries)], label="Theaters", color="C2")

ax.set_xticks(Country)
ax.set_title("Number of cultural venues in four countries in 2021")
ax.set_xlabel("Country")
ax.set_ylabel("Number of venues")
ax.legend()

fig.tight_layout()
fig.savefig("bar chart/png/247.png")

plt.clf()