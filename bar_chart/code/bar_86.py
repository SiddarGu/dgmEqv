
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15,6))

data = [['USA', 1400, 20500, 330], 
        ['UK', 900, 3000, 67], 
        ['Germany', 1200, 5000, 83],
        ['France', 1000, 4000, 66]]

country = [i[0] for i in data]
health_exp = [i[1] for i in data]
gdp = [i[2] for i in data]
pop = [i[3] for i in data]

ind = np.arange(len(country))
width = 0.3

ax = plt.subplot(111)
ax.bar(ind, health_exp, width=width, label='Healthcare Expenditure')
ax.bar(ind+width, gdp, width=width, label='GDP')
ax.bar(ind+2*width, pop, width=width, label='Population')

ax.set_xticks(ind + width)
ax.set_xticklabels(country, rotation=45, wrap=True)

ax.set_title('Healthcare expenditure, GDP and population in four countries in 2021')
ax.legend(loc='best')

plt.tight_layout()
plt.savefig('bar chart/png/563.png')
plt.clf()