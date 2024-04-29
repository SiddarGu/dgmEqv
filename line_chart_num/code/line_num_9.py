
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

time = ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00']
speed = [500,400,350,300,250,200,150,100]
altitude = [0,2.5,5,7.5,10,12.5,15,17.5]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

ax.plot(time,speed,color='red',label='Speed(km/h)')
ax.plot(time,altitude,color='blue',label='Altitude(km)')

ax.set_title('Space shuttle\'s speed and altitude change during launch',fontsize=20)
ax.set_xlabel('Time',fontsize=15)
ax.set_ylabel('Value',fontsize=15)

ax.xaxis.set_major_locator(ticker.MultipleLocator(base=1))
ax.annotate('Speed:{} km/h'.format(speed[-1]),xy=(time[-1],speed[-1]),
            xytext=(time[-1],speed[-1]+20),
            arrowprops=dict(facecolor='red',shrink=0.05))
ax.annotate('Altitude:{} km'.format(altitude[-1]),xy=(time[-1],altitude[-1]),
            xytext=(time[-1],altitude[-1]-5),
            arrowprops=dict(facecolor='blue',shrink=0.05))

ax.legend(loc='upper left',fontsize=15)

plt.tight_layout()
plt.savefig('line chart/png/172.png')
plt.clf()