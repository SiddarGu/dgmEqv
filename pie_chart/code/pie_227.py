
import matplotlib.pyplot as plt
import numpy as np

labels = ['Rail', 'Air', 'Road', 'Sea', 'Other']
percentage = [20,35,25,15,5]

fig = plt.figure(figsize=(8, 8))
plt.title("Distribution of Transportation Modes in the USA, 2023")
ax = fig.add_subplot()
colors = ['#48D1CC','#FF6347','#66CDAA','#90EE90','#C71585']
ax.pie(percentage, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors)
plt.tight_layout()
plt.savefig("pie chart/png/493.png")
plt.clf()