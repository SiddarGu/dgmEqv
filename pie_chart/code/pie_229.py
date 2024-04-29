
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.axis("equal")
labels = ["Elementary", "Middle School", "High School", "College", "Graduate School"]
pcts = [35, 30, 20, 10, 5]
ax.pie(pcts, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, labeldistance=1.1)
ax.set_title("Percentage of Students at Different Levels of Education in the USA, 2023")
ax.legend(bbox_to_anchor=(1.2, 1))
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("pie chart/png/490.png")
plt.clf()