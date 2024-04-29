
import matplotlib.pyplot as plt
import numpy as np

labels = ['Primary', 'Secondary', 'Higher Education', 'Vocational', 'Non-Formal']
sizes = [25, 35, 21, 14, 5]

plt.figure(figsize=(10,10))
explode = (0.05, 0.05, 0.05, 0.05, 0.05)
plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Educational Distribution in the USA, 2023')
plt.legend(loc="lower right", bbox_to_anchor=(1.2, 0.5))
plt.axis('equal')
plt.tight_layout()
plt.savefig("pie chart/png/139.png")
plt.clf()