
import matplotlib.pyplot as plt
import numpy as np

# set up figure
fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(111)

# set up data
data = np.array([[2011, 20, 10, 50], 
                 [2012, 25, 15, 45], 
                 [2013, 30, 20, 40],
                 [2014, 35, 25, 35],
                 [2015, 40, 30, 30],
                 [2016, 45, 35, 25],
                 [2017, 50, 40, 20]])

# plot data
x = data[:,0]
ax.plot(x, data[:,1], label='Smartphone Ownership Rate(%)', linestyle='-', marker='o', markersize=7)
ax.plot(x, data[:,2], label='Tablet Ownership Rate(%)', linestyle='-', marker='s', markersize=7)
ax.plot(x, data[:,3], label='Desktop Computer Ownership Rate(%)', linestyle='-', marker='^', markersize=7)

# set up the labels
ax.set_xlabel('Year')
ax.set_ylabel('Ownership Rate(%)')
ax.set_title('Trends of Device Ownership Rate in the U.S. from 2011-2017')
ax.grid(True, linestyle='--', color='black', alpha=0.2)
ax.legend(loc='lower right')

# annotate data points
for i, txt in enumerate(data[:,1]):
    ax.annotate(txt, (x[i],data[i,1]), xytext=(x[i]+0.2,data[i,1]), fontsize=10)

for i, txt in enumerate(data[:,2]):
    ax.annotate(txt, (x[i],data[i,2]), xytext=(x[i]+0.2,data[i,2]), fontsize=10)

for i, txt in enumerate(data[:,3]):
    ax.annotate(txt, (x[i],data[i,3]), xytext=(x[i]+0.2,data[i,3]), fontsize=10)

# set up x ticks
plt.xticks(x)
plt.tight_layout()

# save the figure
plt.savefig('line chart/png/122.png')
plt.clf()