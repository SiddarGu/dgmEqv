

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

x = ["USA","UK","Germany","France"]
y1 = [13,30,40,35]
y2 = [40,35,25,30]
y3 = [10,10,15,15]

fig, ax = plt.subplots(figsize=(10,6))
ax.bar(x, y1, color="lightblue", label="Renewable Energy")
ax.bar(x, y2, bottom=y1, color="yellow", label="Fossil Fuels")
ax.bar(x, y3, bottom=[y1[i]+y2[i] for i in range(len(y1))], color="red", label="Nuclear Energy")

for i, v in enumerate(y1):
    ax.text(i-0.15, v/2, str(v)+"%", color='black', fontweight='bold', fontsize=11)
for i, v in enumerate(y2):
    ax.text(i-0.15, y1[i] + v/2, str(v)+"%", color='black', fontweight='bold', fontsize=11)
for i, v in enumerate(y3):
    ax.text(i-0.15, y1[i] + y2[i] + v/2, str(v)+"%", color='black', fontweight='bold', fontsize=11)

legend_patch = [mpatches.Patch(color="lightblue", label="Renewable Energy"),
                mpatches.Patch(color="yellow", label="Fossil Fuels"),
                mpatches.Patch(color="red", label="Nuclear Energy")]
ax.legend(handles=legend_patch, bbox_to_anchor=(1.04,0.5), loc="center left")
ax.set_xticks(x)
ax.set_title("Percentage of Renewable Energy, Fossil Fuels and Nuclear Energy in four countries in 2021")
fig.tight_layout()
plt.savefig("Bar Chart/png/377.png")
plt.clf()