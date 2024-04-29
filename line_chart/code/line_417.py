
import matplotlib.pyplot as plt
import numpy as np

data = [[2011, 3000, 5000, 6000, 8000],
        [2012, 3500, 5500, 7000, 9000],
        [2013, 4000, 6000, 8000, 10000],
        [2014, 4500, 6500, 9000, 11000]]

data = np.array(data)

year = data[:,0]
football = data[:,1]
basketball = data[:,2]
baseball = data[:,3]
tennis = data[:,4]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

ax.plot(year, football, linestyle='-', marker='o', label='Football')
ax.plot(year, basketball, linestyle='-', marker='o', label='Basketball')
ax.plot(year, baseball, linestyle='-', marker='o', label='Baseball')
ax.plot(year, tennis, linestyle='-', marker='o', label='Tennis')

plt.title('Popularity of Major Sports in the US from 2011 to 2014')
plt.xlabel('Year')
plt.ylabel('Number of Followers (in Thousands)')
plt.xticks(year)
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.tight_layout()
plt.savefig('line chart/png/549.png')
plt.clf()