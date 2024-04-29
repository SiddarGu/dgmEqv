
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10,6))

regions = ('North America','Europe','Asia','South America')
InvestmentA = [200, 180, 250, 150]
InvestmentB = [300, 250, 300, 200]
InvestmentC = [400, 350, 400, 250]

r1 = np.arange(len(regions))
w = 0.2

ax.bar(r1-w, InvestmentA, width=w, color='#FFC300', label='Investment A')
ax.bar(r1, InvestmentB, width=w, color='#58508D', label='Investment B')
ax.bar(r1+w, InvestmentC, width=w, color='#EE3B3B', label='Investment C')

ax.set_xticks(r1)
ax.set_xticklabels(regions, rotation=45)
ax.set_title('Investment in three categories across four regions in 2021')
ax.legend()
ax.autoscale_view()
ax.set_ylabel('Investment($ billion)')

for i, v in enumerate(InvestmentA):
    ax.text(i-(w/2), v + 5, str(v), color='#FFC300', fontweight='bold')
for i, v in enumerate(InvestmentB):
    ax.text(i+(w/2), v + 5, str(v), color='#58508D', fontweight='bold')
for i, v in enumerate(InvestmentC):
    ax.text(i+(1.5*w), v + 5, str(v), color='#EE3B3B', fontweight='bold')

plt.tight_layout()
plt.savefig('Bar Chart/png/481.png')
plt.clf()