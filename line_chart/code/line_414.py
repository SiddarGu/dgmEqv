
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)
ax.set_title('Average score of students in grades 5-12')

grade = ['5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th']
score = [70, 80, 90, 95, 92, 90, 88, 85]

ax.plot(grade, score, color='#4169E1', marker='o', lw=2.5)
ax.set_xlabel('Grade')
ax.set_ylabel('Average Score')

plt.xticks(grade, rotation=45, fontsize=10, ha='right')
ax.tick_params(axis='both', which='major', labelsize=10)

ax.grid(color='#CDCDCD', linestyle='--', linewidth=1)

ax.text(7.2, 92, '92', fontsize=10, bbox=dict(facecolor='#4169E1', alpha=0.2))
ax.text(7.2, 88, '88', fontsize=10, bbox=dict(facecolor='#4169E1', alpha=0.2))
ax.text(7.2, 85, '85', fontsize=10, bbox=dict(facecolor='#4169E1', alpha=0.2))

plt.tight_layout()

plt.savefig('line chart/png/48.png')
plt.clf()