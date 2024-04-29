
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig=plt.figure(figsize=(7,7))
ax=fig.add_subplot()
labels=['Bonds','Equity','Real Estate','Alternative Assets','Cash']
values=[40,25,15,10,10]
explode=(0,0,0,0,0.1)
colors=['#FFD700','#00FA9A','#FFA500','#ADFF2F','#FF0000']
ax.pie(values,explode=explode,labels=labels,autopct='%.2f%%',colors=colors,shadow=True,startangle=60,textprops={'fontsize':12,'color':'k','ha':'left','va':'center'},wedgeprops={'linewidth':2,'width':1,'edgecolor':'k'},pctdistance=0.85)
ax.axis('equal')
ax.set_title("Investment Portfolio Distribution in 2023",{'fontsize':18,'fontweight':'bold'})
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('pie chart/png/469.png')
plt.clf()