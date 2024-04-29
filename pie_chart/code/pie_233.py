
import matplotlib.pyplot as plt
import numpy as np

data = {'Criminal Law': 30, 'Family Law': 25, 'Civil Law': 25, 'Intellectual Property Law': 10, 'International Law': 10}
labels = list(data.keys())
values = list(data.values())

plt.figure(figsize=(6, 6))
plt.subplot(1, 1, 1)
plt.pie(values, labels=labels, autopct='%.1f%%', pctdistance=0.8, labeldistance=1.1, startangle=90)
plt.axis('equal')
plt.title('Breakdown of Legal Cases in the United States, 2023')
plt.legend(bbox_to_anchor=(1.4, 1), loc='upper right', fontsize=10)
plt.tight_layout()
plt.xticks(rotation=90)
plt.savefig('pie chart/png/269.png')
plt.clf()