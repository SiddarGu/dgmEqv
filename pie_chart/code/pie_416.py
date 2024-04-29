
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 8))
explode = [0.2, 0, 0, 0, 0, 0]
labels = ["Individuals", "Corporations", "Foundations", "Government Grants", "Special Events", "Other"]
sizes = [55, 20, 10, 5, 5, 5]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#fecf3f', '#f99fcf']
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'wrap':True, 'rotation_mode': 'anchor', 'rotation': 90, 'fontsize': 8})
plt.title("Distribution of Donations for Nonprofit Organizations in 2021", loc='center', fontsize=14)
plt.tight_layout()
plt.savefig('pie chart/png/442.png')
plt.clf()