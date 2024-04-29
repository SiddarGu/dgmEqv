
import matplotlib.pyplot as plt
import numpy as np

grade = np.array([9, 10, 11, 12])
average_gpa = np.array([3.0, 3.2, 3.4, 3.5])
average_test_score = np.array([55, 60, 65, 70])

fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(111)

ax1.plot(grade, average_gpa, label='Average GPA', marker='o', color='blue', linestyle='solid', linewidth=2)
ax1.plot(grade, average_test_score, label='Average Test Score', marker='o', color='red', linestyle='solid', linewidth=2)

ax1.set_xlabel('Grade')
ax1.set_ylabel('Average GPA & Test Score')
ax1.set_title('Average Academic Performance of High School Students from Grade 9-12')

ax1.legend(loc='upper center')
ax1.set_xticks(grade)
ax1.grid(True)

plt.tight_layout()
plt.savefig("line chart/png/103.png")
plt.clf()