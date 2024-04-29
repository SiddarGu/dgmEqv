
import matplotlib.pyplot as plt
import numpy as np

grade = np.array(['6th', '7th', '8th', '9th', '10th', '11th', '12th'])
number_of_students = np.array([150, 200, 250, 300, 350, 400, 450])
average_GPA = np.array([3.2, 3.5, 3.8, 3.9, 4.0, 3.7, 3.5])

plt.figure(figsize=(10, 7))
ax = plt.subplot()

ax.plot(grade, number_of_students, label="Number of Students", color='green', marker='o', markerfacecolor='green', markersize=8)
ax.plot(grade, average_GPA, label="Average GPA", color='blue', marker='o', markerfacecolor='blue', markersize=8)

ax.set_title("Academic Performance in Different Grades at a High School")
ax.set_xlabel("Grade")
ax.set_ylabel("Average GPA & Number of Students")

ax.legend()

plt.xticks(grade)

for a, b in zip(grade, average_GPA):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=12)

for a, b in zip(grade, number_of_students):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.savefig('line chart/png/242.png')
plt.clf()