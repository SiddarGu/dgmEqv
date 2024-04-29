
import matplotlib.pyplot as plt

data = [[2009, 500, 4000], [2010, 600, 4500], [2011, 700, 5000],
        [2012, 800, 5500], [2013, 900, 6000], [2014, 1000, 6500],
        [2015, 1200, 7000], [2016, 1400, 7500], [2017, 1600, 8000],
        [2018, 1800, 8500], [2019, 2000, 9000]]

years, online, offline = zip(*data)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)
ax.plot(years, online, label='Online Sales(billion dollars)')
ax.plot(years, offline, label='Offline Sales(billion dollars)')

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)
ax.set_title('Global Retail Sales from 2009-2019')
ax.set_xlabel('Year')
ax.set_ylabel('Sales(billion dollars)')
ax.set_xticks(years)
ax.legend(loc='best')

plt.tight_layout()
plt.savefig('line chart/png/221.png')
plt.clf()