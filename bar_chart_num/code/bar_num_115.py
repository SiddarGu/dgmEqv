
import matplotlib.pyplot as plt
import numpy as np

category = np.array(['Painting', 'Sculpture', 'Music', 'Theatre'])
artist = np.array(['John Doe', 'Jane Doe', 'Jack Doe', 'Jill Doe'])
sales = np.array([500, 400, 300, 200])
attendance = np.array([7500, 8000, 9000, 9200])

fig, ax = plt.subplots(figsize=(12,6))

ax.bar(category, sales, bottom=attendance, label='Sales')
ax.bar(category, attendance, label='Attendance')

ax.set_title('Sales and attendance of artists in four categories in 2021')
ax.legend(loc='upper center')
ax.set_xticks(category)
ax.set_xticklabels(artist, rotation=45, ha='right', wrap=True)

for i, v in enumerate(sales):
    ax.text(i-.2, v/2+attendance[i], str(v), color='blue', fontweight='bold')
for i, v in enumerate(attendance):
    ax.text(i-.2, v/2, str(v), color='red', fontweight='bold')

fig.tight_layout()
plt.savefig('Bar Chart/png/390.png')
plt.clf()