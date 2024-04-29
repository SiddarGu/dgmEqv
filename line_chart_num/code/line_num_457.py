
import matplotlib.pyplot as plt
import numpy as np

data_list = [[2015,40000,25000],[2016,45000,30000],[2017,50000,35000],[2018,60000,40000],[2019,55000,30000],[2020,60000,40000]]
years = [data[0] for data in data_list]
num_filed = [data[1] for data in data_list]
num_settled = [data[2] for data in data_list]

fig = plt.figure(figsize=(15,12))
ax = fig.add_subplot(111)

ax.plot(years, num_filed, c='b', label='Number of Lawsuits Filed')
ax.plot(years, num_settled, c='r', label='Number of Lawsuits Settled')

ax.set_xticks(years)
ax.set_title('Changes in Lawsuits Filed and Settled in the US from 2015-2020')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Lawsuits')
ax.legend(loc='upper left', fontsize=14)

for i,j in zip(years,num_filed):
    ax.annotate(str(j), xy=(i,j+300), rotation=45)

for i,j in zip(years,num_settled):
    ax.annotate(str(j), xy=(i,j+300), rotation=45)

plt.tight_layout()
plt.savefig('line chart/png/146.png')
plt.cla()