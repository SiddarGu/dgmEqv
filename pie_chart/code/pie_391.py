
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.figure(figsize=(8,8))
ax = plt.subplot()
labels=['Fruits','Vegetables','Grains','Dairy Products','Livestock','Other']
sizes=[20,25,15,15,15,10]
colors=['#ffe400','#ff7e00','#6ac98a','#1aacd6','#6b3d9a','#fadf80']
explode=[0,0,0,0,0,0]
ax.pie(sizes, explode=explode, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True)
ax.axis('equal')
ax.set_title('Distribution of Agricultural Production in the USA, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/234.png')
plt.clf()