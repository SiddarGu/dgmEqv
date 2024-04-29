
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()

crops = ['Cereals','Pulses','Fruits','Vegetables','Other']
percentage = [45,10,15,20,10]

ax.pie(percentage, labels=crops, autopct='%1.1f%%', textprops={'fontsize': 14, 'wrap':True, 'rotation':90})
ax.set_title('Global Crop Distribution in 2021', fontsize=18)
plt.tight_layout()
plt.xticks(rotation=90)
plt.savefig('pie chart/png/287.png')
plt.clf()