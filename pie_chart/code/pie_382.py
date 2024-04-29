
import matplotlib.pyplot as plt

level = ["High School", "Associate's Degree", "Bachelor's Degree", "Master's Degree", "Doctorate Degree"]
percentage = [30, 15, 25, 20, 10]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.pie(percentage, labels=level, autopct='%.2f%%')
ax.set_title("Education Level Distribution in the USA, 2023", fontsize=20, pad=20)
ax.legend(loc="upper right", bbox_to_anchor=(1.1, 1.1))
plt.tight_layout()
plt.xticks(rotation=90)
plt.savefig('pie chart/png/511.png')
plt.clf()