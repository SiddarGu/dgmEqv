
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

data = [[2017, 1500, 1200],
        [2018, 1600, 1300],
        [2019, 1700, 1400],
        [2020, 1800, 1500]]

x_pos = np.arange(len(data))
bar_width = 0.35

ax.bar(x_pos, [i[1] for i in data], bar_width, label="Research Papers")
ax.bar(x_pos+bar_width, [i[2] for i in data], bar_width, label="Patents")

ax.set_xticks(x_pos+bar_width/2)
ax.set_xticklabels([i[0] for i in data], rotation=45, ha="right")
ax.set_title('Number of research papers and patents from 2017 to 2020')
ax.set_xlabel('Year')
ax.set_ylabel('Number')
ax.legend()

fig.tight_layout()
plt.savefig('bar chart/png/442.png')
plt.clf()