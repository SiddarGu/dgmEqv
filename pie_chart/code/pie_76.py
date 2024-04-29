
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
ax = plt.subplot()
ax.pie([40, 25, 20, 10, 5], labels=['Road', 'Rail', 'Air', 'Water', 'Other'], autopct='%1.1f%%',
        startangle=90, textprops={'fontsize': 14, 'verticalalignment': 'center', 'horizontalalignment': 'center', 'wrap': True, 'rotation': 45})
ax.set_title('Distribution of Transportation Modes in the World, 2023')
ax.axis('equal')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/188.png')
plt.clf()