
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6,6))
labels = 'Single Family Homes','Townhomes','Condominiums','Multi-Family Homes','Other'
sizes = [42,25,20,7,6]
explode = (0, 0, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
plt.title("Homeownership Distribution in the USA, 2023")
plt.tight_layout()
plt.xticks(np.arange(len(labels)), labels,rotation=45, ha='right')
plt.savefig("pie chart/png/247.png")
plt.clf()