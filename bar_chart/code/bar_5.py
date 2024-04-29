
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

grade = ["5th", "6th", "7th", "8th"]
math = [75, 80, 85, 90]
science = [80, 85, 90, 95]
english = [90, 95, 98, 100]

ax.bar(grade, math, color="blue", label="Math")
ax.bar(grade, science, bottom=math, color="orange", label="Science")
ax.bar(grade, english, bottom=[math[i]+science[i] for i in range(len(math))], color="green", label="English")

plt.title('Academic scores in three subjects for grades 5th to 8th in 2021')
plt.xlabel('Grade')
plt.ylabel('Score (%)')
plt.xticks(rotation=0)
plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig('bar chart/png/225.png')
plt.clf()