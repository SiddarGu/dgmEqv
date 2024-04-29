
import matplotlib.pyplot as plt 
import pandas as pd 

#create figure
fig = plt.figure(figsize = (10,8))
ax = fig.add_subplot() 

#load data 
data={'Year':[2010,2011,2012,2013,2014],
    'Average Salary(thousand dollars)':[40,42,44,46,48],
    'Average Working Hours':[40,38,37,36,35],
    'Employment Rate':[75,80,85,90,95]} 

#plot
ax.plot(data['Year'],data['Average Salary(thousand dollars)'],label='Average Salary(thousand dollars)',marker='o')
ax.plot(data['Year'],data['Average Working Hours'],label='Average Working Hours',marker='o')
ax.plot(data['Year'],data['Employment Rate'],label='Employment Rate',marker='o')

#add labels
for i, txt in enumerate(data['Average Salary(thousand dollars)']):
    ax.annotate(txt, (data['Year'][i], data['Average Salary(thousand dollars)'][i]), rotation=45, wrap=True)
for i, txt in enumerate(data['Average Working Hours']):
    ax.annotate(txt, (data['Year'][i], data['Average Working Hours'][i]), rotation=45, wrap=True)
for i, txt in enumerate(data['Employment Rate']):
    ax.annotate(txt, (data['Year'][i], data['Employment Rate'][i]), rotation=45, wrap=True)

#configure plot
ax.grid(True)
ax.set_title('Changes in Employment rate, Average Salary and Working Hours of Employees in the US from 2010 to 2014')
ax.legend(loc = 'best')
ax.set_xlabel('Year')
ax.set_ylabel('Employment rate/Average Salary(thousand dollars)/Average Working Hours')
ax.set_xticks(data['Year'])

#resize
plt.tight_layout()

#save
plt.savefig('line_464.png')

#clear
plt.clf()