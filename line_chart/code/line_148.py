
import matplotlib.pyplot as plt
import numpy as np

year = np.array([2001, 2002, 2003, 2004])
deaths = np.array([800, 750, 850, 900])
births = np.array([900, 850, 950, 1000])
life_expectancy = np.array([66, 68, 70, 72])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.plot(year, deaths, '-', color='red', label="Deaths")
ax.plot(year, births, '-', color='blue', label="Births")
ax.plot(year, life_expectancy, '-', color='green', label="Life Expectancy")
ax.set_title("Global Births and Deaths and Life Expectancy in the 21st Century", fontsize=20)
ax.set_xlabel('Year', fontsize=16)
ax.set_ylabel('Data (in thousands)', fontsize=16)
ax.legend(loc='upper left', fontsize=14)
ax.grid(linestyle='--')
plt.xticks(year)
plt.tight_layout()
plt.savefig('line chart/png/480.png')
plt.clf()