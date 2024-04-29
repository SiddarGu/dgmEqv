
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 8))

labels=['Visual Arts','Music','Theatre','Dance','Literature','Film']
values=[25,20,20,15,15,5]

plt.pie(values, labels=labels, autopct='%1.2f%%', explode=[0,0,0,0,0,0.1], shadow=True) 

plt.title("Distribution of Arts Categories in the USA in 2023")
plt.legend(labels, bbox_to_anchor=(1, 0.8), loc="upper right")

plt.tight_layout()
plt.savefig("pie chart/png/99.png")
plt.clf()