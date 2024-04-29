
import matplotlib.pyplot as plt
plt.figure(figsize=(15, 8))
ax = plt.subplot()
labels = ["Painting and Drawing", "Sculpture", "Music", "Theatre", "Dance", "Film and Video", "Photography", "Literature"]
values = [25, 20, 18, 15, 10, 8, 7, 5]
ax.pie(values, labels=labels,autopct='%1.1f%%', startangle=90)
ax.axis('equal')
plt.title('Popular Art Forms in the USA, 2023')
plt.savefig('pie chart/png/29.png', bbox_inches='tight')
plt.tight_layout()
plt.xticks(rotation=90)
plt.show()
plt.clf()