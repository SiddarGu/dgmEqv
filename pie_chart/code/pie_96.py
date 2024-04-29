
import matplotlib.pyplot as plt

sources = ["Solar", "Wind", "Nuclear", "Hydro", "Fossil Fuel"]
percentage = [20,30,25,15,10]

fig = plt.figure(figsize=(6,5))
ax = fig.add_subplot(111)

ax.pie(percentage, labels=sources, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10, 'color':'k'},
       wedgeprops={'linewidth':4, 'edgecolor':'k'},shadow=True)

ax.set_title("Renewable Energy Sources in the USA, 2023", fontsize=14)

plt.tight_layout()
plt.savefig('pie chart/png/399.png')
plt.clf()