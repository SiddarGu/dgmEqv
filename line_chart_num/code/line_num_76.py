
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))
plt.title("Academic Performance in Reading, Math, and Science by Grade Level")
ax = fig.add_subplot()

grade_level = ["5th", "6th", "7th", "8th"]
reading_score = [85, 88, 90, 92]
math_score = [86, 87, 88, 92]
science_score = [87, 89, 91, 93]

plt.plot(grade_level, reading_score, label="Reading")
plt.plot(grade_level, math_score, label="Math")
plt.plot(grade_level, science_score, label="Science")

plt.xticks(grade_level)
plt.xlabel("Grade Level")
plt.ylabel("Scores")

for a, b, c, d in zip(grade_level, reading_score, math_score, science_score):
    plt.annotate(d, xy=(a, c+1), xytext=(a, c+1))

plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig("line chart/png/243.png")
plt.clf()