
import matplotlib.pyplot as plt

sports = ['Football','Basketball','Baseball','Tennis','Hockey','Others']
percentage = [40,30,15,7,5,3]

plt.figure(figsize=(7,7))
ax1 = plt.subplot()
ax1.pie(percentage, labels=sports, autopct='%1.1f%%', startangle=90, shadow=True)
ax1.legend(sports, loc="best")
plt.title("Popularity of Sports in the USA, 2023")
plt.tight_layout()
plt.xticks(rotation=0)
plt.savefig('pie chart/png/332.png')
plt.clf()