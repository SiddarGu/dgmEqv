
import matplotlib.pyplot as plt
import numpy as np

labels = ['18-25','26-35','36-45','46-55','56-65']
sizes = [20,30,25,15,10]

fig, ax = plt.subplots(figsize=(7,6))

ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize':12}, wedgeprops={'linewidth':2}, shadow=True)
ax.axis('equal') 
plt.title('Employee Age Distribution in the United States, 2023')
plt.tight_layout()
plt.xticks(rotation=90)
plt.savefig('pie chart/png/310.png')
plt.clf()