
import matplotlib.pyplot as plt

labels = ['USA','India','China','Brazil','Mexico']
data = [40, 400, 100, 60, 50]

fig = plt.figure(figsize=(12,6)) 
ax = fig.add_subplot()
ax.plot(labels,data, marker='o', color='blue', linestyle='-', linewidth=2)
ax.set_title('Poverty Levels in Selected Countries, 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number of People Living Below Poverty Line')
ax.set_xticklabels(labels, rotation=45, ha='right', wrap=True)
plt.tight_layout()
plt.savefig('line chart/png/105.png')
plt.clf()