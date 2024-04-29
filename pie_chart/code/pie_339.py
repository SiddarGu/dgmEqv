
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,8))

sources = ['Renewable Energy','Fossil Fuels','Nuclear Energy','Hydroelectricity','Biomass']
percentage = [30,40,20,7,3]

explode = (0.1, 0, 0, 0, 0)
plt.pie(percentage, explode=explode, labels=sources, autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Energy Mix in the USA in 2023', fontdict={'fontsize': 18, 'fontweight': 'medium'}, wrap=True)
plt.tight_layout()
plt.savefig('pie chart/png/268.png')
plt.clf()