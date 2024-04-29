

import matplotlib.pyplot as plt
import numpy as np

country = ['USA', 'Canada', 'Mexico', 'France', 'Germany', 'Brazil', 'India']
vaccines_administered = [100, 30, 20, 80, 90, 50, 60]
population = [350, 40, 130, 70, 90, 220, 1350]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.plot(country, vaccines_administered, 'b-o', label="Vaccines administered (million doses)")
ax.plot(country, population, 'r-o', label="Population (million people)")
ax.set_title('Vaccination rate of selected countries in 2021')
ax.set_xticks(country)
ax.set_ylabel('Number of doses/people')
ax.legend(loc='upper right')

for x, y1, y2 in zip(country, vaccines_administered, population):
    ax.annotate('{:0.0f}\n{:0.0f}'.format(y1, y2), (x, y1), xytext=(0, 4), textcoords='offset points', rotation=45)

plt.tight_layout()
plt.savefig('line chart/png/2.png', dpi=300)
plt.clf()