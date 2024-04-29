
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot()
labels=['USA','UK','Germany','France']
housing=[200,180,220,190]
stock=[100,110,120,130]
width=0.4
rects1=ax.bar(labels,housing,width,label='Housing Prices(million)')
rects2=ax.bar(labels,stock,width,bottom=housing,label='Stock Prices(million)')
ax.set_title('Housing and Stock Prices in four countries in 2021')
ax.legend()
ax.set_xticklabels(labels,rotation=45,va='top',ha='right',wrap=True)
ax.set_xticks(range(len(labels)))
plt.tight_layout()
plt.savefig('bar chart/png/474.png')
plt.clf()