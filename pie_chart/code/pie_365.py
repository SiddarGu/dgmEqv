
import matplotlib.pyplot as plt
plt.figure(figsize=(10,7))
labels = ['Pop Music','Rock Music','Hip-Hop and R&B','Jazz','Country','Classical','Electronic/Dance']
sizes = [35,15,15,10,10,10,5]
explode = (0.1, 0, 0, 0, 0, 0, 0)
plt.pie(sizes,labels=labels,explode=explode,shadow=True,autopct='%1.1f%%', startangle=140)
plt.title("Popularity of Music Genres in the USA, 2023")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/467.png')
plt.clf()