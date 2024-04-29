
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 4))

labels = ['Beverages', 'Meats', 'Dairy', 'Fruits and Vegetables', 'Bakery and Grains']
percentages = [25, 20, 15, 30, 10]

ax.pie(percentages, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90,
        textprops={'fontsize': 10}, wedgeprops={'linewidth': 1.5})
ax.legend(loc='best', bbox_to_anchor=(1.2, 0), frameon=False, fontsize=10)
ax.set_title('Distribution of Food and Beverage Products in the USA, 2023', fontsize=15)

plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/338.png')
plt.clf()