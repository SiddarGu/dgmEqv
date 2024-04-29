
import matplotlib.pyplot as plt
plt.figure(figsize=(14,6))
ax=plt.subplot()

x=['2015','2016','2017','2018','2019']
Solar=[200,300,400,500,600]
Wind=[800,900,1100,1300,1500]
Hydro=[100,150,200,250,300]
Nuclear=[400,500,600,700,800]

plt.plot(x,Solar,marker='o',label='Solar')
plt.plot(x,Wind,marker='o',label='Wind')
plt.plot(x,Hydro,marker='o',label='Hydro')
plt.plot(x,Nuclear,marker='o',label='Nuclear')

plt.xticks(x)
plt.title('Changes in Energy Production from Renewable and Non-Renewable Sources in the US from 2015-2019')
plt.xlabel('Year')
plt.ylabel('Output(GWh)')
plt.legend(loc='upper left')

for x,y in zip(x,Solar):
    label='{:.0f}'.format(y)
    plt.annotate(label,(x,y),textcoords='offset points',xytext=(0,10),ha='center')
for x,y in zip(x,Wind):
    label='{:.0f}'.format(y)
    plt.annotate(label,(x,y),textcoords='offset points',xytext=(0,10),ha='center')
for x,y in zip(x,Hydro):
    label='{:.0f}'.format(y)
    plt.annotate(label,(x,y),textcoords='offset points',xytext=(0,10),ha='center')
for x,y in zip(x,Nuclear):
    label='{:.0f}'.format(y)
    plt.annotate(label,(x,y),textcoords='offset points',xytext=(0,10),ha='center')

plt.tight_layout()
plt.savefig('line chart/png/75.png')
plt.clf()