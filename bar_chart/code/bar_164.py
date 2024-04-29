
import matplotlib.pyplot as plt
import numpy as np

Mode = ["Train", "Bus", "Car"]
Travel_Time = [120, 150, 90]
Distance = [500, 400, 300]

plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.bar(Mode, Travel_Time, color='#0072BC', width=0.5, bottom=Distance, label="Travel Time(minutes)")
ax.bar(Mode, Distance, color='#ED1C24', width=0.5, label="Distance(km)")
plt.title('Travel time and distance for different modes of transport')
plt.xticks(Mode)
ax.legend(bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig("bar chart/png/472.png")
plt.clf()