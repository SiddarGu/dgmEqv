
import matplotlib.pyplot as plt
plt.figure(figsize=(10,7))
ax = plt.subplot()
ax.bar(x=['USA','UK','Germany','France'],height=[250,200,220,230],label='Literature',width=0.3,bottom=0,align='edge')
ax.bar(x=['USA','UK','Germany','France'],height=[120,130,140,150],label='Philosophy',width=0.3,bottom=[250,200,220,230],align='edge')
ax.bar(x=['USA','UK','Germany','France'],height=[170,150,180,190],label='History',width=0.3,bottom=[370,330,360,380],align='edge')
plt.xticks(rotation=0)
ax.set_title('Number of publications in social sciences and humanities in four countries in 2021', fontsize=16)
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('bar chart/png/350.png')
plt.clf()