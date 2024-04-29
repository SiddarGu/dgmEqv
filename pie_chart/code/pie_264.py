
import matplotlib.pyplot as plt

majors = ['Computer Science', 'Math and Statistics', 'Engineering', 'Physics', 'Chemistry']
percentages = [25, 20, 30, 15, 10]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(percentages, labels=majors, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 12}, shadow=True, wedgeprops={"edgecolor":"k",'linewidth': 1, 'linestyle': 'solid'})
ax.set_title("Distribution of Science and Engineering Majors in 2023", fontsize=16)
plt.legend(loc="lower right")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/515.png')

plt.clf()