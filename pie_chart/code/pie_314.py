
import matplotlib.pyplot as plt
import numpy as np

sources = ['Solar Energy', 'Wind Energy', 'Hydro Power', 'Geothermal Energy', 'Bioenergy']
percentage = [30, 30, 20, 10, 10]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

ax.pie(percentage, labels=sources, autopct='%1.1f%%', rotatelabels=True, textprops={'wrap': True})
ax.set_title('Breakdown of Renewable Energy Sources in the USA, 2023', fontsize=15)

plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/89.png')
plt.clf()