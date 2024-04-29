
import matplotlib.pyplot as plt
import numpy as np

data = [['USA',400,20,350], ['UK',300,16,310], ['Germany',220,18,280], ['France',250,17,290]]

country,political_spending, gdp, population = [], [], [], []
for i in range(len(data)):
    country.append(data[i][0])
    political_spending.append(data[i][1])
    gdp.append(data[i][2])
    population.append(data[i][3])

x = np.arange(len(country))
width = 0.25

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()
ax.bar(x, political_spending, width, label="Political Spending")
ax.bar(x+width, gdp, width, label="GDP")
ax.bar(x+width*2, population, width, label="Population")

ax.set_title("Government spending, GDP and Population in four countries in 2021")
ax.set_xticks(x+width/2)
ax.set_xticklabels(country)
ax.legend(loc='best')

for i in range(4):
    ax.annotate(political_spending[i], (x[i] - 0.1, political_spending[i] + 15))
    ax.annotate(gdp[i], (x[i] + 0.2, gdp[i] + 15))
    ax.annotate(population[i], (x[i] + 0.6, population[i] + 15))

plt.tight_layout()
plt.savefig('Bar Chart/png/145.png')
plt.cla()