
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(1, 1, 1)
plt.title('Government Spending Distribution in the USA, 2023')
labels = ["Education","Social Services","Defense","Healthcare","Infrastructure","Public Works","Other"]
sizes = [30,20,15,15,10,10,10]
explode = [0, 0, 0, 0, 0, 0, 0.2]
ax.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/35.png')
plt.clf()