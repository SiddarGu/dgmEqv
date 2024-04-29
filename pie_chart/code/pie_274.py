
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

labels = ['Primary Education', 'Secondary Education', 'Higher Education', 'Special Education', 'Other']
sizes = [25, 30, 20, 15, 10]
explode = (0, 0, 0, 0, 0.1)

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax.axis('equal') 

plt.title("Distribution of Government Education Spending in 2023")
plt.xticks(rotation=90, wrap=True)
plt.tight_layout()

plt.savefig('pie chart/png/75.png')

plt.clf()