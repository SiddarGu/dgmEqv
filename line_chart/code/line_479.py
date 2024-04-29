
import matplotlib.pyplot as plt
import numpy as np

data = [[2011, 45, 60, 30], [2012, 50, 70, 35], [2013, 55, 75, 40], 
        [2014, 60, 80, 45], [2015, 65, 85, 50], [2016, 70, 90, 55]]

#load data
year = np.array(data)[:,0]
smartphone = np.array(data)[:,1]
computer = np.array(data)[:,2]
tablet = np.array(data)[:,3]

#plot
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()
ax.plot(year, smartphone, label='Smartphone', marker='o')
ax.plot(year, computer, label='Computer', marker='o')
ax.plot(year, tablet, label='Tablet', marker='o')

#style
ax.set_title('Global Market Share of Smartphones, Computers and Tablets from 2011 to 2016')
ax.set_xlabel('Year')
ax.set_ylabel('Market Share')
ax.set_xticks(year)
ax.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)
plt.tight_layout()

#save
plt.savefig('line chart/png/59.png')

#clear
plt.clf()