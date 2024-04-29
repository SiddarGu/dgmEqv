
import matplotlib.pyplot as plt
import numpy as np

Country = np.array(['USA', 'UK', 'India', 'China', 'Japan', 'Philippines', 'Thailand'])
Rate_of_Literacy = np.array([94, 90, 81, 96, 99, 92, 87])

plt.figure(figsize=(8, 6))
plt.plot(Country, Rate_of_Literacy, label='Literacy Rate', marker='o', color='red')
plt.title('Literacy Rate in Selected Countries in 2021')
plt.xticks(Country, rotation=45, wrap=True)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Rate of Literacy', fontsize=12)
plt.grid(True, linewidth=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('line chart/png/4.png')
plt.clf()