
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt 

plt.figure(figsize=(6,6))  

labels = ['Painting','Sculpture','Printmaking','Photography','Drawing','Other']
sizes = [45,20,15,10,7,3]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 8, 'color':'Black'}, shadow=True, startangle=130, rotatelabels=True, radius=1.2, wedgeprops={'linewidth': 2, 'edgecolor':"White"})

plt.title("Art Forms Popularity in the USA, 2023")

plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/299.png', dpi=100)

plt.clf()