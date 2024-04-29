
import matplotlib.pyplot as plt
import numpy as np

month = ['January', 'February', 'March', 'April', 'May', 'June']
production_a = [200, 220, 210, 250, 240, 230]
production_b = [300, 260, 280, 320, 310, 290]
production_c = [400, 450, 410, 390, 420, 440]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
ax.plot(month, production_a, label='Production A')
ax.plot(month, production_b, label='Production B')
ax.plot(month, production_c, label='Production C')

for i, v in enumerate(production_a):
    ax.text(i, v + 5, str(v), rotation=45, ha='center', va='bottom')
for i, v in enumerate(production_b):
    ax.text(i, v + 5, str(v), rotation=45, ha='center', va='bottom')
for i, v in enumerate(production_c):
    ax.text(i, v + 5, str(v), rotation=45, ha='center', va='bottom')

plt.title('Production Output of Three Categories of Products in 2020')
plt.xlabel('Month')
plt.ylabel('Production')
ax.legend(loc='upper left')
ax.grid(axis='y', linestyle='-')

plt.xticks(np.arange(len(month)), month, rotation=45, ha='right')
plt.tight_layout()
plt.savefig('line chart/png/136.png', dpi=300)
plt.clf()