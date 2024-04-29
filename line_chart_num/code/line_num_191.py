
import matplotlib.pyplot as plt
plt.figure(figsize=(14,6))
plt.plot(['2010','2011','2012','2013','2014','2015','2016','2017','2018'], [200000,210000,250000,270000,300000,290000,310000,350000,400000], label='Criminal Cases Filed')
plt.plot(['2010','2011','2012','2013','2014','2015','2016','2017','2018'], [800000,850000,910000,100000,940000,950000,970000,900000,1000000], label='Civil Cases Filed')
plt.title('Increase in Filed Cases in US Legal System from 2010 to 2018')
plt.xlabel('Year')
plt.ylabel('Number of Cases')
plt.xticks(['2010','2011','2012','2013','2014','2015','2016','2017','2018'])
plt.legend(loc='best')
for i,j in zip(['2010','2011','2012','2013','2014','2015','2016','2017','2018'], [200000,210000,250000,270000,300000,290000,310000,350000,400000]):
    plt.annotate(str(j),xy=(i,j),xytext=(0,5), textcoords='offset points',rotation=90, fontsize=10, horizontalalignment='center', verticalalignment='bottom')
for i,j in zip(['2010','2011','2012','2013','2014','2015','2016','2017','2018'], [800000,850000,910000,100000,940000,950000,970000,900000,1000000]):
    plt.annotate(str(j),xy=(i,j),xytext=(0,5), textcoords='offset points',rotation=90, fontsize=10, horizontalalignment='center', verticalalignment='bottom')
plt.tight_layout()
plt.savefig('line chart/png/568.png')
plt.clf()