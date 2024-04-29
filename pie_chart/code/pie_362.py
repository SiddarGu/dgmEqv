
import matplotlib.pyplot as plt
import numpy as np

labels = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass']
data = [25,25,20,20,10]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot()
ax.pie(data, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 14})
ax.axis('equal')
ax.set_title('Percentage of Renewable Energy Sources in the USA, 2023', fontsize=16)
plt.tight_layout()
plt.savefig('pie chart/png/141.png')
plt.clf()