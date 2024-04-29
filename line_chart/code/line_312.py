
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15, 10))
x = np.arange(4)
country =['USA', 'China', 'India', 'Japan']
population = [330000000,1400000000,1326000000,1268000000]
GDP = [2140000000000,1420000000000,2700000000000,5400000000000]

plt.bar(x, population, label='Population')
plt.plot(x, GDP, color='red', label='GDP')
plt.xticks(x, country, rotation=45, fontsize=12, wrap=True)
plt.title('Population and GDP of Top 4 Economies in 2020', fontsize=20)
plt.legend()
plt.tight_layout()
plt.savefig('line chart/png/23.png')
plt.clf()