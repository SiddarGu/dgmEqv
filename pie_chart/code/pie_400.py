
import matplotlib.pyplot as plt
import numpy as np

labels= ["Private Insurance", "Medicare", "Medicaid", "Other Public Insurance", "Uninsured"]
sizes = [35,25,25,10,5]

fig = plt.figure(figsize=(10, 10)) 
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 14}, 
       wedgeprops=dict(width=0.5), startangle=90)
ax.set_title("US Population Health Insurance Coverage in 2023", fontsize=16)
ax.legend(labels, loc="upper right", fontsize=12, bbox_to_anchor=(1.3,1))
plt.tight_layout()
plt.savefig('pie chart/png/291.png',dpi=300)
plt.clf()