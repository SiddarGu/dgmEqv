
import matplotlib.pyplot as plt

Modes = ['Rail','Air','Road','Water']
Percentage = [25,20,45,10]

plt.figure(figsize=(8,8))
ax = plt.subplot()

ax.pie(Percentage, labels=Modes, autopct='%1.1f%%',
       startangle=90, shadow=True,
       textprops={'fontsize': 14},
       wedgeprops={'linewidth': 2, 'edgecolor': 'white'})
ax.set_title('Distribution of Transportation Modes in the US, 2023', fontsize=20)
ax.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/280.png')
plt.clf()