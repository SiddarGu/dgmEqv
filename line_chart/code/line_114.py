
import matplotlib.pyplot as plt
import numpy as np

Grade = np.array([5,6,7,8,9,10])
Math_Score = np.array([90,95,85,95,90,85])
English_Score = np.array([85,90,95,90,80,85])
Science_Score = np.array([75,80,75,85,75,80])

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.plot(Grade, Math_Score, label='Math Score')
ax.plot(Grade, English_Score, label='English Score')
ax.plot(Grade, Science_Score, label='Science Score')
ax.set_title('Student Scores by Grade in Math, English, and Science')
plt.xticks(Grade)
ax.legend(loc='upper left')
plt.tight_layout()
ax.set_xlabel('Grade')
ax.set_ylabel('Scores')
fig.savefig('line chart/png/328.png')
plt.clf()