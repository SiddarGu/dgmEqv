
import matplotlib.pyplot as plt
plt.figure(figsize=(9,5),dpi=150)
x_data = ["Grade 1","Grade 2","Grade 3","Grade 4"]
y_math = [70, 80, 90, 85]
y_science = [60, 65, 70, 75]
y_english = [80, 85, 90, 95]
ax = plt.subplot()
ax.bar(x_data, y_math, bottom=0, label="Math")
ax.bar(x_data, y_science, bottom=y_math, label="Science")
ax.bar(x_data, y_english, bottom=[i+j for i,j in zip(y_math,y_science)], label="English")
plt.xticks(rotation=45,ha='right',wrap=True)
plt.title("Academic performance in Math, Science, and English of students from Grade 1 to 4 in 2021")
plt.legend(loc="upper right")
plt.tight_layout()
plt.savefig('bar chart/png/54.png')
plt.clf()