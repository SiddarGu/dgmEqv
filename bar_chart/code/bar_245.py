
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()

country = ['USA','UK','Germany','France']
public_spending = [20, 25, 30, 27]
taxation = [30, 32, 35, 33]

ax.bar(country, public_spending, label='Public Spending', bottom=taxation, color='#AADD00')
ax.bar(country, taxation, label='Taxation', color='#50A6C2')
ax.legend(loc='upper right', ncol=2)
ax.set_title('Government spending and taxation in four countries in 2021')
ax.set_ylabel('% of GDP')
ax.set_xticklabels(country, rotation=45, horizontalalignment='right', wrap=True)
plt.tight_layout()
plt.savefig('bar chart/png/200.png')
plt.clf()