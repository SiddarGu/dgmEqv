
import matplotlib.pyplot as plt
import numpy as np

x=np.array([2020,2021,2022,2023,2024])
y1=np.array([1000,1100,1200,1300,1400])
y2=np.array([20000,19000,18000,17000,16000])
y3=np.array([50000,51000,52000,53000,54000])

fig=plt.figure(figsize=(8,6))
ax1=fig.add_subplot(111)
ax1.plot(x,y1,label='Hospitalizations')
ax1.plot(x,y2,label='Emergency Room Visits')
ax1.plot(x,y3,label='Primary Care Visits')
ax1.set_xlabel('Year')
ax1.xaxis.set_ticks(x)
ax1.set_ylabel('Utilization')
ax1.set_title('Healthcare utilization in the United States from 2020 to 2024')
ax1.legend(loc='best')

for a,b in zip(x,y1):
    ax1.text(a,b+50,str(b))
for a,b in zip(x,y2):
    ax1.text(a,b+50,str(b))
for a,b in zip(x,y3):
    ax1.text(a,b+50,str(b),rotation=45,ha='center',va='bottom',wrap=True)

plt.tight_layout()
plt.savefig('line chart/png/54.png')
plt.clf()