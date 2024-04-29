
import matplotlib.pyplot as plt
import numpy as np

Country = ["USA","UK","Germany","France"]
Healthcare_Expenditure = [1000,550,750,400]
Population = [350,67,83,67]

fig, ax = plt.subplots(figsize=(12, 8))
width = 0.25
xpos = np.arange(len(Country))
ax.bar(xpos-width, Healthcare_Expenditure, width=width, 
        label='Healthcare Expenditure', color='green')
ax.bar(xpos, Population, width=width, 
        label='Population', color='blue')

ax.set_xticks(xpos)
ax.set_xticklabels(Country)
ax.legend(loc="upper left")
ax.set_title("Healthcare Expenditure and Population of four countries in 2021")

for i in range(len(Country)):
    ax.annotate(f'{Healthcare_Expenditure[i]}', xy=(xpos[i]-width,Healthcare_Expenditure[i]), 
                xytext=(0, 4), 
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate(f'{Population[i]}', xy=(xpos[i],Population[i]), 
                xytext=(0, 4), 
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/90.png')
plt.clf()