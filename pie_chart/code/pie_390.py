
import matplotlib.pyplot as plt 
plt.figure(figsize=(10, 6))
labels = ['Millenials', 'Generation X', 'Baby Boomers', 'Generation Z']
sizes = [35, 30, 25, 10]
explode = [0, 0.1, 0, 0]
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, textprops={'fontsize': 11},
        wedgeprops={'linewidth': 1.5, 'edgecolor': 'black'})
plt.title("Percentage of Employees in Different Generations, 2023")
plt.tight_layout()
plt.savefig('pie chart/png/190.png')
plt.clf()