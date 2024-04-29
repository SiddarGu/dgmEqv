
import matplotlib.pyplot as plt
import numpy as np

grade_data = np.array([[80, 90, 85],
                       [90, 85, 95],
                       [95, 80, 90],
                       [75, 95, 85]])

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.set_title('Academic Performance in Math, Science, and Language in Grade 1-4')
ax.set_xlabel('Grade')
ax.set_ylabel('Scores')
ax.set_xticks(np.arange(1, 5, 1))
ax.plot(grade_data[:,0], label='Math Scores')
ax.plot(grade_data[:,1], label='Science Scores')
ax.plot(grade_data[:,2], label='Language Scores')
ax.legend(loc="best")
plt.tight_layout()
plt.savefig('line chart/png/326.png')
plt.clf()