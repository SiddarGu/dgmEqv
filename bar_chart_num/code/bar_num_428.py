
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Automotive_Production = [10, 9, 11, 8]
Electronic_Production = [12, 13, 14, 15]
Medical_Supplies_Production = [8, 11, 12, 14]

x = np.arange(len(Country))
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width, Automotive_Production, width=width, label='Automotive Production(million)')
ax.bar(x, Electronic_Production, width=width, label='Electronic Production(million)')
ax.bar(x + width, Medical_Supplies_Production, width=width, label='Medical Supplies Production(million)')

ax.set_title('Manufacturing Production Output in Four Countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.legend()

for i, v in enumerate(Automotive_Production):
    ax.text(i - width/2, v + 0.5, str(v), color='black', fontweight='bold')
for i, v in enumerate(Electronic_Production):
    ax.text(i - width/2, v + 0.5, str(v), color='black', fontweight='bold')
for i, v in enumerate(Medical_Supplies_Production):
    ax.text(i + width/2, v + 0.5, str(v), color='black', fontweight='bold')

plt.tight_layout()
plt.savefig('Bar Chart/png/434.png',dpi=300)
plt.clf()