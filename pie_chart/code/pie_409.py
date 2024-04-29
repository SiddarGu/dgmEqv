
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 8))
labels = ["Television", "YouTube", "Social media", "Streaming services", "Radio"]
sizes = [35, 25, 20, 10, 10]
explode = (0.1, 0, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 8, 'rotation': 45, 'wrap':True})
plt.axis('equal')
plt.title('Viewership Distribution for Sports and Entertainment Platforms in 2023')
plt.tight_layout()
plt.savefig("pie chart/png/223.png")
plt.clf()