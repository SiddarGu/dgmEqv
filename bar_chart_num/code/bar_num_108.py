
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 200, 18], ['UK', 150, 22], ['Germany', 180, 30], ['France', 125, 25]]

Country, Carbon_Emission, Renewable_Energy = zip(*data)
ind = np.arange(len(Country))
width = 0.35

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.bar(ind, Carbon_Emission, width, bottom=0, color='darkslategray', label='Carbon Emission(million ton)')
ax.bar(ind, Renewable_Energy, width, bottom=Carbon_Emission, color='lightseagreen', label='Renewable Energy(%)')

ax.set_xticks(ind)
ax.set_xticklabels(Country, rotation=45, ha='right')
ax.set_title('Carbon emission and renewable energy in four countries in 2021')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5)

for i in range(len(Country)):
    ax.annotate(Carbon_Emission[i], xy=(ind[i] - 0.2, Carbon_Emission[i] + 2), color='white')
    ax.annotate(Renewable_Energy[i], xy=(ind[i] + 0.2, Carbon_Emission[i] + Renewable_Energy[i] + 2), color='white')

fig.tight_layout()
plt.savefig('Bar Chart/png/333.png')
plt.clf()