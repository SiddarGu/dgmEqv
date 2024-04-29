
import matplotlib.pyplot as plt
import numpy as np

Country =['USA','UK','Germany','France']
Tax_Rate=[20,18,22,21]
Public_Spending=[1000,1200,1100,1300]

fig, ax = plt.subplots(figsize=(8,4))
ax.bar(Country, Tax_Rate, label='Tax Rate', color='blue')
ax.bar(Country, Public_Spending, bottom=Tax_Rate, label='Public Spending', color='red')

ax.set_xticks(Country)
ax.set_title('Tax Rate and Public Spending in four countries in 2021')
ax.legend(loc='upper left')
for i, v in enumerate(Tax_Rate):
    ax.text(i, v/2, str(v)+'%', fontsize=12)
for i, v in enumerate(Public_Spending):
    ax.text(i, v+Tax_Rate[i]/2, str(v)+'B', fontsize=12, wrap=True)

plt.tight_layout()
plt.savefig('Bar Chart/png/376.png')
plt.clf()