
import matplotlib.pyplot as plt
import numpy as np

x = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
y1 = [50, 45, 49, 51, 46, 48, 47, 48]
y2 = [40, 45, 49, 51, 46, 48, 47, 50]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

ax.plot(x, y1, color='red', marker='o', label='Carbon Emissions')
ax.plot(x, y2, color='blue', marker='o', label='Renewable Energy Sources')

plt.title('Carbon Emissions and Renewable Energy Sources in Europe in 2020')
plt.xticks(x, rotation=45, wrap=True)
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/65.png')
plt.clf()