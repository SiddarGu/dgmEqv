
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax=plt.subplot()
labels=['Clinical Care','Administrative Services','Research and Development','Other Services','Prevention and Public Health']
sizes=[60,15,10,10,5]
explode=(0.1,0,0,0,0)
ax.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax.axis('equal')
ax.set_title('Distribution of Healthcare Services in the USA, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/391.png')
plt.clf()