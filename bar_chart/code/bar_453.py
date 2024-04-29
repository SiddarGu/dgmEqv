
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(10,7))
ax=fig.add_subplot(111)
country=['USA','UK','Germany','France']
crop=[1000,800,900,1100]
livestock=[5000,4500,4000,5500]

width=0.4
ax.bar(country,crop,width,label='Crops(tons)')
ax.bar(country,livestock,width,bottom=crop,label='Livestock(heads)')

ax.set_title('Crop and Livestock Production in Four Countries in 2021')
ax.set_xticklabels(country,rotation=45,ha="right",rotation_mode="anchor")
ax.legend(loc='best')

plt.tight_layout()
plt.savefig('bar chart/png/146.png')
plt.clf()