
import matplotlib.pyplot as plt
import numpy as np

# set up the data
country = ['USA', 'UK', 'Japan', 'India', 'China']
GDP = [20.4, 2.9, 4.9, 2.9, 14.2]
population = [330, 67.6, 126.9, 1353.6, 1409.4]

# set up the figure
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

# plot the line chart
ax.plot(country, GDP, label='GDP', marker='o', color='red', linestyle='dashed')
ax.plot(country, population, label='Population', marker='o', color='blue', linestyle='dashed')

# set the title
ax.set_title('GDP and Population in Top 5 Economies in 2020', fontsize=20)

# set the x-axis label
ax.set_xlabel('Country', fontsize=16)

# set the y-axis label
ax.set_ylabel('Values', fontsize=16)

# set the x-axis ticks
ax.set_xticks(np.arange(len(country)))
ax.set_xticklabels(country, rotation=45, fontweight='bold')

# set the legend
ax.legend(loc='best', fontsize=16)

# annotate the value of each data point
for i, txt in enumerate(GDP):
    ax.annotate(txt, (country[i], GDP[i]), fontsize=14)

for j, txt in enumerate(population):
    ax.annotate(txt, (country[j], population[j]), fontsize=14)

# set the background grid
ax.grid(True, linestyle='--')

# adjust the plot size
fig.tight_layout()

# save the figure
plt.savefig('line chart/png/468.png')

# clear the current image state
plt.clf()