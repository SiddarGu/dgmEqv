
import matplotlib.pyplot as plt
plt.figure(figsize=(7,7))
labels = ['Renewable Sources','Nuclear','Natural Gas','Coal','Oil']
sizes = [35,25,20,15,5]
explode = (0.1,0,0,0,0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.title('Energy Sources in the USA, 2023', size=20, pad=25)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/130.png')
plt.clf()