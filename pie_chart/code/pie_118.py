
import matplotlib.pyplot as plt

labels = ['Mobile', 'Laptop', 'Desktop', 'Tablet', 'Other']
sizes = [35, 30, 20, 10, 5]

fig = plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 14, 'wrap': True, 'rotation': 0})

plt.title('Global Distribution of Device Usage in 2023', fontsize=14, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/85.png')
plt.close('all')