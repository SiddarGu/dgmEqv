
import matplotlib.pyplot as plt

Country = ['China', 'India', 'USA', 'UK']
Crops = [200, 180, 120, 100]
Livestock = [100, 90, 70, 50]

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.bar(Country, Crops, width=0.4, label='Crops(million tons)', color='red')
ax.bar(Country, Livestock, width=0.4, bottom=Crops, label='Livestock(million tons)', color='orange')
ax.set_title('Agricultural production of crops and livestock in four countries in 2021')
ax.set_xlabel('Country')
ax.set_xticks(Country)
ax.set_xticklabels(Country, rotation=45, ha="right", fontsize=8)
ax.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.grid(linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('bar chart/png/297.png')
plt.clf()