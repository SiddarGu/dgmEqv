
import matplotlib.pyplot as plt

plt.figure(figsize=(10,8))
ax1 = plt.subplot(1,1,1)

ax1.plot(2005,90,marker='o',color='b',label='Enrollment Rate(%)')
ax1.plot(2005,80,marker='o',color='r',label='Graduation Rate(%)')
ax1.plot(2005,15,marker='o',color='g',label='Dropout Rate(%)')
ax1.plot(2006,92,marker='o',color='b')
ax1.plot(2006,83,marker='o',color='r')
ax1.plot(2006,14,marker='o',color='g')
ax1.plot(2007,94,marker='o',color='b')
ax1.plot(2007,85,marker='o',color='r')
ax1.plot(2007,12,marker='o',color='g')
ax1.plot(2008,96,marker='o',color='b')
ax1.plot(2008,87,marker='o',color='r')
ax1.plot(2008,10,marker='o',color='g')
ax1.plot(2009,98,marker='o',color='b')
ax1.plot(2009,89,marker='o',color='r')
ax1.plot(2009,8,marker='o',color='g')

ax1.annotate('90%', xy=(2005,90), xytext=(2005,90.2))
ax1.annotate('80%', xy=(2005,80), xytext=(2005,80.2))
ax1.annotate('15%', xy=(2005,15), xytext=(2005,15.2))
ax1.annotate('92%', xy=(2006,92), xytext=(2006,92.2))
ax1.annotate('83%', xy=(2006,83), xytext=(2006,83.2))
ax1.annotate('14%', xy=(2006,14), xytext=(2006,14.2))
ax1.annotate('94%', xy=(2007,94), xytext=(2007,94.2))
ax1.annotate('85%', xy=(2007,85), xytext=(2007,85.2))
ax1.annotate('12%', xy=(2007,12), xytext=(2007,12.2))
ax1.annotate('96%', xy=(2008,96), xytext=(2008,96.2))
ax1.annotate('87%', xy=(2008,87), xytext=(2008,87.2))
ax1.annotate('10%', xy=(2008,10), xytext=(2008,10.2))
ax1.annotate('98%', xy=(2009,98), xytext=(2009,98.2))
ax1.annotate('89%', xy=(2009,89), xytext=(2009,89.2))
ax1.annotate('8%', xy=(2009,8), xytext=(2009,8.2))

ax1.set_title("Change in Enrollment, Graduation, and Dropout Rates in US Education System", fontsize=14)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Percentage(%)', fontsize=14)
ax1.grid(True)
ax1.legend(loc='best')

plt.xticks(range(2005, 2010))
plt.tight_layout()
plt.savefig('line chart/png/149.png')
plt.close()