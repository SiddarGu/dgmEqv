
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12,6))

year = np.array([2021, 2022, 2023 , 2024])
gov_spending = np.array([3000, 3200, 3000, 2800])
taxation= np.array([2000, 2500, 2300, 2200])

plt.plot(year, gov_spending, label='Government Spending')
plt.plot(year, taxation, label='Taxation')

plt.xticks(year)
plt.xlabel('Year')
plt.ylabel('Amount (billion dollars)')
plt.title('Changes in Government Spending and Taxation from 2021 to 2024')

plt.legend(loc='best')

for a,b,c in zip(year, gov_spending, taxation):
    plt.annotate('%s\n'%b,xy=(a,b),xytext=(a-0.1,b+50))
    plt.annotate('%s'%c,xy=(a,c),xytext=(a-0.1,c-50))

plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/309.png')
plt.clf()