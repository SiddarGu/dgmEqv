
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (10, 6))
ax = fig.add_subplot()

country_list = ["USA", "UK", "Germany", "France"]
renewable_list = [500,400,600,350]
non_renewable_list = [1000, 900, 1100, 800]

ax.bar(country_list, renewable_list, label="Renewable Energy(GWh)", bottom=non_renewable_list)
ax.bar(country_list, non_renewable_list, label="Non-Renewable Energy(GWh)")

ax.set_xticklabels(country_list, rotation=0, wrap=True)
ax.legend(loc="upper center")
ax.set_title("Renewable and Non-renewable Energy Production in Four Countries in 2021")
fig.tight_layout()

plt.savefig("bar chart/png/308.png")
plt.clf()