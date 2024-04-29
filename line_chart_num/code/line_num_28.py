
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15,10))
plt.plot([2018, 2019, 2020, 2021, 2022, 2023], 
         [20000, 30000, 50000, 80000, 100000, 120000], 
         color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.xlabel('Year')
plt.ylabel('Number of Users')
plt.title('Increase of Internet Usage in the Past 5 Years')
plt.xticks(np.arange(2018, 2024, 1))
plt.grid(axis='y', linestyle='--')

for a,b in zip([2018, 2019, 2020, 2021, 2022, 2023], 
         [20000, 30000, 50000, 80000, 100000, 120000]): 
    plt.text(a, b, str(b), fontsize=12, wrap=True)

plt.tight_layout()
plt.savefig('line chart/png/161.png')
plt.clf()