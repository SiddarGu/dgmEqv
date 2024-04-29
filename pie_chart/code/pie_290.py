
import matplotlib.pyplot as plt 
fig=plt.figure(figsize=(8,8)) 
ax=fig.add_subplot(111) 
labels=['Education', 'Healthcare', 'Housing', 'Economy', 'Environment','Social and Community Well-being'] 
sizes=[20,25,18,15,12,10] 
explode=[0,0.1,0,0,0,0] 
ax.pie(sizes,explode=explode,labels=labels,autopct='%.2f %%',shadow=True,startangle=90) 
ax.axis('equal') 
ax.set_title('Quality of Life in the USA in 2023',fontsize=20,y=1.08) 
plt.xticks(rotation=30) 
plt.tight_layout() 
plt.savefig("pie chart/png/186.png") 
plt.clf()