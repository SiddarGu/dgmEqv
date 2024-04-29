
import matplotlib.pyplot as plt
import numpy as np

country = ('USA','UK','Germany','France')
solar = (100,50,90,70)
wind = (80,60,70,50)
nuclear = (30,20,40,35)

x = np.arange(len(country))
width = 0.2

fig, ax = plt.subplots(figsize=(10,5))
ax.bar(x-width, solar, width=width, label='Solar Energy(GW)')
ax.bar(x, wind, width=width, label='Wind Energy(GW)')
ax.bar(x+width, nuclear, width=width, label='Nuclear Energy(GW)')
ax.set_title('Production of different energy sources in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(country)
ax.legend()

for i in range(len(country)):
    ax.annotate(str(solar[i]), xy=(x[i]-width, solar[i]), xytext=(x[i]-width, solar[i]+5), ha='center', va='bottom', rotation=90)
    ax.annotate(str(wind[i]), xy=(x[i], wind[i]), xytext=(x[i], wind[i]+5), ha='center', va='bottom', rotation=90)
    ax.annotate(str(nuclear[i]), xy=(x[i]+width, nuclear[i]), xytext=(x[i]+width, nuclear[i]+5), ha='center', va='bottom', rotation=90)

plt.tight_layout()
plt.savefig('Bar Chart/png/391.png')
plt.clf()