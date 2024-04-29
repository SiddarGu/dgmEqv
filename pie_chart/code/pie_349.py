
import matplotlib.pyplot as plt
import numpy as np

sources = ['Solar','Wind','Hydropower','Biomass','Geothermal']
percentage = [25,20,30,15,10]

plt.figure(figsize=(10,8))
ax = plt.subplot()
ax.pie(percentage, labels=sources, autopct='%1.2f%%', wedgeprops={"edgecolor":"k",'linewidth': 2})
plt.title("Distribution of Renewable Energy Sources in the USA, 2023", fontsize=16)
plt.legend(loc="upper left", bbox_to_anchor=(1,1),fontsize=14)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("pie chart/png/309.png")
plt.clf()