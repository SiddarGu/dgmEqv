
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.plot(['2010','2011','2012','2013','2014','2015','2016'],[25,27,28,29,30,32,33],marker='o',label='Tax Rate')
ax.plot(['2010','2011','2012','2013','2014','2015','2016'],[600,650,700,750,800,850,900],marker='o',label='Government Spending(billion dollars)')
ax.legend(loc='upper left', bbox_to_anchor=(1,1))
for a,b in zip(['2010','2011','2012','2013','2014','2015','2016'],[25,27,28,29,30,32,33]): 
    ax.annotate(str(b)+'%',xy=(a,b))
for c,d in zip(['2010','2011','2012','2013','2014','2015','2016'],[600,650,700,750,800,850,900]): 
    ax.annotate(str(d)+'$',xy=(c,d))
ax.set_xticks(['2010','2011','2012','2013','2014','2015','2016'])
ax.set_xlabel('Year')
ax.set_title('Changes in Tax Rate and Government Spending in the US from 2010 to 2016')
plt.tight_layout()
plt.savefig('line chart/png/89.png')
plt.clf()