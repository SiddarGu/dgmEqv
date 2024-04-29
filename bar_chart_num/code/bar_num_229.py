
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,4))
ax = fig.add_subplot()
plt.title('GDP and Unemployment Rate of four countries in 2021')
label = ['USA','UK','Germany','France']
GDP = [21,3,4,2.7]
UnemploymentRate = [5,4,6,8]
plt.bar(label, GDP, label='GDP', bottom=UnemploymentRate, width=0.6, align="edge")
plt.bar(label, UnemploymentRate, label='Unemployment Rate', width=0.6, align="edge")
plt.xticks(rotation=45)
ax.annotate('{}'.format(GDP[0]), xy=(0,GDP[0]/2+UnemploymentRate[0]/2), size=14)
ax.annotate('{}'.format(GDP[1]), xy=(1,GDP[1]/2+UnemploymentRate[1]/2), size=14)
ax.annotate('{}'.format(GDP[2]), xy=(2,GDP[2]/2+UnemploymentRate[2]/2), size=14)
ax.annotate('{}'.format(GDP[3]), xy=(3,GDP[3]/2+UnemploymentRate[3]/2), size=14)
plt.legend(bbox_to_anchor=(1, 1), loc='upper right', ncol=1)
plt.tight_layout()
plt.savefig('Bar Chart/png/274.png',dpi=300)
plt.clf()