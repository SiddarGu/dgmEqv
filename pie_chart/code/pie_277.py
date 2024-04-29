
import matplotlib.pyplot as plt 
import matplotlib
plt.figure(figsize=(8, 8)) 
ax = plt.subplot(111) 
ax.pie([60, 40], labels=['Male', 'Female'], autopct='%.2f%%', 
       pctdistance=0.7, labeldistance=1.2, 
       rotatelabels=True, textprops={'fontsize': 12},
       wedgeprops={'linewidth': 2, 'edgecolor': 'white'}, 
       startangle=90) 
plt.title("Gender Employment Rate in the USA, 2023", fontsize=14, wrap=True) 
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('pie chart/png/129.png') 
plt.clf()