
import matplotlib.pyplot as plt
import numpy as np

region = ['North America', 'South America', 'Europe', 'Asia']
research_institutions = [50, 25, 75, 100]
laboratories = [90, 70, 120, 150]
engineers = [1500, 1200, 1100, 1300]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()

ax.bar(region, research_institutions, label='Research Institutions')
ax.bar(region, laboratories, bottom=research_institutions, label='Laboratories')
ax.bar(region, engineers, bottom=np.array(research_institutions)+np.array(laboratories), label='Engineers')

ax.set_xticks(region)
ax.set_title('Number of research institutions, laboratories, and engineers in four regions in 2021')
ax.set_xlabel('Region')
ax.set_ylabel('Number')

ax.legend(loc='upper left')

for i, v in enumerate(research_institutions):
    ax.text(i-0.1, v/2, str(v), color='white', fontweight='bold')
for i, v in enumerate(laboratories):
    ax.text(i-0.1, research_institutions[i] + v/2, str(v), color='white', fontweight='bold')
for i, v in enumerate(engineers):
    ax.text(i-0.1, research_institutions[i] + laboratories[i] + v/2, str(v), color='white', fontweight='bold')

plt.tight_layout()
plt.savefig('Bar Chart/png/472.png')
plt.clf()