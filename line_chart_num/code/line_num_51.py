
# import libraries
import matplotlib.pyplot as plt
import numpy as np

# data
data = [['USA', 330, 20], 
        ['China', 1400, 13], 
        ['India', 1300, 3], 
        ['Canada', 37, 1.8], 
        ['France', 67, 2.7], 
        ['Mexico', 128, 1.2]]

# extract data
countries, population, gdp = [], [], []
for row in data:
    countries.append(row[0])
    population.append(row[1])
    gdp.append(row[2])

# create figure
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)

# plot data
ax.plot(population, gdp, marker='o', label="GDP")

# annotate
for i, txt in enumerate(countries):
    ax.annotate(txt, (population[i], gdp[i]), xytext=(2,-2), textcoords='offset points')

# add legend
ax.legend(loc="upper left")

# add title
ax.set_title('Population and GDP comparison of five countries in 2021', fontsize=14)

# add axes labels
ax.set_xlabel("Population (in millions)")
ax.set_ylabel("GDP (in billions)")

# add grids
ax.grid(True, linestyle='--', linewidth=0.5)

# set xticks
ax.set_xticks(np.arange(0, 1500, 200))

# resize image
fig.tight_layout()

# save figure
fig.savefig('line chart/png/479.png')

# clear figure
plt.clf()