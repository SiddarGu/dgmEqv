
import matplotlib.pyplot as plt
import numpy as np

sources = ['Fossil Fuels', 'Renewable Energy', 'Nuclear Power', 'Other']
percentage = [35, 35, 20, 10]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()
pie_chart = ax.pie(percentage, labels=sources, autopct='%.1f%%', startangle=90, textprops={'fontsize': 14}, 
                    wedgeprops={'linewidth': 2, 'edgecolor': 'w'}, explode=[0.1, 0.1, 0.1, 0.1])
ax.set_title('Energy Sources Distribution in the USA, 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Energy Sources', fontsize=14, fontweight='bold')

plt.legend(fontsize=14)
plt.tight_layout()
plt.xticks(rotation=30)
plt.savefig('pie chart/png/302.png', bbox_inches='tight')
plt.clf()