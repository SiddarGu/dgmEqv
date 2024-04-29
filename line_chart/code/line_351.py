
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot()

grade = [1, 2, 3, 4]
reading_score = [90, 85, 80, 95]
math_score = [80, 90, 95, 85]
science_score = [95, 90, 85, 95]

ax.plot(grade, reading_score, label="Reading Score", marker="o", color="red")
ax.plot(grade, math_score, label="Math Score", marker="v", color="green")
ax.plot(grade, science_score, label="Science Score", marker="s", color="blue")

ax.set_xticks(grade)
ax.set_title("Reading, Math and Science scores of students in Grade 1-4")
ax.legend(loc="best", ncol=3, frameon=False)

plt.tight_layout()
plt.savefig("line chart/png/421.png")
plt.clf()