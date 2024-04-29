
import matplotlib.pyplot as plt
import numpy as np

labels = ['High School', 'Bachelor Degree', 'Master Degree', 'Doctoral Degree', 'Post-Doctoral Degree']
sizes = [25, 30, 20, 15, 10]

fig1, ax1 = plt.subplots(figsize=(10, 8))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 14}, startangle=90, wedgeprops={'linewidth': 0.7, 'edgecolor':'white'})
plt.title('Educational Attainment Rates in the USA, 2023', fontsize=16)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1), fontsize=14)
plt.tight_layout()
plt.savefig('pie chart/png/51.png')
plt.clf()