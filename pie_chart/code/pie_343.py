
import matplotlib.pyplot as plt 
import numpy as np

fig = plt.figure(figsize=(8,6)) 
ax = fig.add_subplot()

sources = ['Solar','Wind','Nuclear','Hydroelectric','Geothermal']
percentage = [25,20,30,15,10]

ax.pie(percentage, labels=sources, autopct='%1.1f%%',
        shadow=True, startangle=90,
        wedgeprops={'linewidth':2,'edgecolor':'black'})

plt.title('Energy Distribution in the USA, 2023')
plt.legend(bbox_to_anchor=(1,0.5), loc="center right", fontsize=12)
plt.tight_layout()
plt.xticks(rotation=45)

plt.savefig('pie chart/png/202.png')
plt.clf()