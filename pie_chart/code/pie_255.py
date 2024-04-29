
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
sports = ["Football","Basketball","Tennis","Baseball","Hockey","Other"]
percentage = [35,25,15,10,10,5]
plt.pie(percentage, labels=sports, autopct='%1.2f%%', shadow=True, startangle=90, textprops={'wrap': True, 'rotation': 0})
plt.title('Popular Sports Participated in the USA, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/258.png')
plt.show()
plt.clf()