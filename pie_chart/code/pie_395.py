
import matplotlib.pyplot as plt
import numpy as np

crops = ('Cereals', 'Vegetables', 'Fruits', 'Legumes', 'Nuts', 'Seeds', 'Oils', 'Other')
percentages = (28, 18, 20, 12, 10, 7, 5, 10)

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(percentages, labels=crops, autopct='%.1f%%', textprops={'wrap':True, 'rotation':30})
ax.set_title('Distribution of Crops by Percentage in the Global Agriculture Industry, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/453.png')
plt.clf()