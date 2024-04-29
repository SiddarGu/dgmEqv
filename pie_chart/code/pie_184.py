
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7,7))

labels = ["Full-time", "Part-time", "Contract", "Self-employed"]
sizes = [50, 30, 15, 5]
colors = ["yellowgreen", "gold", "lightskyblue", "lightcoral"]
explode = (0, 0, 0.1, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Employee Status in the US in 2023", fontsize=14, fontweight="bold")
plt.axis('equal')
plt.tight_layout()
plt.xticks(rotation=45)

plt.savefig('pie chart/png/187.png')
plt.clf()