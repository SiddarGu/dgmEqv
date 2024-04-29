
import matplotlib.pyplot as plt
import numpy as np

Types = ['Fast Food', 'Processed Foods', 'Natural Foods', 'Organic Foods', 'Diet Foods']
Percentage = [30, 20, 25, 15, 10]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.pie(Percentage, labels=Types, autopct='%1.1f%%', textprops={'fontsize': 14}) 
ax.set_title('Food Industry Distribution in the USA, 2023', fontsize=18)
plt.tight_layout()
plt.savefig("pie chart/png/113.png", bbox_inches='tight')
plt.close()