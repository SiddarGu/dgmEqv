
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
ax.plot(['2010','2011','2012','2013','2014','2015','2016'],[1000,1300,1500,1800,2000,2200,2500],'b-',label='Website Users(million)')
ax.plot(['2010','2011','2012','2013','2014','2015','2016'],[500,700,900,1100,1300,1500,1900],'r-',label='Social Media Users(million)')
ax.plot(['2010','2011','2012','2013','2014','2015','2016'],[200,400,700,1000,1500,1800,2000],'g-',label='Online Shopping Users(million)')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Users (million)')
ax.set_title('Increase of Online User Numbers from 2010 to 2016')
ax.legend(loc='upper left',fontsize='medium')
ax.grid(True)
for x,y in zip(['2010','2011','2012','2013','2014','2015','2016'],[1000,1300,1500,1800,2000,2200,2500]):
    ax.annotate(y,xy=(x,y),xytext=(-8,5),textcoords='offset points')
for x,y in zip(['2010','2011','2012','2013','2014','2015','2016'],[500,700,900,1100,1300,1500,1900]):
    ax.annotate(y,xy=(x,y),xytext=(-8,5),textcoords='offset points')
for x,y in zip(['2010','2011','2012','2013','2014','2015','2016'],[200,400,700,1000,1500,1800,2000]):
    ax.annotate(y,xy=(x,y),xytext=(-8,5),textcoords='offset points')
ax.set_xticks(['2010','2011','2012','2013','2014','2015','2016'])
plt.tight_layout()
plt.savefig('line chart/png/598.png')
plt.clf()