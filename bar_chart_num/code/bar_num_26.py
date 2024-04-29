
import matplotlib.pyplot as plt
import numpy as np

discipline = np.array(['Psychology','Sociology','Economics','Anthropology'])
publications = np.array([1400,1800,1600,1320])
citations = np.array([6000,7200,6800,6400])

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()
ax.bar(discipline,publications,bottom=citations,label='Publications')
ax.bar(discipline,citations,label='Citations')
ax.set_title('Number of publications and citations in four disciplines of Social Sciences and Humanities in 2021')
ax.set_xlabel('Discipline')
ax.legend()

for i, v in enumerate(publications):
    ax.text(discipline[i], v/2+citations[i], str(v), fontsize=10, color='black', va='center', ha='center')
for i, v in enumerate(citations):
    ax.text(discipline[i], v/2, str(v), fontsize=10, color='black', va='center', ha='center')

plt.xticks(discipline, [str(i) for i in discipline])
plt.tight_layout()
plt.savefig('Bar Chart/png/214.png')
plt.clf()