
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Lawsuits = [3000, 2000, 1500, 2500]
Judges = [500, 400, 350, 450]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

width = 0.35 
xlocs = np.arange(len(Country))
ax.bar(xlocs-width, Lawsuits, width=width, align='center', label="Lawsuits")
ax.bar(xlocs, Judges, width=width, align='center', label="Judges")

ax.set_xticks(xlocs)
ax.set_xticklabels(Country)
ax.set_ylabel('Number')
ax.set_title('Number of lawsuits and judges in four countries in 2021')
ax.legend()

for i, v in enumerate(Lawsuits):
    ax.text(xlocs[i]-width/2, v+10, str(v), ha='center', va='bottom')
for i, v in enumerate(Judges):
    ax.text(xlocs[i]+width/2, v+10, str(v), ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/203.png')
plt.clf()