
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

labels = ["Part-time","Full-time","Contractors","Freelancers"]
sizes = [25,50,20,5]
explode = (0.05,0.05,0.05,0.05)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, textprops={'fontsize': 14})

ax.axis('equal')
ax.set_title("Employee Composition of a Company in 2023", fontsize=18, y=1.05)

plt.xticks(rotation = 90)
plt.tight_layout()
plt.savefig('pie chart/png/211.png')
plt.clf()