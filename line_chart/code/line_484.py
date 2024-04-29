
import matplotlib.pyplot as plt

data = [[2011,50,40],
        [2012,60,45],
        [2013,70,55],
        [2014,80,60],
        [2015,90,65],
        [2016,95,70],
        [2017,98,75],
        [2018,100,80]]

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

years = [d[0] for d in data]
smartphone_usage = [d[1] for d in data]
computer_usage = [d[2] for d in data]

ax.plot(years, smartphone_usage, label="Smartphone Usage")
ax.plot(years, computer_usage, label="Computer Usage")

ax.set_title('Increase in usage of Smartphones and Computers from 2011-2018')
ax.set_xlabel('Year')
ax.set_ylabel('Usage %')

ax.legend(loc='lower right')
ax.set_xticks(years)

plt.tight_layout()
plt.savefig('line chart/png/5.png')

plt.clf()