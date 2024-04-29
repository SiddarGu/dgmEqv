
import matplotlib.pyplot as plt
import matplotlib.text as text

labels = ["Physics","Chemistry","Biology","Computer Science","Mathematics","Engineering"]
sizes = [20,15,25,15,15,10]

fig=plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 15, 'wrap': True, 'rotation': 0}) 
ax.axis('equal') 
ax.set_title("Distribution of Scientific Fields in the USA, 2023")
plt.tight_layout()
plt.savefig('pie chart/png/517.png')
plt.clf()