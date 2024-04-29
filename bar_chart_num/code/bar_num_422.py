
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 800, 500], 
        ['UK', 900, 700], 
        ['Germany', 700, 500], 
        ['France', 800, 600]]

country = [x[0] for x in data]
man_output = [x[1] for x in data]
exports = [x[2] for x in data]

x = np.arange(len(country))
width = 0.35
fig, ax = plt.subplots(figsize=(15, 8))
ax.bar(x - width/2, man_output, width, label='Manufacturing Output (in million)', color='r')
ax.bar(x + width/2, exports, width, label='Exports (in million)', color='b')

ax.set_xticks(x)
ax.set_xticklabels(country)
ax.legend()
ax.set_ylabel('Output')
ax.set_title('Manufacturing and Export Output of Four Countries in 2021')

for i, v in enumerate(man_output):
    ax.text(x[i] - width/2, v + 5, str(v), ha='center', va='bottom', fontsize=10)
for i, v in enumerate(exports):
    ax.text(x[i] + width/2, v + 5, str(v), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('Bar Chart/png/215.png')
plt.clf()