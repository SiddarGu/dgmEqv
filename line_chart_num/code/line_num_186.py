
import matplotlib.pyplot as plt
import numpy as np

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
Wind = [50, 60, 65, 70, 75, 80, 85, 90]
Solar = [10, 20, 30, 25, 35, 20, 10, 30]
Hydro = [20, 25, 30, 30, 35, 40, 45, 50]
Nuclear = [30, 35, 40, 50, 45, 50, 55, 60]

plt.figure(figsize=(10, 6))
plt.plot(month, Wind, color='red', marker='o',label='Wind Energy(TWh)')
plt.plot(month, Solar, color='orange', marker='o',label='Solar Energy(TWh)')
plt.plot(month, Hydro, color='blue', marker='o',label='Hydro Energy(TWh)')
plt.plot(month, Nuclear, color='green', marker='o',label='Nuclear Energy(TWh)')

plt.xlabel('Month', fontsize=12)
plt.ylabel('Energy Output(TWh)', fontsize=12)
plt.title('Renewable energy sources production in the USA, 2021')
plt.xticks(np.arange(len(month)), month, fontsize=10, rotation=45)
plt.legend(loc='upper left')

for x, y in zip(month, Wind):
    label = "{:.2f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-3,3), # distance from text to points (x,y)
                 ha='right') # horizontal alignment can be left, right or center

for x, y in zip(month, Solar):
    label = "{:.2f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-3,3), # distance from text to points (x,y)
                 ha='right') # horizontal alignment can be left, right or center

for x, y in zip(month, Hydro):
    label = "{:.2f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-3,3), # distance from text to points (x,y)
                 ha='right') # horizontal alignment can be left, right or center

for x, y in zip(month, Nuclear):
    label = "{:.2f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-3,3), # distance from text to points (x,y)
                 ha='right') # horizontal alignment can be left, right or center

plt.tight_layout()
plt.savefig('line chart/png/127.png')
plt.clf()