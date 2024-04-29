
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax=plt.subplot()
ax.bar(x=['USA','UK','Germany','France'],height=[25,30,20,15],label='Tourists (million)',width=0.3,color='#3F51B5')
ax.bar(x=['USA','UK','Germany','France'],height=[70,75,60,65],bottom=[25,30,20,15],label='Hotel Occupancy (%)',width=0.3,color='#FF9800')
ax.bar(x=['USA','UK','Germany','France'],height=[200,220,180,160],bottom=[95,105,80,80],label='Restaurant Revenue ($million)',width=0.3,color='#4CAF50')
ax.set_xticks(['USA','UK','Germany','France'])
ax.set_title('Tourism and hospitality indicators in four countries in 2021')
ax.legend(loc='upper center')
plt.tight_layout()
for x,y in zip(['USA','UK','Germany','France'], [95,105,80,80]):
    ax.annotate('{}'.format(y), xy=(x,y/2), xytext=(0,3),  # 3 points vertical offset
                textcoords="offset points", ha='center', va='bottom')
for x,y in zip(['USA','UK','Germany','France'], [25,30,20,15]):
    ax.annotate('{}'.format(y), xy=(x,y/2), xytext=(0,3),  # 3 points vertical offset
                textcoords="offset points", ha='center', va='bottom')
for x,y in zip(['USA','UK','Germany','France'], [270,295,260,240]):
    ax.annotate('{}'.format(y), xy=(x,y/2), xytext=(0,3),  # 3 points vertical offset
                textcoords="offset points", ha='center', va='bottom')
plt.savefig('Bar Chart/png/287.png')
plt.clf()