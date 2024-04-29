
import matplotlib.pyplot as plt
import numpy as np

grade = ["1st Grade", "2nd Grade", "3rd Grade", "4th Grade"]
students = [500, 400, 350, 450]
teachers = [35, 30, 25, 35]

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(grade, students, width=0.4, label="Students")
ax.bar(grade, teachers, width=0.4, bottom=students, label="Teachers")
ax.set_title("Number of students and teachers in four grades in 2021")
ax.set_ylabel("Number of People")
ax.legend(loc="upper left")
plt.xticks(grade, rotation=45, wrap=True)
plt.tight_layout()
plt.savefig("bar chart/png/304.png")
plt.clf()