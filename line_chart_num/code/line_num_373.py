
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))
ax = plt.subplot()

grain_yield = [1000,1100,1300,1200]
fruit_yield = [200,300,400,500]
vege_yield = [500,550,600,650]
herb_yield = [100,150,200,250]

year = [2020,2021,2022,2023]

ax.plot(year,grain_yield,label="Grain Yield")
ax.plot(year,fruit_yield,label="Fruit Yield")
ax.plot(year,vege_yield,label="Vegetable Yield")
ax.plot(year,herb_yield,label="Herb Yield")

ax.set_title("Crop Yields in the United States from 2020 to 2023")
ax.set_xlabel("Year")
ax.set_ylabel("Yield(Tonnes)")

ax.legend(bbox_to_anchor=(1.05,1),loc='upper left',borderaxespad=0.)

for i in range(len(year)):
    ax.annotate(str(grain_yield[i]), xy=(year[i],grain_yield[i]),rotation=45,wrap=True)
    ax.annotate(str(fruit_yield[i]), xy=(year[i],fruit_yield[i]),rotation=45,wrap=True)
    ax.annotate(str(vege_yield[i]), xy=(year[i],vege_yield[i]),rotation=45,wrap=True)
    ax.annotate(str(herb_yield[i]), xy=(year[i],herb_yield[i]),rotation=45,wrap=True)

plt.xticks(year)
plt.tight_layout()
plt.savefig('line chart/png/70.png',dpi=70)
plt.clf()