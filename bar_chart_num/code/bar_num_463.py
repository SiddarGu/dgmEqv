
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

country = ['USA','UK','Germany','France']
hotel_rooms = [4500,3000,4000,3500]
tourist_arrivals = [320000,280000,260000,250000]

rects1 = ax.bar(country, hotel_rooms, label='Hotel Rooms')
rects2 = ax.bar(country, tourist_arrivals, bottom=hotel_rooms, label='Tourist Arrivals')
ax.set_title('Number of hotel rooms and tourist arrivals in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number')
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
plt.xticks(country)
plt.tight_layout()
plt.savefig('Bar Chart/png/140.png')
plt.clf()