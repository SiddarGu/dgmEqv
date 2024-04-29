
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 330, 21000, 4.0], 
        ['UK', 67, 3000, 6.2], 
        ['France', 66, 2500, 9.6], 
        ['Canada', 37, 1800, 7.1], 
        ['India', 1350, 2700, 7.4]]

labels = np.array(data)[:,0]
population = np.array(data)[:,1].astype(float)
gdp = np.array(data)[:,2].astype(float)
unemployment = np.array(data)[:,3].astype(float)

fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(111)

ax1.plot(labels, population, label='Population(millions)', color='b', marker='o')
ax1.plot(labels, gdp, label='GDP(billion dollars)', color='r', marker='o')
ax1.plot(labels, unemployment, label='Unemployment rate', color='g', marker='o')

plt.xticks(np.arange(len(labels)), labels, rotation=45)
plt.title('Population, GDP, and Unemployment rate of four countries in 2020')
ax1.legend()
plt.tight_layout()
plt.savefig('line chart/png/208.png')
plt.clf()