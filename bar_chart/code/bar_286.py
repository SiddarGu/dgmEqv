
import matplotlib.pyplot as plt
import numpy as np

country = ['USA','UK','France','Germany']
agricultural_output = [7000,4500,6000,5500]
food_production = [5000,3000,4000,3500]

plt.figure(figsize=(10,8))
ax = plt.subplot()
ax.bar(country, agricultural_output, label='Agricultural Output')
ax.bar(country, food_production, bottom=agricultural_output, label='Food Production')
plt.title('Agricultural and Food Production Output in Four Countries in 2021')
plt.xlabel('Country')
plt.ylabel('Output (tonnes)')
plt.legend(loc='upper right',bbox_to_anchor=(1.25,1))
plt.xticks(country,rotation=45)
plt.tight_layout()
plt.savefig('bar chart/png/39.png')
plt.clf()