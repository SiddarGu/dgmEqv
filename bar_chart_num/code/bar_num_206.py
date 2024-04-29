
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(12,8))
ax=fig.add_subplot()
x=["USA","UK","Germany","France"]
hospitals=[150,170,140,160]
staffs=[25000,26000,23000,24000]
ax.bar(x,hospitals,label="Hospitals",bottom=staffs,color='#00aaff',alpha=0.7)
ax.bar(x,staffs,label="Staff",color='#ffaa00',alpha=0.7)
for i,j in zip(x,hospitals):
    ax.annotate(str(j),xy=(i,j),ha='center',va='center',color='black',fontsize=12)
for i,j in zip(x,staffs):
    ax.annotate(str(j),xy=(i,j),ha='center',va='center',color='black',fontsize=12)
ax.set_title("Number of hospitals and staffs in four countries in 2021",fontsize=15)
ax.set_xticks(x)
ax.set_ylabel("Number")
ax.legend(loc="upper right")
plt.tight_layout()
plt.savefig('Bar Chart/png/179.png')
plt.clf()