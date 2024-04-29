

import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
ax = plt.subplot()
ax.set_title('Growth in Number of Employees and Training Hours at ABC Company')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Employees/Training Hours')
ax.plot([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018], [500, 600, 650, 700, 750, 800, 850, 900], linestyle='solid', label='Number of Employees')
ax.plot([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018], [100, 110, 115, 120, 125, 130, 135, 140], linestyle='dashed', label='Training Hours')
ax.legend()
ax.grid(True, linestyle='dashed')
for x, y, z in zip([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018], [500, 600, 650, 700, 750, 800, 850, 900], [100, 110, 115, 120, 125, 130, 135, 140]):
    ax.annotate('{}/{}'.format(y,z), xy=(x, y), xytext=(20, 0), textcoords='offset points', rotation=45, ha='right')
plt.xticks([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018])
plt.tight_layout()
plt.savefig('line chart/png/16.png')
plt.clf()