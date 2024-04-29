
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(7,7))
labels = ['Single Family Homes','Condominiums','Apartments','Townhouses','Other']
sizes = [45,25,20,5,5]
explode = (0, 0, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90, textprops={'fontsize': 6, 'rotation': 0, 'wrap': True})
plt.title('Distribution of Housing Types in the US Real Estate Market, 2023', fontsize=10)
plt.tight_layout()
plt.savefig('pie chart/png/146.png')
plt.show()
plt.clf()