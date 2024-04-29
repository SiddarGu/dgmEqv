
import matplotlib.pyplot as plt
import numpy as np

#set figure size
plt.figure(figsize=(10,6))

# create a bar chart
ax=plt.subplot()
ax.bar(x = np.arange(4), height = [4000,3500,3800,4200], 
            label = 'Restaurants',width=0.2, align='edge')
ax.bar(x = np.arange(4)+0.2, height = [5000,4500,4800,5200], 
            label = 'Cafes',width=0.2, align='edge')
ax.bar(x = np.arange(4)+0.4, height = [3000,2500,2800,3200], 
            label = 'Takeaways',width=0.2, align='edge')

#set xticks
ax.set_xticks(np.arange(4))
ax.set_xticklabels(['USA', 'UK', 'Germany', 'France'], rotation=90, wrap=True)

#set title
ax.set_title("Number of food outlets in four countries in 2021")

#set legend
plt.legend(loc="upper right")

#adjust the font size
plt.rcParams.update({'font.size': 14})

plt.tight_layout()
plt.savefig('bar chart/png/413.png')
plt.clf()