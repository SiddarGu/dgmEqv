
import matplotlib.pyplot as plt
import numpy as np

labels = ['Renewable', 'Nuclear', 'Fossil Fuel']
percentages = [55, 20, 25]

plt.figure(figsize=(10,8))
plt.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 14}, wedgeprops={'linewidth': 3, 'edgecolor': 'white'})
plt.title('Energy Sources in the USA in 2023', fontsize=18, fontweight='bold', wrap=True, horizontalalignment='center')
plt.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=14, frameon=False)
plt.axis('equal')
plt.xticks([])
plt.tight_layout()
plt.savefig('pie chart/png/350.png', bbox_inches='tight')
plt.clf()