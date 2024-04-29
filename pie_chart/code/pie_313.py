
import matplotlib.pyplot as plt
import numpy as np

labels = ['Full-time Employees', 'Part-time Employees', 'Contractors', 'Interns', 'Other']
sizes = [60, 20, 10, 5, 5]

plt.figure(figsize=(8, 8))
plt.subplot()
plt.pie(sizes, labels=labels, autopct='%.1f%%', shadow=True, startangle=90)
plt.title('Employee Status Distribution in Organizations, 2023', fontsize=15)
plt.legend(bbox_to_anchor=(1, 0.5), loc="center right", fontsize=12)
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/56.png')
plt.clf()