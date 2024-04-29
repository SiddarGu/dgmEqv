
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10,6))
country = ['USA','UK','Germany','France']
crops = [200, 100, 150, 110]
livestock = [70, 50, 60, 40]

ax.bar(country,crops,label='Crops',bottom=livestock,width=0.3,align='center')
ax.bar(country,livestock,label='Livestock',width=0.3,align='center')
ax.set_xticks(country)
ax.set_title('Crop and Livestock Production in Four Countries in 2021')
ax.legend(bbox_to_anchor=(1.05,1),loc='upper left')
plt.tight_layout()
plt.savefig('bar chart/png/471.png')
plt.clf()