
import matplotlib.pyplot as plt
import numpy as np

grade = np.array(['5th','6th','7th','8th'])
ave_score = np.array([80,82,84,86])
pass_rate = np.array([60,70,80,90])

fig,ax = plt.subplots(figsize=(12,6))

ax.plot(grade,ave_score,label='Average Score',marker='o',linestyle='-')
ax.plot(grade,pass_rate,label='Passing Rate',marker='o',linestyle='-')

ax.set_title('Average score and passing rate of students in 5th to 8th grade',fontsize=14)
ax.set_xlabel('Grade',fontsize=12)
ax.set_ylabel('Score',fontsize=12)

ax.xaxis.set_tick_params(labelsize=10)
ax.yaxis.set_tick_params(labelsize=10)
ax.set_xticks(np.arange(len(grade)))
ax.set_xticklabels(grade)

for i,j in zip(grade,ave_score):
    ax.annotate(str(j),xy=(i,j-1))
for i,j in zip(grade,pass_rate):
    ax.annotate(str(j),xy=(i,j-2))

ax.legend()

plt.tight_layout()
plt.savefig('line chart/png/478.png',dpi=200)

plt.clf()