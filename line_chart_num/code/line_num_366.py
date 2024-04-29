
import matplotlib.pyplot as plt

year = [2010, 2011, 2012, 2013, 2014, 2015]
migration_rate = [3.2, 3.5, 3.7, 4.0, 4.2, 4.5]
unemployment_rate = [7.8, 7.4, 7.1, 7.2, 7.4, 7.5]
average_wage = [25000, 26000, 27000, 28000, 29000, 30000]

fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(111)
ax1.set_title('Changes in migration, unemployment and wage in USA from 2010-2015') 
ax1.set_xlabel('Year')
ax1.set_ylabel('Rate')

ax1.plot(year, migration_rate, label = 'Migration Rate(%)', color = 'b', marker = 'o')
ax1.plot(year, unemployment_rate, label = 'Unemployment Rate(%)', color = 'k', marker = 'o')
ax1.plot(year, average_wage, label = 'Average Wage(USD)', color = 'g', marker = 'o')

ax1.set_xticks(year)
ax1.legend(loc = 'best')

for i, txt in enumerate(migration_rate):
    ax1.annotate(txt, (year[i], migration_rate[i]), rotation = 45)
for i, txt in enumerate(unemployment_rate):
    ax1.annotate(txt, (year[i], unemployment_rate[i]), rotation = 45, wrap = True)
for i, txt in enumerate(average_wage):
    ax1.annotate(txt, (year[i], average_wage[i]), rotation = 45)

plt.tight_layout()
plt.savefig('line chart/png/360.png')
plt.clf()