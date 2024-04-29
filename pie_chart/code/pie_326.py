
import matplotlib.pyplot as plt
import numpy as np

labels = ['Conservatism', 'Liberalism', 'Libertarianism','Socialism', 'Anarchism', 'Green Politics', 'Nationalism']
percentages = [25, 25, 15, 15, 10, 5, 5]

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
ax.axis('equal')
ax.pie(percentages, labels=labels, autopct='%1.1f%%', shadow=True)
ax.set_title('Political Ideology Distribution in the USA, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/210.png')
plt.clf()