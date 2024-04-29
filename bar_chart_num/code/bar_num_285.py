
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Organic_Farming = np.array([10, 15, 12, 17])
Conventional_Farming = np.array([20, 30, 25, 27])

x = np.arange(len(Country))
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(x, Organic_Farming, width=0.4, label='Organic Farming', bottom=Conventional_Farming)
ax.bar(x, Conventional_Farming, width=0.4, label='Conventional Farming')

for i in range(len(Country)):
    ax.annotate(Organic_Farming[i], xy=(i - 0.2, Conventional_Farming[i] + Organic_Farming[i]/2), ha='center', va='center', fontsize=8, rotation=90)
    ax.annotate(Conventional_Farming[i], xy=(i + 0.2, Conventional_Farming[i]/2), ha='center', va='center', fontsize=8, rotation=90)

plt.xticks(x, Country)
plt.title('Comparison of Organic and Conventional Farming acreage in four countries in 2021')
plt.legend()
plt.tight_layout()
plt.savefig('Bar Chart/png/348.png')
plt.clf()