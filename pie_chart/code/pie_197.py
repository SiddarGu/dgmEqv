
import matplotlib.pyplot as plt
import numpy as np

gender = ['Male', 'Female']
percentage = [50, 50]

fig, ax = plt.subplots(figsize=(7,7))
ax.set_title('Gender Distribution in the USA, 2023', fontsize=18)
ax.pie(percentage, labels=gender, autopct='%.2f%%', shadow=True, startangle=90, radius=1.2)
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/116.png')
plt.clf()