
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()
City = np.arange(4)
Hotel_Rooms = [4500,3500,4800,4000]
Tourists = [10000,8000,11000,9000]
ax.bar(City, Hotel_Rooms, bottom=Tourists, label='Hotel Rooms', width=0.5)
ax.bar(City, Tourists, label='Tourists', width=0.5)
ax.set_xticks(City)
ax.set_xticklabels(['Tokyo','London','New York','Paris'], rotation=45, wrap=True)
ax.legend(loc='best')
ax.set_title('Number of hotel rooms and tourists in four major cities in 2021')
plt.tight_layout()
plt.savefig('bar chart/png/557.png')
plt.clf()