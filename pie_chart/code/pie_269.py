
import matplotlib.pyplot as plt
import matplotlib

plt.figure(figsize=(8, 6))

sources = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Bioenergy']
percentage = [25, 20, 30, 15, 10]

plt.pie(percentage, labels=sources, autopct='%1.1f%%', textprops={'fontsize': 14}, 
        wedgeprops={'linewidth': 3, 'edgecolor':'white'}, startangle=90, shadow=True)

plt.title('Distribution of Renewable Energy Sources in the USA, 2023', fontsize=14)
plt.tight_layout()
plt.savefig('pie chart/png/194.png')

plt.close()