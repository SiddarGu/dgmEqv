
import matplotlib.pyplot as plt
import numpy as np

labels = ['Female','Male']
sizes = [45,55]
colors = ['#ff9999','#66b3ff']
plt.figure(figsize=(10,7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Gender Distribution of Employees in the US, 2023', fontsize=14, wrap=True)
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/389.png') 
plt.clf()