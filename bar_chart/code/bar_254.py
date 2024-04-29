
import matplotlib.pyplot as plt
import numpy as np

data = [[2020,180,2500],
        [2021,220,3000],
        [2022,240,3500],
        [2023,280,4000]]

years= [row[0] for row in data]
inventions = [row[1] for row in data]
papers = [row[2] for row in data]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

ax.bar(years, inventions, width=0.4, label='Inventions', color='#D0E8CF', edgecolor='black')
ax.bar(years, papers, width=0.4, label='Research papers', color='#08BDBD', bottom=inventions, edgecolor='black')

ax.set_xticks(years)
ax.set_title('Number of inventions and research papers from 2020 to 2023')
ax.legend(loc='upper left')
plt.tight_layout()

plt.savefig('bar chart/png/94.png')
plt.clf()