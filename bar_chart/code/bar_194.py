
import matplotlib.pyplot as plt
import numpy as np

Level = ["Primary", "Secondary", "College", "University"]
Students = [200, 160, 110, 80]
AverageScore = [85, 90, 95, 97]

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(1, 1, 1)
ax.bar(Level, Students, 0.5, label="Students", color="lightblue")
ax.bar(Level, AverageScore, 0.5, label="AverageScore", color="orange", bottom=Students)

ax.set_title('Number of students and average score of education levels in 2021')
ax.set_xlabel("Level")
ax.set_ylabel("Number")
ax.legend(loc="upper center")
ax.set_xticks(np.arange(len(Level)) + 0.25)
ax.set_xticklabels(Level, rotation=45, ha="right", wrap=True)

fig.tight_layout()
fig.savefig("bar chart/png/14.png", dpi=100)

plt.clf()