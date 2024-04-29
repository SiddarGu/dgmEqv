
import matplotlib.pyplot as plt
plt.figure(figsize=(10,7))
ax = plt.subplot(aspect="equal")
lables = ['Financial Services','Manufacturing','Retail','E-commerce','Transportation','Energy','Construction']
sizes = [25,20,18,15,10,7,5]
explode = (0.1,0,0,0,0,0,0)
ax.pie(sizes, labels=lables, autopct='%.2f%%', startangle=90,explode=explode)
ax.set_title('Distribution of Industries in the US Economy, 2023',fontsize=14)
ax.legend(lables,bbox_to_anchor=(1,0.5),loc="center right",fontsize=11)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('pie chart/png/396.png')
plt.clf()