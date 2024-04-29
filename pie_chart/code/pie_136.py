
import matplotlib.pyplot as plt
import numpy as np

labels = ['Individuals', 'Corporations', 'Foundations', 'Government', 'Other']
sizes = [40, 25, 20, 10, 5]


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.1f%%',
        startangle=90,textprops={'fontsize': 12, 'wrap': True})

ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

ax.set_title('Distribution of Donations Received by Nonprofit Organizations in the United States, 2023', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('pie chart/png/314.png')
plt.show()
plt.clf()