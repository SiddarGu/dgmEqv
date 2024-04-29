
import matplotlib.pyplot as plt
import numpy as np

labels = ['Renewables', 'Coal', 'Oil', 'Natural Gas', 'Nuclear']
sizes = [25, 20, 15, 30, 10]

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 14})
ax.axis('equal') 
ax.set_title('Energy Sources in the US, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/342.png')
plt.clf()