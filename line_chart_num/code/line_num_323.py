
import matplotlib.pyplot as plt
import numpy as np

grade = ['4th Grade', '5th Grade', '6th Grade', '7th Grade', '8th Grade']
average_score =[87, 91, 95, 90, 92]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

ax.plot(grade, average_score, color='#008080', marker='o', linestyle='--', lw=3, label='Average Score')
ax.set_xticklabels(grade, rotation=45, fontsize=12, ha='right')
ax.set_title('Average scores of students in 4th to 8th grades', fontsize=14, fontweight='bold')
ax.set_xlabel('Grade', fontsize=14)
ax.set_ylabel('Average Score', fontsize=14)
ax.legend(loc='upper center', fontsize=14, frameon=True, shadow=True, framealpha=1)

for i, txt in enumerate(average_score):
    ax.annotate(txt, (grade[i], average_score[i]), fontsize=14)

plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('line chart/png/219.png')
plt.clf()