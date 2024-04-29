
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
labels=['USA','UK','Germany','France']
x=np.arange(len(labels))
width=0.35
rects1 = ax.bar(x-width/2, [50,45,35,40], width, label='Carbon Emission(thousand Kg/yr)')
rects2 = ax.bar(x+width/2, [20,25,30,35], width, label='Renewable Energy(%)')
ax.set_title('Carbon emission and renewable energy usage in four countries in 2021', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=12, rotation=30, ha='right', wrap=True)
ax.set_ylabel('Values', fontsize=12)
ax.legend(loc='best')
fig.tight_layout()
plt.savefig('bar_262.png')
plt.clf()