
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot()
ax.plot(['Q1', 'Q2', 'Q3', 'Q4'], [1000, 1400, 1800, 2200], color='tab:red', linewidth=3, label='Average Revenue')
ax.set_title('Average Revenue of an Online Retail Store in 2021', fontsize=20, fontweight='bold')
ax.set_xlabel('Quarter', fontsize=15, fontweight='bold')
ax.set_ylabel('Average Revenue', fontsize=15, fontweight='bold') 
ax.legend(loc='upper left')
ax.grid(True, linestyle='dashed', linewidth='1', axis='x')
ax.set_xticks(['Q1', 'Q2', 'Q3', 'Q4'])

plt.tight_layout()
plt.savefig('line chart/png/78.png')
plt.clf()