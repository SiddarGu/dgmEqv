
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(7,7))
labels = ['Male', 'Female']
sizes = [45, 55]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 14})
plt.title('Gender Distribution in the USA in 2021', fontsize=16)
plt.tight_layout()
plt.savefig('pie chart/png/392.png')
plt.clf()