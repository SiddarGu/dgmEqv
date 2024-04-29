
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax=plt.subplot(1,1,1)
ax.bar(['USA','UK','Germany','France'],[20000,18000,15000,14000],bottom=0,label='Lawyers',width=0.4,align='center',color='b')
ax.bar(['USA','UK','Germany','France'],[5000,4000,3500,3000],bottom=0,label='Courts',width=0.4,align='center',color='r')
plt.xticks(['USA','UK','Germany','France'], rotation='vertical')
for a,b in zip(['USA','UK','Germany','France'],[20000,18000,15000,14000]):
    plt.text(a,b+500,'%s'%round(b,1),ha='center',va='bottom',fontsize=11)
for a,b in zip(['USA','UK','Germany','France'],[5000,4000,3500,3000]):
    plt.text(a,b+500,'%s'%round(b,1),ha='center',va='bottom',fontsize=11)
plt.xlabel('Country')
plt.ylabel('Number of Lawyers and Courts')
plt.title('Number of Lawyers and Courts in four countries in 2021')
plt.legend(loc='upper left',bbox_to_anchor=(1,1))
plt.tight_layout()
plt.savefig('bar chart/png/193.png',dpi=300)
plt.clf()