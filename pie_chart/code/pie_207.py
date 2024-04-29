
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.subplot()

modes = ["Air", "Rail", "Road", "Water", "Pipeline"]
percentages = [25, 20, 45, 5, 5]

ax.pie(percentages, labels=modes, autopct='%1.1f%%', textprops={'fontsize': 14}, startangle=90,
       labeldistance=1.05, radius=1.2, rotatelabels=True, wedgeprops={'linewidth': 1.5, 'edgecolor': 'white'})

plt.title("Method of Transportation in the US in 2023", fontsize=16)
plt.tight_layout()

plt.savefig('pie chart/png/170.png')
plt.clf()