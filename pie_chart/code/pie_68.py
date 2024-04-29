
import matplotlib.pyplot as plt 
import numpy as np 

types = ['Single-Family Homes', 'Multi-Family Homes', 'Townhomes', 'Condos', 'Mobile Homes']
percentages = [45, 25, 10, 10, 10]

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot()
ax.pie(percentages, autopct='%.1f%%', pctdistance=0.8, shadow=True, startangle=90, textprops={'fontsize': 12, 'color':'black'})
ax.legend(types, bbox_to_anchor=(1.05, 0, 0.4, 1), loc='lower left', fontsize='large')
plt.title('Distribution of Home Types in the USA, 2023', fontsize=18)
plt.tight_layout()
plt.savefig('pie chart/png/402.png')
plt.show()
plt.clf()