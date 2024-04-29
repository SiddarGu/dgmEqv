
import matplotlib.pyplot as plt
import numpy as np

#Data
year = np.array([2001,2002,2003,2004,2005])
storage = np.array([1000,2000,3000,4000,5000])
transfer = np.array([50,100,150,200,250])

#Plot
fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(111)

ax1.plot(year, storage, label="Data Storage", color = 'b', linestyle = '-', marker = 'o')
ax1.plot(year, transfer, label="Data Transfer", color = 'r', linestyle = '-', marker = 'o')
ax1.set_title("Increase of data Storage and Transfer Speeds of Computers from 2001 to 2005")
ax1.set_xlabel('Year')
ax1.set_ylabel('Data Storage/Transfer in MB/s')
ax1.set_xticks(year)

for x, y1, y2 in zip(year, storage, transfer):
    ax1.annotate('%s\n%s' % (y1, y2), xy=(x,y1), xytext=(0,5), 
        textcoords="offset points", ha='center', va='bottom')

ax1.legend(loc=2)
fig.tight_layout()
plt.savefig('line chart/png/494.png')
plt.clf()