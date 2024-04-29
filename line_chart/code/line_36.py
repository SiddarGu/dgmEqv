
import matplotlib.pyplot as plt
import numpy as np

data = [['January', 30, 20], 
        ['February', 40, 25], 
        ['March', 50, 30], 
        ['April', 60, 35], 
        ['May', 70, 40], 
        ['June', 80, 45], 
        ['July', 90, 50], 
        ['August', 100, 55]]

months, download_speed, upload_speed = zip(*data)

plt.figure(figsize=(10,6)) 
ax = plt.subplot()
ax.plot(months, download_speed, color='b', label='Download Speed(Mbps)')
ax.plot(months, upload_speed, color='r', label='Upload Speed(Mbps)')
ax.set_title('Average Home Internet Speeds in 2021')
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, rotation=90, wrap=True)
ax.legend(loc=2)
plt.tight_layout()
plt.savefig('line chart/png/378.png')
plt.clf()