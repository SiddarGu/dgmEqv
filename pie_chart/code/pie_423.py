
import matplotlib.pyplot as plt

plt.figure(figsize=(10,8))
ax=plt.subplot()
ax.axis('equal')
labels=['Donations','Grants','Government Funding','Other Charitable Events','Investment Income','Other Sources']
sizes=[45,25,15,5,5,5]
explode=[0.05,0,0,0,0,0]
ax.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',startangle=90)
ax.set_title('Sources of Revenue for Nonprofit Organizations in 2023')
plt.tight_layout()
plt.savefig('pie chart/png/165.png')
plt.clf()