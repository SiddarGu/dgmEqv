
import matplotlib.pyplot as plt
import numpy as np

year = np.array([2000, 2001, 2002, 2003, 2004])
commuted = np.array([35, 32, 45, 42, 37])
pardoned = np.array([40, 45, 50, 55, 60])
reduced = np.array([30, 25, 40, 45, 50])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
ax.plot(year, commuted, label="Sentences Commuted")
ax.plot(year, pardoned, label="Sentences Pardoned")
ax.plot(year, reduced, label="Prison Sentences Reduced")

ax.set_xlabel('Year')
ax.set_ylabel('Number of Clemency Actions')
ax.set_title('Presidential Clemency Actions in the United States from 2000 to 2004')
ax.set_xticks(year)
ax.grid(linestyle='--')
ax.legend(loc='upper left', bbox_to_anchor=(-0.1, 1.0))
fig.tight_layout()

fig.savefig('line chart/png/204.png')
plt.clf()