
import matplotlib.pyplot as plt
import numpy as np

Country =['USA','UK','Germany','France']
Lawyers = [50,40,45,35]
Judges =[30,20,25,35]

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(Country, Lawyers, label='Lawyers', color='c', bottom=Judges)
ax.bar(Country, Judges, label='Judges', color='m')
ax.set_title('Number of lawyers and judges in four countries in 2021')
ax.set_xlabel('Country') 
ax.set_ylabel('Number (thousand)')
ax.legend()
ax.set_xticklabels(Country, rotation=45, ha='right')
plt.tight_layout()
plt.savefig('bar chart/png/310.png')
plt.clf()