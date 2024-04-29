

import matplotlib.pyplot as plt 

fig = plt.figure(figsize=(8,6)) 
ax = fig.add_subplot(111) 

country = ['USA', 'UK', 'Germany', 'France'] 
museums = [50, 60, 55, 65] 
galleries = [70, 80, 75, 85] 
theatres = [30, 40, 35, 45] 

ax.bar(country, museums, label='Museums', width=0.2, color='lightgray') 
ax.bar(country, galleries, bottom=museums, label='Galleries', width=0.2, color='darkslategrey') 
ax.bar(country, theatres, bottom=[m+g for m,g in zip(museums, galleries)], label='Theatres', width=0.2, color='darkgray') 

ax.set_title('Number of Arts and Culture venues in four countries in 2021')
ax.set_xticklabels(country, fontsize=10, rotation=0)
ax.set_ylabel("Number of Venues")
ax.legend(loc='best')

plt.tight_layout() 
plt.savefig('bar chart/png/250.png') 
plt.clf()