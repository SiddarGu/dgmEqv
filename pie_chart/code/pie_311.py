
import matplotlib.pyplot as plt
import numpy as np

labels = ['Primary School', 'Secondary School', 'Tertiary Education', 'Vocational Education']
sizes = [30, 35, 25, 10]

fig, ax = plt.subplots(figsize=(7,7))
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
        colors=['dodgerblue', 'orange', 'forestgreen', 'crimson'],
        textprops=dict(color="black", wrap=True, rotation=45))

ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax.set_title('Distribution of Education Levels in the USA, 2023', fontsize=14)
plt.tight_layout()
plt.savefig('pie chart/png/281.png')
plt.clf()