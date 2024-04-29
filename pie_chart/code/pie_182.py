
import matplotlib.pyplot as plt
import numpy as np

Types = ['Renewable Energy','Nuclear Energy','Fossil Fuels']
Percentage = [50, 20, 30]

plt.figure(figsize=(8,6))
plt.pie(Percentage, labels=Types, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 16, 'color':'black'})
plt.title('Energy Sources Distribution in the USA, 2023', fontsize=22)
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/124.png')
plt.clf()