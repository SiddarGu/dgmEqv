
import matplotlib.pyplot as plt 
import matplotlib as mpl 

fig = plt.figure(figsize=(10,6))
ax=fig.add_subplot(1,1,1) 

labels=['Cloud Computing','Machine Learning','Artificial Intelligence','Big Data','Blockchain','Augmented Reality']
sizes=[25,20,20,15,10,10]
explode=[0.1,0,0,0,0,0]

ax.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90,textprops={'fontsize':14},wedgeprops={'linewidth':1.5,'edgecolor':'black'})

ax.set_title("Technology Types Used in the Global Market in 2023",fontsize=15)
plt.legend(labels,bbox_to_anchor=(1,0.8),loc="center right",fontsize=14)

plt.xticks(rotation=-45,ha='left')
plt.tight_layout()

plt.savefig('pie chart/png/306.png')
plt.clf()