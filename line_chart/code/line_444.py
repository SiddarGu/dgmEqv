
import matplotlib.pyplot as plt
import pandas as pd 

fig=plt.figure(figsize=(15,5))
ax=fig.add_subplot(111)
data=[[1,1000],[2,1100],[3,1200],[4,1300],[5,1400],[6,1500],[7,1600],[8,1700],[9,1800],[10,1900],[11,2000],[12,2100]]
df=pd.DataFrame(data,columns=['Month','Average salary'])
ax.plot(df['Month'],df['Average salary'],color='#ff6347',marker='o',linestyle='-',markersize=7)
ax.set_xticks(df['Month'])
ax.set_xlabel('Month',fontsize=14)
ax.set_ylabel('Average salary',fontsize=14)
ax.set_title('Average salary of employees in a company from January to December 2021',fontsize=14,wrap=True)
plt.grid(axis='y',linestyle='-.')
plt.tight_layout()
plt.savefig('line chart/png/151.png')
plt.clf()