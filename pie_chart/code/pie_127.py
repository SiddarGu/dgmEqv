
import matplotlib.pyplot as plt

sports = ["Football", "Basketball", "Baseball", "Hockey", "Soccer", "Golf", "Other Sports"]
percentages = [25, 20, 15, 15, 10, 10, 5]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(percentages, labels= sports, autopct='%1.1f%%', rotatelabels=True, textprops={'wrap': True})
ax.set_title('Popularity of Sports in the USA, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/382.png')
plt.clf()