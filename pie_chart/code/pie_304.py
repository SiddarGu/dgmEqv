
import matplotlib.pyplot as plt
import numpy as np

labels = 'Income Tax', 'Property Tax', 'Sales Tax', 'Excise Tax', 'Fuel Tax', 'Other Taxes'
sizes = [40, 20, 15, 7, 6, 12]

plt.figure(figsize=(10,8))
ax = plt.subplot()
ax.set_title('Distribution of Tax Types in the USA in 2023')
ax.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 14},
        wedgeprops={'linewidth': 2}, startangle=90,
        shadow=True, rotatelabels=True, labeldistance=1.2)
ax.axis('equal') 
plt.tight_layout()
plt.savefig('pie chart/png/443.png')
plt.clf()