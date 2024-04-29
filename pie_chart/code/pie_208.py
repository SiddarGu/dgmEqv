
import matplotlib.pyplot as plt

labels = ["Primary School", "Secondary School", "High School", "College", "University"]
sizes = [30, 25, 20, 15, 10]
colors = ["red", "green", "blue", "orange", "purple"]

fig = plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 12, 'wrap': True, 'rotation': 90})
plt.title('Education Level Distribution in the USA, 2023', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/31.png')
plt.clf()