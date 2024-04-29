
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
plt.figure(figsize=(8,8))
labels=['Cloud Computing','Artificial Intelligence','Internet of Things','Big Data','Cyber Security']
sizes=[25,20,30,15,10]
colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#e6e6e6']
explode=(0.1,0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',startangle=90)
plt.title('Distribution of Technology Services in the Global Market, 2023',fontsize=20)
plt.axis('equal')
plt.legend(labels,bbox_to_anchor=(1.10, 1.0))
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig('pie chart/png/91.png')
plt.clf()