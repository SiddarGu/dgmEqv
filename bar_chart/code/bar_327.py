
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

data = np.array([[1000,1100],[900,1300],[1100,1400],[800,1500]])
grade_level = ["Elementary", "Middle", "High School", "College"]
male_students = [1000,900,1100,800]
female_students = [1100,1300,1400,1500]

x = np.arange(len(grade_level))
width = 0.35

ax.bar(x - width/2, male_students, width, label='Male Students', align='center')
ax.bar(x + width/2, female_students, width, label='Female Students', align='center')

ax.set_xticks(x)
ax.set_xticklabels(grade_level, rotation=45, wrap=True)
ax.set_ylabel('Number of Students')
ax.set_title('Number of students by gender at each grade level in 2021')
ax.legend()

plt.tight_layout()
plt.savefig('bar chart/png/104.png')
plt.clf()