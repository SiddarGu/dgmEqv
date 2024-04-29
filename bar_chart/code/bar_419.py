
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

ax.set_title('Academic Scores of Students in Grades 8 to 11')
ax.set_xlabel('Grade')
ax.set_ylabel('Scores')

grades = ['Grade 8', 'Grade 9', 'Grade 10', 'Grade 11']
math_score = [75, 85, 90, 95]
science_score = [80, 90, 95, 100]
english_score = [90, 95, 80, 90]

ax.bar(grades, math_score, label='Math Score', width=0.2, color='blue')
ax.bar(grades, science_score, label='Science Score', width=0.2, bottom=math_score, color='orange')
ax.bar(grades, english_score, label='English Score', width=0.2, bottom=[m+s for m,s in zip(math_score, science_score)], color='green')

plt.xticks(grades, rotation=45, fontsize=12, wrap=True)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=3, fontsize=13)

plt.tight_layout()

plt.savefig('bar chart/png/162.png')

plt.clf()