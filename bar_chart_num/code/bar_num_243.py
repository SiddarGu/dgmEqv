
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

grade = [1, 2, 3, 4]
math_scores = [90, 85, 88, 80]
english_scores = [93, 89, 92, 87]
science_scores = [95, 90, 92, 93]

bar_width = 0.2

ax.bar(grade, math_scores, width=bar_width, label='Math', color='blue', bottom=english_scores)
ax.bar(grade, english_scores, width=bar_width, label='English', color='orange', bottom=science_scores)
ax.bar(grade, science_scores, width=bar_width, label='Science', color='green')

ax.set_title('Academic Performance in Math, English and Science of Four Grades in 2021')
ax.set_ylabel('Scores(%)')
ax.set_xlabel('Grades')

ax.legend()
ax.set_xticks(grade)

for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + 0.2, p.get_height() + 0.1))

plt.tight_layout()
plt.savefig('Bar Chart/png/200.png')
plt.clf()