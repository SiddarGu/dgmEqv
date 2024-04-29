
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,5))

x = np.arange(4)
research_papers = [300, 320, 340, 360]
patents = [100, 120, 140, 160]

ax = plt.subplot()
ax.bar(x-0.2, research_papers, width=0.4, label='Research Papers')
ax.bar(x+0.2, patents, width=0.4, label='Patents')

ax.set_xticks(x)
ax.set_xticklabels(['2020', '2021', '2022', '2023'])
ax.set_title('Number of research papers and patents in science and engineering from 2020 to 2023')
ax.legend(loc='center right', bbox_to_anchor=(1.3, 0.5))
ax.grid(axis='y')

plt.tight_layout()
plt.savefig('bar chart/png/96.png', dpi=96)

plt.clf()