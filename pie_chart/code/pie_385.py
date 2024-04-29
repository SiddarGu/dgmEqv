
import matplotlib.pyplot as plt

labels = ['Road', 'Rail', 'Air', 'Water', 'Others']
sizes = [40, 20, 25, 10, 5]
explode = (0.1, 0, 0, 0, 0) 

fig1, ax1 = plt.subplots(figsize=(6,6))
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
ax1.set_title("Distribution of Transportation Modes in the USA, 2023")
ax1.legend(loc="upper right", bbox_to_anchor=(1.5, 1.5), fontsize="medium")
plt.tight_layout()
plt.xticks(rotation=90)
plt.savefig("pie chart/png/352.png")
plt.cla()