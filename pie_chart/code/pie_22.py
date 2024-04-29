
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 8))
ax = plt.subplot()

sources = ['Fossil Fuels','Renewables','Nuclear Power','Hydroelectric','Solar','Geothermal']
percentage = [40,25,15,10,5,5]

plt.pie(percentage, labels=sources, autopct='%1.1f%%', startangle=90, 
        textprops={'fontsize': 12}, 
        wedgeprops={'linewidth': 1, 'edgecolor':'black'})

ax.set_title('Energy Production Sources in the USA, 2023', fontsize=18)
plt.tight_layout()
plt.savefig('pie chart/png/93.png')
plt.cla()