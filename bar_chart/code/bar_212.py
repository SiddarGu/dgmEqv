
import matplotlib.pyplot as plt

# set the figure size
plt.figure(figsize=(15,8))

# create subplot
ax = plt.subplot()

# set the data
countries = ["USA","UK","Germany","France"]
solar = [15000,18000,14000,16000]
wind = [20000,17000,19000,18000]
hydro = [12000,14000,18000,15000]

# plot the data
ax.bar(countries, solar, label="Solar Energy(KWh)")
ax.bar(countries, wind, bottom=solar, label="Wind Energy(KWh)")
ax.bar(countries, hydro, bottom=[i+j for i,j in zip(solar, wind)], label="Hydro Energy(KWh)")

# set the title of the figure
ax.set_title("Energy production from solar, wind and hydro sources in four countries in 2021")

# set the xticks
ax.set_xticks(countries)

# add legend
ax.legend(bbox_to_anchor=(1.2, 1))

# add grids
ax.grid(axis="y", alpha=0.5)

# adjust the figure
plt.tight_layout()

# save the figure as png
plt.savefig("bar chart/png/554.png")

# clear the current image state
plt.clf()