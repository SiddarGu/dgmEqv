
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,5))

data = np.array([[200,400,800],[300,500,1000],[180,400,900],[230,470,1100]])
index = np.arange(4)
country = ['USA','UK','Germany','France']

width = 0.2
x = np.arange(4)
production_A = data[:,0]
production_B = data[:,1]
production_C = data[:,2]

ax = plt.subplot()
ax.bar(x-width, production_A, width, label='Production A', align='edge')
ax.bar(x, production_B, width, label='Production B', align='edge')
ax.bar(x+width, production_C, width, label='Production C', align='edge')

ax.set_xticks(index)
ax.set_xticklabels(country,rotation=45,ha='right')
ax.set_title('Production output in three categories in four countries in 2021')
ax.set_ylabel('million')
ax.legend()
plt.tight_layout()
plt.savefig('bar chart/png/358.png')
plt.clf()