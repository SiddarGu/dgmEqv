
import matplotlib.pyplot as plt
import numpy as np

# data
data = np.array([[2000, 2500, 3500, 1000, 1500],
                 [2001, 3000, 4000, 1200, 2000],
                 [2002, 2700, 4500, 1400, 1800],
                 [2003, 2500, 5000, 1700, 2200],
                 [2004, 3000, 4000, 2000, 2500]])

# set fig size
plt.figure(figsize=(10,8))

# create line chart
plt.plot(data[:,0], data[:,1], label='Criminal Cases', color='b', marker='o')
plt.plot(data[:,0], data[:,2], label='Civil Cases', color='r', marker='o')
plt.plot(data[:,0], data[:,3], label='Family Cases', color='g', marker='o')
plt.plot(data[:,0], data[:,4], label='Traffic Cases', color='orange', marker='o')

# add legend
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=5)

# add title
plt.title('Number of Cases in Different Law Fields in US from 2000 to 2004')

# add grid
plt.grid(True, linestyle='--', linewidth=1, alpha=0.3)

# set xticks
plt.xticks(data[:,0])

# add labels
for i, j in zip(data[:,0], data[:,1]):
    plt.annotate(str(j), xy=(i, j), fontsize=12, rotation=45, wrap=True)
for i, j in zip(data[:,0], data[:,2]):
    plt.annotate(str(j), xy=(i, j), fontsize=12, rotation=45, wrap=True)
for i, j in zip(data[:,0], data[:,3]):
    plt.annotate(str(j), xy=(i, j), fontsize=12, rotation=45, wrap=True)
for i, j in zip(data[:,0], data[:,4]):
    plt.annotate(str(j), xy=(i, j), fontsize=12, rotation=45, wrap=True)

# adjust figure
plt.tight_layout()

# save figure
plt.savefig('line chart/png/390.png', dpi=300)

# clear the current image state
plt.clf()