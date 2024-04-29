
import matplotlib.pyplot as plt
import numpy as np

grade = np.array(['Grade 5','Grade 6','Grade 7','Grade 8'])
math_score = np.array([85,86,87,89])
read_score = np.array([90,91,93,95])

fig, ax = plt.subplots(figsize=(10,5))
ax.bar(grade, math_score, width=0.4, color='b', label='Math', bottom=read_score)
ax.bar(grade, read_score, width=0.4, color='y', label='Reading')

ax.set_title('Average Math and Reading scores by Grade in 2021')
ax.set_xlabel('Grade')
ax.set_ylabel('Score')

ax.set_xticks(grade)

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

for x, y in zip(grade, math_score):
    ax.annotate(y, (x, y+1), ha='center', va='bottom')

for x, y in zip(grade, read_score):
    ax.annotate(y, (x, y+1), ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/529.png')
plt.clf()