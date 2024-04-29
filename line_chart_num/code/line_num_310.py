
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(14,6))
ax=fig.add_subplot()

months = ['January','February','March','April','May','June','July']
car_values = [500,550,600,650,700,750,800]
truck_values = [100,110,120,125,130,140,145]
motorbike_values = [1000,900,800,700,600,500,400]
train_values = [200,225,250,275,300,325,350]

ax.plot(months, car_values, color = 'red', label = 'Cars')
ax.plot(months, truck_values, color = 'green', label = 'Trucks')
ax.plot(months, motorbike_values, color = 'blue', label = 'Motorbikes')
ax.plot(months, train_values, color = 'orange', label = 'Trains')

plt.title('Overview of Motor Vehicle Transportation in the United States in 2021')

plt.xlabel('Month')
plt.ylabel('Number of Vehicles (thousands)')

plt.xticks(months)

plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), shadow=True, ncol=1)

for x,y in zip(months, car_values):
    label = "{:.1f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center',
                 wrap=True)

for x,y in zip(months, truck_values):
    label = "{:.1f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center',
                 wrap=True)

for x,y in zip(months, motorbike_values):
    label = "{:.1f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center',
                 wrap=True)

for x,y in zip(months, train_values):
    label = "{:.1f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center',
                 wrap=True)

plt.tight_layout()
plt.savefig('line chart/png/118.png')
plt.clf()