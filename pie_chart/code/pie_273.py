
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
labels = ['Road','Rail','Air','Water']
sizes = [40,20,30,10]
explode = [0, 0, 0.1, 0]
ax.pie(sizes, explode = explode, labels=labels, autopct='%1.1f%%', 
       shadow=True, startangle=90)
ax.set_title("Distribution of Transportation Modes in the USA, 2023")
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig('pie chart/png/42.png')
plt.clf()