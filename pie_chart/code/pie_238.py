
import matplotlib.pyplot as plt
import numpy as np

labels=['Renewable', 'Nuclear', 'Coal', 'Natural Gas', 'Oil']
sizes=[35,17,20,15,13]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.pie(sizes, labels = labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal') 
plt.title('Energy Consumption in the USA, 2023')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/200.png')
plt.clf()