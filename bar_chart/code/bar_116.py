
import matplotlib.pyplot as plt
import numpy as np

region = ["North America", "Europe", "Asia", "South America"]
donations = [200, 150, 180, 100]
hours = [4500, 4000, 4700, 3000]

fig, ax = plt.subplots(figsize=(10,8))
ax.bar(region, donations, label = "Donations Received (million)", width=0.5, alpha=0.5, bottom=0)
ax.bar(region, hours, label = "Volunteering Hours", width=0.5, alpha=0.5, bottom=donations)

ax.set_title("Donations and volunteering hours of charitable organizations in four regions in 2021")
ax.set_xticks(region)
ax.legend(loc="upper left")

plt.tight_layout()
plt.savefig("bar chart/png/497.png")
plt.clf()