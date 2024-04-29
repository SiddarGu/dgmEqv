
import matplotlib.pyplot as plt
import numpy as np

labels = ['Solar', 'Wind', 'Nuclear', 'Hydro', 'Natural Gas', 'Biomass', 'Geothermal']
sizes = [25, 20, 15, 15, 10, 10, 5]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightsteelblue', 'plum', 'springgreen', 'lavender']
explode = (0, 0.1, 0, 0, 0, 0, 0) 

fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot()
ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
ax.axis('equal')
ax.set_title('Renewable Energy Sources in the USA in 2023', fontsize=20)
ax.legend(labels, bbox_to_anchor=(1, 1), loc='upper left', fontsize=15)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/361.png')
plt.clf()