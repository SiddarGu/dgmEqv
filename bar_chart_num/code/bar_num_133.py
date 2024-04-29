
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10, 6))

State = ['California', 'New York', 'Michigan', 'Texas']
Research_Papers = [400, 360, 390, 420]
Scholars = [120, 150, 110, 130]

x = np.arange(len(State))
width = 0.35

ax = plt.subplot()
ax.bar(x - width/2, Research_Papers, width, label='Research Papers')
ax.bar(x + width/2, Scholars, width, label='Scholars')

ax.set_ylabel('Number')
ax.set_title('Number of research papers and scholars in four states in 2021')
ax.set_xticks(x)
ax.set_xticklabels(State)
ax.legend(fontsize='medium')
for a,b in zip(x, Research_Papers):
    plt.text(a-0.2, b+2, str(b), fontsize=10)
for a,b in zip(x, Scholars):
    plt.text(a+0.2, b+2, str(b), fontsize=10)

plt.tight_layout()
plt.savefig('Bar Chart/png/544.png', dpi=300)
plt.clf()