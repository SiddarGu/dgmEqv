
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False

data = {'Month': ['January','February','March','April','May','June'],
        'Hotel A': [500,600,700,800,900,1000],
        'Hotel B': [400,450,550,650,750,850],
        'Hotel C': [600,700,800,900,1000,1100]
       }

fig = plt.figure(figsize=(8,5))

plt.plot(data['Month'],data['Hotel A'],label='Hotel A',color='green')
plt.plot(data['Month'],data['Hotel B'],label='Hotel B',color='blue')
plt.plot(data['Month'],data['Hotel C'],label='Hotel C',color='red')

plt.title('Hotel occupancy rate in three hotels in Miami, Florida from January to June 2021')
plt.xlabel('Month')
plt.ylabel('Occupancy rate')

plt.xticks(data['Month'],rotation=45)
plt.legend(bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.savefig('line chart/png/67.png')
plt.clf()